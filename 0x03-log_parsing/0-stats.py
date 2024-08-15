#!/usr/bin/python3
"""
Log parsing
"""
import sys
import signal
import re


total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

log_pattern = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')


def print_stats():
    """
    print the current statistics
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
                
except Exception as e:
    sys.stderr.write(f"Error: {e}\n")

print_stats()
