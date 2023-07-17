import datetime
from collections import deque
from dateutil.parser import parse
from typing import List, Dict
from utils import round_down_to_minute, round_up_to_minute
from algorithms.moving_average_calculator import MovingAverageCalculator

class DequeAverageDeliveryTimeCalculator(MovingAverageCalculator):
    
    def calculate_average(self, events: List[Dict[str, str]], window_size: int) -> List[Dict[str, float]]:
        average_delivery_times = []
        window = deque()
        total_duration = 0

        if len(events) < 1:
            raise ValueError("There must be at least 1 event for the moving average to be calculated.")

        start_time = round_down_to_minute(events[0]['timestamp'])
        end_time = round_up_to_minute(events[-1]['timestamp'])
        
        current_time = start_time
        event_index = 0

        while current_time <= end_time:
            window_low_lim = current_time - datetime.timedelta(minutes=window_size)
            window_high_lim = current_time

            # Remove events from the window that are outside the current window range
            while window and parse(window[0]['timestamp']) <= window_low_lim:
                removed_event = window.popleft()
                total_duration -= removed_event['duration']

            # Find the end index of events within the window
            end_index = event_index
            while end_index < len(events) and parse(events[end_index]['timestamp']) < window_high_lim:
                event = events[end_index]
                window.append(event)
                total_duration = total_duration + event['duration']
                end_index += 1

            # Calculate the average delivery time for the current window
            if window_size == 0 or len(window) == 0:
                average_delivery_times.append({"date": current_time, "average_delivery_time": 0})
            else:
                average_time = total_duration / len(window)
                average_delivery_times.append({"date": current_time, "average_delivery_time": average_time})

            current_time += datetime.timedelta(minutes=1)
            event_index = end_index

        return average_delivery_times