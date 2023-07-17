import unittest
import subprocess

class UnbabelCLITestCase(unittest.TestCase):
    def test_end_year(self):

        input_file =       'tests/inputs/test_end_year.json'
        result_file      = 'tests/golden_outputs/test_end_year.json'
        test_result_file = 'tests/tmp.json'

        command = ['python', 'unbabel_cli.py', '--input_file', input_file, '--window_size', '5','--output_file',test_result_file]
                
        result = subprocess.run(command, capture_output=True, text=True)

        with open(test_result_file, 'r') as test_result, open(result_file, 'r') as golden_result:

            self.assertEqual(test_result.read(), golden_result.read())
