#!/usr/bin/python3
"""
    This script processes log lines from standard input,
    extracts relevant information
        (IP, timestamp, request, status code, response size),
    calculates statistics on status codes and total file size,
"""
import sys
import re
import typing


def print_result(size: int, status_dict: dict):
    """
    Prints the calculated file size and status code counts.

    Args:
        size: The total file size.
        status_dict: A dictionary containing status code counts.
    """
    print(f"File size: {size}")
    for key, value in sorted(status_dict.items()):
        print(f"{key}: {value}")

if __name__ == '__main__':
    counter: int = 0
    total_size: int = 0
    value: int = 0
    matches: list = []
    status: dict = {}
    pattern: str = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] \"GET /projects/\d+ HTTP/1\.1\" \d{3} \d+"""

    # read from stdin
    try:
        for line in sys.stdin:
            matches = re.findall(pattern, line)
            if matches:
                stat, size = re.findall(r"\d{3} \d+", line)[0].split(' ')
                total_size += int(size)
                if status.get(stat) is None:
                    value = 1
                else:
                    value += 1
                status[stat] = value

            if counter == 10:
                print_result(total_size, status)
                counter = 0
            counter += 1

    except KeyboardInterrupt:
        print_result(total_size, status)
        raise
