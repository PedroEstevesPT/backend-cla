# Unbabel Backend Engineer Challenge by Pedro Esteves

## Index

1. [How to Install Command Line Application](#how-to-install-command-line-application)
2. [How to Use the Command Line Application](#how-to-use)
3. [Algorithm Complexity](#algorithm-complexity)
4. [Implementation Notes](#implementation-notes)
5. [Tests](#tests)
6. [Test List](#test-list)

## How to Install Command Line Application

Check if you have the virtualenv package installed by running the following command:

``` virtualenv --version``` 

If you do not have it, you can install it with:

``` pip install virtualenv ``` 

Then, create a virtual environment with:

```  virtualenv -p python3.7 venv ``` 

Activate the virtual environment on Linux/Mac:

``` source venv/bin/activate ``` 

Install project dependencies:

```  pip install -r requirements.txt ``` 

Deactivate the virtual environment:

```  deactivate ``` 

## How to Use:

Run the Command Line App:

``` python unbabel_cli.py --input_file tests/inputs/test_default.json --window_size 10 --output_file tmp.json ```

You can add a flag `--print` to print the result in the CLI besides saving it on a file.

``` python unbabel_cli.py --input_file tests/inputs/test_default.json --window_size 10 --output_file tmp.json --print ```

You can add a flag `--time` to print the execution time of the CLI.

You can add a flag `--algorithm {deque,prefix}` to choose an algorithm to calculate the moving average. Both have a space complexity of O(n) for the average case, where n is the number of events, but the deque algorithm is better for the worst case. You can observe that by running a worst case performance test (events spaced by a big time interval):

``` python unbabel_cli.py --input_file tests/inputs/test_big_event_gap.json --window_size 10 --output_file tmp.json --time --algorithm deque ```

or

``` python unbabel_cli.py --input_file tests/inputs/test_big_event_gap.json --window_size 10 --output_file tmp.json --time --algorithm prefix ```

If you do not use the `--algorithm` flag, the algorithm will default to deque.

## Algorithm Complexity:

#### Deque Algorithm (best) ####

<b>Time Complexity: O(n) </b>
- The algorithm calculates the start and end time. This step takes constant time since we know the input is sorted.
- Creating a prefix sum array. This step has a time complexity of O(n) as it requires iterating through each event to calculate cumulative durations.
- Iterating through each minute between the start and end time. This step takes O(m), where m is the number of minutes between the start and end time, resulting in a complexity of O(n). In the worst case, the number of minutes can dominate the time complexity, making it O(m) rather than O(n).
- Finding events within the window takes O(k), where k is the number of events in the current window, resulting in a complexity of O(n).
- The remaining steps have constant time complexity.

<b>Space Complexity: O(n)</b>
The deque algorithm uses a deque data structure to store the events within the window. Additionally, a prefix sum array of length n+1 is created to store the cumulative duration of the events. Therefore, the space complexity is O(n). Other variables used are constants. For limit cases where the events are spaced between days, weeks, months etc... the deque provides better memory management.

#### Prefix Algorithm
<b> Time complexity: O(n). </b>
- The algorithm calculates the start and end time. This step takes constant time since we know the input is sorted.
- Creating a prefix sum array. This step has a time complexity of O(n) as it requires iterating through each event to calculate cumulative durations.
- Iterating through each minute between start and end time. This step takes O(m), where m is the number of minutes between the start and end time, resulting in a complexity of O(n). In the worst case, the number of minutes can dominate the time complexity, making it O(m) rather than O(n).
- Finding events within the window takes O(k), where k is the number of events in the current window, resulting in a complexity of O(n).
- The rest of the steps are constant.

<b> Space complexity: O(n). </b>
The prefix algorithm uses an array to store the cumulative duration of the events with a length of n+1, where n is the number of events. Other variables used are constants.

The reason why deque algorithm is better than the prefix algorithm has to do with the first inner while condition being much faster in the deque algorithm than in the prefix:

(DEQUE) 1st while condition: 
```while window and parse(window[0]['timestamp']) <= window_low_lim:```
(PREFIX) 1st while condition: 
```while start_index < len_events and parse(events[start_index]['timestamp']) <= window_low_lim:```

Deque while is faster because only checks if the 'window' (deque) is empty or not which can be done in constant time.
In the cases where the events are very spaced this drastically improves the speed because most of the times the condition
will return false and the second part will not be evaluated. THe same does not apply to the prefix algorithm.

## Implementation Notes

The strategy pattern is used in the `DequeAverageDeliveryTimeCalculator` class and the `PrefixAverageDeliveryTimeCalculator` class (both inherit from `MovingAverageCalculator`). This pattern provides flexibility and extensibility in the code. If new algorithms for calculating the average delivery times are needed in the future, they can be added by implementing the `MovingAverageCalculator` interface without modifying the existing code.

## Tests

Run a single test:

```python3.7 -m unittest tests/test_default.py```

Run all tests:

```./run_tests.sh```

## Test List

- `test_0_events`: Tests CLI with an input file with 0 events. Raises an error.
- `test_1_event`: Tests just 1 event. Valid case.
- `test_2_events`: Tests 2 events. Valid case.
- `test_default`: Test provided in the exercise. Valid case.
- `test_different_window_size`: Tests the algorithm for different valid window sizes. Valid cases.
- `test_end_year`: Tests events that happen on YYYY-12-31 23:59:SS. Valid case.
- `test_invalid_cli`: Tests where CLI does not have `--input_file`, `--output_file`, or `--windows_size`. Raises an error.
- `test_invalid_input`: Tests an input where the duration is a string instead of a number. Raises an error.
- `test_leap_year`: Tests events that happen on 2022-02-28 23:59:SS (leap year) and non-leap year. Valid cases.
- `test_multiple_events_window_1`: Big test. Empirical proof that the algorithm is better than the naive algorithm and that deque beats prefix. Valid case.