"""Extract and run the two Fred article examples in an isolated directory.

Redis Lua is documentation-only here: this script does not start Redis or a cluster.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.github/scripts'))
from jdk25 import require_jdk25, check_class_versions


def block(article, language):
    matches = re.findall(r'^```' + language + r'\n(.*?)^```\s*$', article, re.M | re.S)
    if len(matches) != 1:
        raise ValueError(f'Expected exactly one {language} example')
    return matches[0]


def run(command, directory):
    result = subprocess.run(command, cwd=directory, text=True, capture_output=True, timeout=60)
    if result.returncode:
        raise RuntimeError(f'{command}: {result.stdout}\n{result.stderr}')
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path)
    args = parser.parse_args()
    lottery = next((ROOT / 'content/post/system-design').glob('▶️ YT-Fred 那些年*.md'))
    solid = next((ROOT / 'content/post/software-design').glob('▶️ YT-Fred 聊 SOLID*.md'))
    versions = require_jdk25()
    with tempfile.TemporaryDirectory(prefix='blog-fred-examples-') as directory:
        work = Path(directory)
        (work / 'weighted-draw.mjs').write_text(block(lottery.read_text(), 'javascript'))
        node_output = run(['node', 'weighted-draw.mjs'], work)
        if node_output != 'PASS: 機率區間與無效輸入':
            raise ValueError(f'Unexpected Node output: {node_output}')
        # Enumerate the full random-index space to check the stated weights.
        with (work / 'weighted-draw.mjs').open('a') as stream:
            stream.write('\nconst counts = new Map(table.map(row => [row.prize, 0]));\n'
                         'for (let i = 0; i < total; i++) {\n'
                         ' const prize = draw(i); counts.set(prize, counts.get(prize) + 1);\n'
                         '}\nassert.deepEqual([...counts.values()], [50, 200, 750, 9000]);\n')
        run(['node', 'weighted-draw.mjs'], work)
        (work / 'SolidInvoiceDemo.java').write_text(block(solid.read_text(), 'java'))
        run(['javac', '-encoding', 'UTF-8', 'SolidInvoiceDemo.java'], work)
        classes = check_class_versions(work)
        java_output = run(['java', 'SolidInvoiceDemo'], work)
        expected = 'memory-a: amount=200\nmemory-b: amount=200\ninvalid invoice: rejected'
        if java_output != expected:
            raise ValueError(f'Unexpected Java output: {java_output}')
        report = {
            'checkedAt': datetime.now(timezone.utc).isoformat(),
            'status': 'passed', 'jdk': versions,
            'node': run(['node', '--version'], work),
            'nodeChecks': '8 boundaries, 4 invalid inputs, random selection, all 10000 indices',
            'nodeOutput': node_output, 'javaOutput': java_output,
            'javaClassCount': classes, 'classMajorVersion': 69,
            'javaChecks': 'two memory-store configurations, save/read, overwrite, blank id rejected',
            'limitations': ['Redis Lua not executed; no real cloud storage, concurrent service or load test'],
        }
    if args.results:
        args.results.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
