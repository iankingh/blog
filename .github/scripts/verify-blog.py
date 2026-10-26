"""Run the blog's checks and retain evidence outside the source tree (stdlib)."""
import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Step:
    name: str
    command: tuple
    needs: tuple = ()


def source_state(root):
    def git(*args):
        return subprocess.check_output(["git", *args], cwd=root)

    head = git("rev-parse", "HEAD").decode().strip()
    status = git("status", "--porcelain=v1", "--untracked-files=all")
    submodules = git("submodule", "status", "--recursive")
    digest = hashlib.sha256(head.encode() + status + submodules)
    digest.update(git("diff", "HEAD", "--binary"))
    for name in sorted(git("ls-files", "--others", "--exclude-standard", "-z").split(b"\0")):
        if not name:
            continue
        path = root / os.fsdecode(name)
        digest.update(name + b"\0")
        if path.is_symlink():
            digest.update(os.fsencode(os.readlink(path)))
        elif path.is_file():
            digest.update(str(path.stat().st_mode).encode())
            digest.update(path.read_bytes())
    # A dirty gitlink marker alone cannot distinguish two different theme edits.
    for entry in git("ls-files", "--stage", "-z").split(b"\0"):
        if entry.startswith(b"160000 "):
            name = entry.partition(b"\t")[2]
            child = root / os.fsdecode(name)
            if (child / ".git").exists():
                digest.update(name + source_state(child)["fingerprint"].encode())
    return {"commit": head, "dirty": bool(status),
            "fingerprint": digest.hexdigest(),
            "submodules": submodules.decode().splitlines()}


def run_step(step, root, output, timeout, env):
    log_path = output / "logs" / (step.name + ".log")
    result = {"name": step.name, "command": list(step.command),
              "log": str(log_path), "status": "failed", "exit_code": None}
    started = time.monotonic()
    with log_path.open("w", encoding="utf-8") as log:
        try:
            process = subprocess.Popen(step.command, cwd=root, stdout=log,
                                       stderr=subprocess.STDOUT, env=env,
                                       start_new_session=(os.name == "posix"))
            try:
                code = process.wait(timeout=timeout)
                result.update(exit_code=code, status="passed" if code == 0 else "failed")
            except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
                # Kill descendants too, so a failed check cannot leave a server running.
                if os.name == "posix":
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                else:
                    process.kill()
                process.wait()
                if isinstance(error, KeyboardInterrupt):
                    result.update(status="interrupted", error="Verification interrupted")
                else:
                    result.update(status="timed_out", error=f"Exceeded {timeout:g} seconds")
        except OSError as error:
            result.update(status="unavailable", error=str(error))
            log.write(str(error) + "\n")
    result["seconds"] = round(time.monotonic() - started, 3)
    return result


def execute_plan(steps, root, output, timeout, env, on_result=None):
    results, statuses = [], {}
    interrupted = False
    (output / "logs").mkdir()
    for step in steps:
        missing = [name for name in step.needs if statuses.get(name) != "passed"]
        if missing or interrupted:
            result = {"name": step.name, "command": list(step.command),
                      "status": "skipped", "reason": "Verification interrupted" if interrupted else
                      "Prerequisite not passed: " + ", ".join(missing)}
        else:
            result = run_step(step, root, output, timeout, env)
        results.append(result)
        statuses[step.name] = result["status"]
        interrupted = interrupted or result["status"] == "interrupted"
        if on_result:
            on_result(result)
        print(f"{result['status'].upper():11} {step.name}", flush=True)
    return results


def site_plan(output):
    scripts = ".github/scripts/"
    site = str(output / "site")
    return [
        Step("hugo-version", ("hugo", "version")),
        Step("node-version", ("node", "--version")),
        Step("python-version", (sys.executable, "--version")),
        Step("note-source", (sys.executable, scripts + "check-note-content.py")),
        Step("search", ("node", scripts + "check-search.cjs"), ("node-version",)),
        Step("diagrams", ("node", scripts + "check-diagrams.cjs"), ("node-version",)),
        Step("python-unit-tests", (sys.executable, "-m", "unittest", "discover",
                                   "-s", scripts, "-p", "test_*.py")),
        Step("build", ("hugo", "--minify", "--noBuildLock", "--cacheDir",
                       str(output / "cache"), "--destination", site), ("hugo-version",)),
        Step("generated-content", (sys.executable, scripts + "check-note-content.py",
                                   "--site", site), ("build",)),
        Step("generated-security", (sys.executable, scripts + "check-site-security.py", site),
             ("build",)),
    ]


def all_passed(results):
    return bool(results) and all(row["status"] == "passed" for row in results)


def save_report(output, report):
    temporary = output / "report.json.tmp"
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(output / "report.json")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New directory outside this repository; never reused")
    parser.add_argument("--timeout", type=float, default=300, help="Positive per-check timeout in seconds")
    args = parser.parse_args(argv)
    if args.timeout <= 0 or not args.timeout < float("inf"):
        parser.error("--timeout must be finite and positive")
    root = ROOT.resolve()
    if args.output:
        output = args.output.expanduser().resolve()
        if output == root or root in output.parents:
            parser.error("--output must be outside the source repository")
        try:
            output.mkdir(parents=True, exist_ok=False)
        except OSError as error:
            parser.error(f"Cannot create a fresh output directory: {error}")
    else:
        output = Path(tempfile.mkdtemp(prefix="blog-harness-")).resolve()
    report = {"schema_version": 1, "scope": "site", "root": str(root),
              "started_at": datetime.now(timezone.utc).isoformat(),
              "output": str(output), "status": "running", "checks": [],
              "limitations": ["Does not rerun Java, Spring, Vue or Angular tutorial examples",
                              "Does not verify browser layout or publish the site",
                              "Ignored files are excluded from the source fingerprint"]}
    print(f"Evidence: {output}", flush=True)
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HUGO_RESOURCEDIR"] = str(output / "resources")
    def checkpoint(result):
        report["checks"].append(result)
        save_report(output, report)

    try:
        report["source_before"] = source_state(root)
        save_report(output, report)
        report["checks"] = execute_plan(site_plan(output), root, output, args.timeout, env, checkpoint)
        report["source_after"] = source_state(root)
        report["source_unchanged"] = report["source_before"] == report["source_after"]
        if not report["source_unchanged"]:
            report["error"] = "Source changed during verification; run again on a stable tree"
        if all_passed(report["checks"]) and report["source_unchanged"]:
            report["status"] = "passed"
    except (OSError, subprocess.SubprocessError, KeyboardInterrupt) as error:
        report["error"] = str(error)
    finally:
        if report["status"] != "passed":
            report["status"] = "failed"
        report["finished_at"] = datetime.now(timezone.utc).isoformat()
        save_report(output, report)
    print(f"{report['status'].upper()}: {output / 'report.json'}", flush=True)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
