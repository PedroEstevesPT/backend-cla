import unittest
import subprocess
import os

class UnbabelCLITestCase(unittest.TestCase):
    def test_invalid_cli_input(self):

        input_file = 'tests/inputs/test_invalid_cli_input.json'
 
        command = ['python', 'unbabel_cli.py', '--input_file', input_file]
        result = subprocess.run(command, capture_output=True, text=True).stderr.split("\n")[-2]
        self.assertEqual(result, "ValueError: Both --input_file and --window_size must be provided.")

        command = ['python', 'unbabel_cli.py', '--window_size', '10']
        result = subprocess.run(command, capture_output=True, text=True).stderr.split("\n")[-2]
        self.assertEqual(result, "ValueError: Both --input_file and --window_size must be provided.")

        command = ['python', 'unbabel_cli.py']
        result = subprocess.run(command, capture_output=True, text=True).stderr.split("\n")[-2]
        self.assertEqual(result, "ValueError: Both --input_file and --window_size must be provided.")
