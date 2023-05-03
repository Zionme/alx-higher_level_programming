#!/usr/bin/python3
"""
Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(total_size, status_codes):
    """Print accumulated metrics.
    Args:
        total_size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            try:
                fields = line.split()
                if len(fields) < 7:
                    raise ValueError("Invalid input format")
                size = int(fields[-1])
                code = fields[-2]
                if code not in valid_codes:
                    raise ValueError("Invalid status code")
                total_size += size
                status_codes[code] = status_codes.get(code, 0) + 1
            except ValueError as e:
                print("Error processing line {}: {}".format(line_count, str(e)), file=sys.stderr)

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

