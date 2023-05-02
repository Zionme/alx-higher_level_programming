#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        fields = line.split()
        if len(fields) >= 7:
            try:
                status = int(fields[6])
                if status in status_codes:
                    status_count[status] += 1
            except ValueError:
                pass
            try:
                size = int(fields[8])
                total_size += size
            except (ValueError, IndexError):
                pass
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes):
                if status_count[code] > 0:
                    print("{}: {}".format(code, status_count[code]))
except KeyboardInterrupt:
    pass

print("File size: {}".format(total_size))
for code in sorted(status_codes):
    if status_count[code] > 0:
        print("{}: {}".format(code, status_count[code]))
