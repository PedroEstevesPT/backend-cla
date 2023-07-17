import argparse
import time
from algorithms.deque_average_delivery_time_calculator import DequeAverageDeliveryTimeCalculator
from algorithms.prefix_average_delivery_time_calculator import PrefixAverageDeliveryTimeCalculator
from utils import float2string , parse_events , write_output , print_output

def main(input_file: str, output_file: str, window_size: int, print_output_flag: bool, algorithm: str, show_time: bool) -> None:
    try:
        events = parse_events(input_file)
        start_time = time.time()

        if algorithm == 'prefix':
            calculator = PrefixAverageDeliveryTimeCalculator()
        else:
            calculator = DequeAverageDeliveryTimeCalculator()

        average_delivery_times = calculator.calculate_average(events, window_size)


        end_time = time.time()

        write_output(output_file, average_delivery_times)

        if print_output_flag:
            print_output(average_delivery_times)

        if show_time:
            execution_time = end_time - start_time
            print(f"Execution time: {execution_time:.2f} seconds")
            
    except TypeError as e: 
        raise TypeError(e) from e

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Unbabel Engineering Challenge')
    parser.add_argument('--input_file', type=str, help='Input file path')
    parser.add_argument('--output_file', type=str, help='Output file path')
    parser.add_argument('--window_size', type=int, help='Window size for moving average')
    parser.add_argument('--print', action='store_true', help='Print output')
    parser.add_argument('--algorithm', type=str, choices=['deque', 'prefix'], default='deque', help='Algorithm choice')
    parser.add_argument('--time', action='store_true', default=False , help='Print execution time')

    args = parser.parse_args()

    if  args.input_file is None or args.window_size is None:
        raise ValueError("Both --input_file and --window_size must be provided.")

    main(args.input_file, args.output_file, args.window_size,args.print,args.algorithm,args.time)