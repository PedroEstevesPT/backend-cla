import unittest
import subprocess
import traceback

class UnbabelCLITestCase(unittest.TestCase):
    def test_0_events(self):

        input_file = 'tests/inputs/test_0_events.json'

        command = ['python', 'unbabel_cli.py', '--input_file', input_file, '--window_size', '5']
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            stderr = e.stderr
            # Check if the error message contains 'ValueError'
            error_message = stderr.split("\n")[-2]
            if error_message.startswith('ValueError:'):
                self.assertEqual(error_message, "ValueError: There must be at least 1 event for the moving average to be calculated.")
