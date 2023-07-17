import datetime
from dateutil.parser import parse
from typing import List, Dict
from utils import round_down_to_minute, round_up_to_minute
from algorithms.moving_average_calculator import MovingAverageCalculator


class PrefixAverageDeliveryTimeCalculator(MovingAverageCalculator):
    def calculate_average(self, events: List[Dict[str, str]], window_size: int) -> List[Dict[str, float]]:
        average_delivery_times = []
        delivery_times = []
        window_start = None

        if len(events) < 1: 
            raise ValueError("There must be at least 1 event for the moving average to be calculated.")

        start_time = round_down_to_minute(events[0]['timestamp'])
        end_time = round_up_to_minute(events[-1]['timestamp'])
        
        # Create a prefix sum array for the durations
        prefix_sum = [0] * (len(events) + 1)
        for i, event in enumerate(events):
            prefix_sum[i + 1] = prefix_sum[i] + event['duration']

        # Iterate from the start_time to the end_time, incrementing by 1 minute
        current_time = start_time
        event_index = 0

        while current_time <= end_time:

            window_low_lim = current_time - datetime.timedelta(minutes=window_size)
            window_high_lim = current_time

            # Find the start and end indices of events within the window
            start_index = event_index
            while start_index < len(events) and parse(events[start_index]['timestamp']) <= window_low_lim:
                start_index += 1
            end_index = event_index
            while end_index < len(events) and parse(events[end_index]['timestamp']) < window_high_lim:
                end_index += 1
            
            # Calculate the sum of durations within the window using the prefix sum
            window_sum = prefix_sum[end_index] - prefix_sum[start_index]
            if end_index - start_index == 0:
                average_delivery_times.append({"date": current_time, "average_delivery_time": 0})
            else:
                average_time = window_sum / (end_index - start_index)
                average_delivery_times.append({"date": current_time, "average_delivery_time": average_time})

            current_time += datetime.timedelta(minutes=1)
            event_index = start_index

        return average_delivery_times