"""Shared checks for native JDK 25 article compilation."""
from pathlib import Path
import re
import shutil
import struct
import subprocess


def require_jdk25():
    versions = {}
    for command in ('java', 'javac'):
        executable = shutil.which(command)
        if not executable:
            raise RuntimeError(f'{command} is missing; install JDK 25 and check PATH')
        result = subprocess.run(
            [executable, '-version'], capture_output=True, text=True, timeout=30,
        )
        output = result.stdout + result.stderr
        pattern = r'(?:openjdk|java) version "([^"]+)"' if command == 'java' else r'javac\s+(\S+)'
        match = re.search(pattern, output)
        if result.returncode or not match or match[1].split('.')[0] != '25':
            raise RuntimeError(f'{command} must be version 25; received: {output.strip()}')
        versions[command] = match[1]
    print(f'JDK 25: java {versions["java"]}; javac {versions["javac"]}')
    return versions


def check_class_versions(directory):
    classes = sorted(Path(directory).rglob('*.class'))
    if not classes:
        raise RuntimeError(f'{directory}: no compiled classes found')
    for path in classes:
        header = path.read_bytes()[:8]
        if len(header) != 8 or header[:4] != b'\xca\xfe\xba\xbe':
            raise RuntimeError(f'{path}: invalid class header')
        minor, major = struct.unpack('>HH', header[4:])
        if (minor, major) != (0, 69):
            raise RuntimeError(f'{path}: expected native Java 25 class version 69.0, got {major}.{minor}')
    return len(classes)
