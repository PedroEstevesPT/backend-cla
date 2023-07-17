
import datetime
import json
from dateutil.parser import parse
from typing import List, Dict


def round_down_to_minute(timestamp: str) -> datetime.datetime:
    rounded_timestamp = parse(timestamp)
    rounded_timestamp = rounded_timestamp.replace(second=0, microsecond=0)
    return rounded_timestamp

def round_up_to_minute(timestamp: str) -> datetime.datetime:
    res = (parse(timestamp) + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
    return res

def float2string(value: float) -> str:
    return '{:.1f}'.format(value).rstrip('0').rstrip('.')


def parse_events(input_file: str) -> List[Dict[str, str]]:
    with open(input_file, 'r') as file:
        events = [json.loads(line) for line in file]
    return events


def write_output(output_file: str, average_delivery_times: List[Dict[str, float]]) -> None:
    with open(output_file, 'w') as f:
        for i, average_delivery_time in enumerate(average_delivery_times):
            date = average_delivery_time['date']
            avg_delivery_time = average_delivery_time['average_delivery_time']
            line = '{"date": "%s", "average_delivery_time": %s}' % (date, float2string(avg_delivery_time))
            if i != len(average_delivery_times) - 1:
                line += '\n'
            f.write(line)

def print_output(average_delivery_times: List[Dict[str, float]]) -> None:
    for average_delivery_time in average_delivery_times:
        date = average_delivery_time['date']
        avg_delivery_time = average_delivery_time['average_delivery_time']
        print('{"date": "%s", "average_delivery_time": %s}' % (date, float2string(avg_delivery_time)))