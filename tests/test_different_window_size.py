import unittest
import subprocess
import os

class UnbabelCLITestCase(unittest.TestCase):
    def test_different_window_size(self):

        for window_size in ['0','5']:

            input_file = 'tests/inputs/test_different_window_size.json'
            result_file = 'tests/golden_outputs/test_window_{}.json'.format(window_size)
            test_result_file = 'tests/tmp.json'

            command = ['python', 'unbabel_cli.py', '--input_file',input_file, '--window_size',window_size,'--output_file',test_result_file]
            result = subprocess.run(command, capture_output=True, text=True)

            with open(test_result_file, 'r') as test_result, open(result_file, 'r') as golden_result:
                self.assertEqual(test_result.read(), golden_result.read())

            os.remove(test_result_file)
