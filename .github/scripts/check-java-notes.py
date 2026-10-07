"""Compile article examples and compare their stdout with the documented output.

Requires Python 3.9+ and JDK 25 for both compilation and execution. Compilation happens in a
temporary directory; source articles are never modified and no JARs are fetched.

Usage:
    python3 .github/scripts/check-java-notes.py --standard-only
    python3 .github/scripts/check-java-notes.py --classpath '/path/to/lib/*'

The full check needs HikariCP 7.0.2, H2 2.4.240 and SLF4J API 2.0.17 on the
classpath. JAVA_NOTES_CLASSPATH can supply the same value as --classpath.
"""

import argparse
import difflib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from jdk25 import check_class_versions, require_jdk25


ROOT = Path(__file__).resolve().parents[2]
ARTICLES = (
    ("polymorphism.md", "PolymorphismDemo", False),
    ("HikariPool-1-error.md", "PoolTimeoutDemo", True),
    ("java-DecimalFormat.md", "DecimalFormatDemo", False),
)
FENCED_BLOCK = re.compile(
    r"^```(?P<language>\w+)[ \t]*\r?\n(?P<body>.*?)^```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


def extract_example(path, class_name):
    """Require one runnable Java block and one following text output block."""
    content = path.read_text(encoding="utf-8")
    blocks = list(FENCED_BLOCK.finditer(content))
    java_blocks = [block for block in blocks if block["language"] == "java"]
    if len(java_blocks) != 1:
        raise ValueError(f"{path.name}: expected exactly one Java fenced block")
    java_block = java_blocks[0]
    source = java_block["body"]
    if not re.search(rf"\bpublic\s+class\s+{re.escape(class_name)}\b", source):
        raise ValueError(f"{path.name}: missing public class {class_name}")
    outputs = [
        block for block in blocks
        if block["language"] == "text" and block.start() > java_block.end()
    ]
    if len(outputs) != 1 or not outputs[0]["body"].strip():
        raise ValueError(f"{path.name}: expected one nonempty text output after Java")
    return source, outputs[0]["body"].rstrip("\r\n") + "\n"


def run_command(command, directory):
    result = subprocess.run(
        command, cwd=directory, capture_output=True, text=True,
        encoding="utf-8", timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {command[0]}\n"
            f"{result.stdout}{result.stderr}"
        )
    return result.stdout


def check_output(command, directory, expected, label):
    actual = run_command(command, directory)
    if actual != expected:
        difference = "".join(difflib.unified_diff(
            expected.splitlines(keepends=True), actual.splitlines(keepends=True),
            fromfile="documented output", tofile="actual output",
        ))
        raise RuntimeError(f"{label}: output mismatch\n{difference}")
    print(f"PASS {label}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--classpath", default=os.environ.get("JAVA_NOTES_CLASSPATH", ""),
        help="HikariCP/H2/SLF4J JAR paths separated by the OS classpath separator",
    )
    parser.add_argument(
        "--standard-only", action="store_true",
        help="Explicitly run only the two examples that need no external JARs",
    )
    parser.add_argument('--results', type=Path, help='Write verified article results as JSON')
    args = parser.parse_args()
    versions = require_jdk25()
    java, javac = shutil.which("java"), shutil.which("javac")
    if not java or not javac:
        parser.error("java and javac must be available on PATH")
    if not args.standard_only and not args.classpath:
        parser.error("Full checks need --classpath; use --standard-only for JDK examples")

    # Temporary compilation runs in another cwd; resolve relative JAR paths here.
    dependencies = os.pathsep.join(
        str(Path(entry).expanduser().absolute())
        for entry in args.classpath.split(os.pathsep) if entry
    )
    checked = 0
    results = {}
    with tempfile.TemporaryDirectory(prefix="java-notes-") as temporary:
        for filename, class_name, external in ARTICLES:
            if external and args.standard_only:
                continue
            source, expected = extract_example(ROOT / "content/post/java" / filename, class_name)
            directory = Path(temporary) / class_name
            directory.mkdir()
            source_file = directory / f"{class_name}.java"
            source_file.write_text(source, encoding="utf-8")
            compile_command = [javac, "-encoding", "UTF-8"]
            runtime_classpath = str(directory)
            if external:
                compile_command.extend(["-cp", dependencies])
                runtime_classpath += os.pathsep + dependencies
            compile_command.append(str(source_file))
            run_command(compile_command, directory)
            class_count = check_class_versions(directory)
            java_command = [java, "-Dfile.encoding=UTF-8", "-cp", runtime_classpath]
            check_output(java_command + [class_name], directory, expected, class_name)
            if class_name == "DecimalFormatDemo":
                check_output(
                    java_command + ["-Duser.language=de", "-Duser.country=DE", class_name],
                    directory, expected, f"{class_name} (German default locale)",
                )
            checked += 1
            detail = {
                'PoolTimeoutDemo': 'HikariCP 7.0.2／H2 2.4.240／SLF4J API 2.0.17；借滿、逾時與釋放後再借',
                'DecimalFormatDemo': '預設與德文 locale',
                'PolymorphismDemo': '多型呼叫',
            }[class_name]
            results[f'content/post/java/{filename}'] = (
                f'JDK 25 原生編譯與執行（java {versions["java"]}／javac {versions["javac"]}；'
                f'{class_count} 個 class 均為版本 69）；{detail}，標準輸出逐字比對通過'
            )
    mode = "JDK-only" if args.standard_only else "full"
    print(f"Verified {checked} article examples ({mode}).")
    if args.results:
        args.results.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
