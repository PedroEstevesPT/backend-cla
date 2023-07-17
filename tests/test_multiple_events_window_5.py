import unittest
import subprocess
import os

class UnbabelCLITestCase(unittest.TestCase):
    def test_multiple_events_window_5(self):

        input_file =       'tests/inputs/test_multiple_events_window_1.json'
        result_file      = 'tests/golden_outputs/test_multiple_events_window_1.json'
        test_result_file = 'tests/tmp.json'

        command = ['python', 'unbabel_cli.py', '--input_file', input_file, '--window_size', '1','--output_file',test_result_file]
                
        result = subprocess.run(command, capture_output=True, text=True)

        with open(test_result_file, 'r') as test_result, open(result_file, 'r') as golden_result:
            self.assertEqual(test_result.read(), golden_result.read())

        os.remove(test_result_file)