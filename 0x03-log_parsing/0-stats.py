#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics.
"""

import sys


def print_stats(file_size, st_codes):
    """
    Print the accumulated metrics.
    """
    print("File size: {}".format(file_size))
    for code in sorted(st_codes.keys()):
        if st_codes[code] > 0:
            print("{}: {}".format(code, st_codes[code]))


def main():
    """
    Main function to process the input and compute metrics.
    """
    file_size = 0
    st_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split(" ")

            # Validate and extract information
            if len(parts) >= 9:
                try:
                    file_size += int(parts[-1])
                    status_code = int(parts[-2])
                    if status_code in st_codes:
                        st_codes[status_code] += 1
                except ValueError:
                    continue

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(file_size, st_codes)

    except KeyboardInterrupt:
        print_stats(file_size, st_codes)
        raise

    # Final stats
    print_stats(file_size, st_codes)


if __name__ == "__main__":
    main()
