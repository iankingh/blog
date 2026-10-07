"""Reject mismatched JDKs and downgraded or preview bytecode."""
from pathlib import Path
import struct
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from jdk25 import check_class_versions, require_jdk25


class Jdk25Checks(unittest.TestCase):
    def versions(self, java, javac):
        responses = [
            subprocess.CompletedProcess([], 0, '', f'openjdk version "{java}"'),
            subprocess.CompletedProcess([], 0, f'javac {javac}', ''),
        ]
        with patch('jdk25.shutil.which', side_effect=lambda name: f'/jdk/bin/{name}'), patch('jdk25.subprocess.run', side_effect=responses):
            return require_jdk25()

    def test_native_25(self):
        self.assertEqual(self.versions('25.0.4.1', '25.0.4.1')['javac'], '25.0.4.1')

    def test_old_runtime(self):
        with self.assertRaisesRegex(RuntimeError, 'java must be version 25'):
            self.versions('21.0.1', '25.0.4.1')

    def test_old_compiler(self):
        with self.assertRaisesRegex(RuntimeError, 'javac must be version 25'):
            self.versions('25.0.4.1', '21.0.1')

    def test_missing_tool(self):
        with patch('jdk25.shutil.which', return_value=None), self.assertRaisesRegex(RuntimeError, 'missing'):
            require_jdk25()

    def test_bytecode_versions(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'Demo.class'
            for minor, major in ((0, 52), (0, 65), (65535, 69)):
                with self.subTest(minor=minor, major=major):
                    path.write_bytes(b'\xca\xfe\xba\xbe' + struct.pack('>HH', minor, major))
                    with self.assertRaisesRegex(RuntimeError, 'expected native Java 25'):
                        check_class_versions(temporary)
            path.write_bytes(b'\xca\xfe\xba\xbe' + struct.pack('>HH', 0, 69))
            self.assertEqual(check_class_versions(temporary), 1)
            path.write_bytes(b'not a class')
            with self.assertRaisesRegex(RuntimeError, 'invalid class'):
                check_class_versions(temporary)

    def test_no_compiled_classes(self):
        with tempfile.TemporaryDirectory() as temporary, self.assertRaisesRegex(RuntimeError, 'no compiled classes'):
            check_class_versions(temporary)


if __name__ == '__main__':
    unittest.main()
