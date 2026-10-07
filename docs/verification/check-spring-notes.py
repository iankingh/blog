"""Build the six Spring articles with JDK 25 in an isolated directory.

Usage: python3 docs/verification/check-spring-notes.py /tmp/blog-spring-lab
       --maven-repo /tmp/blog-m2 --results /tmp/blog-spring-results.json
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.github/scripts'))
from jdk25 import check_class_versions, require_jdk25


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--maven-repo', type=Path)
    parser.add_argument('--results', type=Path)
    args = parser.parse_args()
    versions = require_jdk25()
    lab = args.directory.resolve()
    if lab == ROOT or ROOT in lab.parents:
        parser.error('Use an isolated directory outside the repository')
    subprocess.run([sys.executable, str(Path(__file__).with_name('prepare-spring-lab.py')), str(lab)], check=True)
    command = ['mvn', '-B', '-f', str(lab / 'pom.xml')]
    if args.maven_repo:
        command.append(f'-Dmaven.repo.local={args.maven_repo.resolve()}')
    # Confirm the Maven process uses JDK 25 too, before allowing it to compile.
    info = subprocess.check_output(command + ['-version'], text=True, stderr=subprocess.STDOUT)
    if not re.search(r'Java version: 25(?:\.|,|\s)', info):
        raise RuntimeError(f'Maven must use JDK 25:\n{info}')
    subprocess.run(command + ['clean', 'test'], check=True)
    class_count = check_class_versions(lab / 'target/classes')
    test_class_count = check_class_versions(lab / 'target/test-classes')
    totals = dict.fromkeys(('tests', 'failures', 'errors', 'skipped'), 0)
    reports = sorted((lab / 'target/surefire-reports').glob('TEST-*.xml'))
    for report in reports:
        suite = ET.parse(report).getroot()
        for key in totals:
            totals[key] += int(suite.attrib[key])
    if totals != {'tests': 8, 'failures': 0, 'errors': 0, 'skipped': 0}:
        raise RuntimeError(f'Expected 8 passing Spring tests: {totals}')
    result = {
        'java': versions['java'], 'javac': versions['javac'],
        'springBoot': '3.5.16', 'springdoc': '2.8.9', 'h2': '2.3.232',
        'classMajorVersion': 69, 'mainClasses': class_count,
        'testClasses': test_class_count, **totals,
        'scope': '六篇文章抽取程式與本地 H2；API／profile／查詢另用 fixture，未連外部 DB 或叢集',
    }
    if args.results:
        args.results.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('PASS Spring JDK 25:', json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError, ET.ParseError) as error:
        raise SystemExit(f'FAIL {error}')
