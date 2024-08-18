#!/usr/bin/python3 
"""
This script processes log lines from standard input, extracts relevant information (IP, timestamp, request, status code, response size),
calculates statistics on status codes and total file size, and prints the results every 9 lines or upon receiving an interrupt signal.
"""
import sys 
import re
import signal
from typing import List


pattern: str = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] \"GET /projects/\d+ HTTP/1\.1\" \d{3} \d+"
status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

count = 0
file_size = 0

def print_result(size, status_dict):
    """
    Prints the calculated file size and status code counts.

    Args:
        size: The total file size.
        status_dict: A dictionary containing status code counts.
    """
    print(f"File size: {size}")
    for key, value in status_dict.items():
        print(f"{key}: {value}")

def signal_handler(signal, frame):
    """
    Handles the SIGINT signal (Ctrl+C) by printing results and exiting.
    """
    print_result(file_size, status)
    sys.exit(0)

for line in sys.stdin:
    if count == 9:
        print_result(file_size, status)
        count = 0

    matches: List = re.findall(pattern, line)
    if matches:
        stat, size = re.findall(r"\d{3} \d+", line)[0].split(' ')
        size = int(size)
        appear = status.get(stat)
        appear += 1
        status.update({stat: appear})
        file_size += size
    count += 1
    signal.signal(signal.SIGINT, signal_handler)
