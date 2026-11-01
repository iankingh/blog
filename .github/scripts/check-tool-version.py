"""Check the running tools against the project's Node pin and CI Hugo version."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def check_node(expected, runtime):
    if not re.fullmatch(r"\d+\.\d+\.\d+", expected):
        raise ValueError(".nvmrc must pin an exact Node version")
    actual = runtime["version"].removeprefix("v")
    if actual != expected:
        raise ValueError(f"Node {actual} differs from .nvmrc {expected}; use the pinned version")
    if not runtime.get("lts"):
        raise ValueError(f"Node {actual} is not an LTS build")
    return f"Node {actual} LTS ({runtime['lts']}); matches .nvmrc"


def check_hugo(expected, output):
    match = re.search(r"hugo v(\d+\.\d+\.\d+)([^\s]*)", output)
    if not match or "+extended" not in match[2]:
        raise ValueError("Hugo Extended is required")
    actual = match[1]
    if tuple(map(int, actual.split("."))) < tuple(map(int, expected.split("."))):
        raise ValueError(f"Hugo {actual} is older than the CI version {expected}")
    warning = None
    if actual != expected:
        warning = (f"Hugo {actual} differs from CI {expected}; "
                   "this run does not verify the pinned CI Hugo version")
    return output.strip(), warning


def ci_hugo_version(root):
    versions = []
    for name in ("deploy.yml", "verify.yml"):
        text = (root / ".github/workflows" / name).read_text()
        matches = re.findall(r"hugo-version:\s*['\"](\d+\.\d+\.\d+)['\"]", text)
        if len(matches) != 1:
            raise ValueError(f"{name} must pin exactly one Hugo version")
        versions.extend(matches)
    if len(set(versions)) != 1:
        raise ValueError("Deploy and PR workflows pin different Hugo versions")
    return versions[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tool", choices=("node", "hugo"))
    args = parser.parse_args()
    if args.tool == "node":
        raw = subprocess.check_output([
            "node", "-p", "JSON.stringify({version:process.version,lts:process.release.lts||false})"
        ], text=True)
        print(check_node((ROOT / ".nvmrc").read_text().strip(), json.loads(raw)))
    else:
        output = subprocess.check_output(["hugo", "version"], text=True)
        message, warning = check_hugo(ci_hugo_version(ROOT), output)
        print(message)
        if warning:
            print("WARNING: " + warning)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as error:
        raise SystemExit(f"FAIL {error}")
