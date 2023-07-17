import unittest
import subprocess
import os

class UnbabelCLITestCase(unittest.TestCase):
    def test_average_delivery_time(self):

        input_file       = 'tests/inputs/test_default.json'
        result_file      = 'tests/golden_outputs/test_default.json'
        test_result_file = 'tests/tmp.json'

        command = ['python', 'unbabel_cli.py', '--input_file', input_file, '--window_size', '10','--output_file',test_result_file]
        result = subprocess.run(command, capture_output=True, text=True)

        with open(result_file, 'r') as test_result, open(test_result_file, 'r') as golden_result:
            self.assertEqual(test_result.read(), golden_result.read())

        os.remove(test_result_file)
