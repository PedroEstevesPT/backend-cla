import unittest
import subprocess
import traceback

class UnbabelCLITestCase(unittest.TestCase):
    def test_invalid_input_json(self):

        input_file = 'tests/inputs/test_invalid_input_json.json'

        command = ['python', 'unbabel_cli.py', '--input_file', input_file, '--window_size', '10']

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)

        except subprocess.CalledProcessError as e:
            stderr = e.stderr.strip().split("\n")[-1]
            self.assertEqual(stderr, "TypeError: unsupported operand type(s) for +: 'int' and 'str'")

