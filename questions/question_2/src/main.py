"""
This module generates a CSV file with random data.
It takes in two command line arguments:
The number of rows to generate, and the CSV filename.
"""

import argparse
import csv
import random
import string

from questions.question_2.tests.tests import (
    test_number_of_rows,
    test_column_headers,
    test_data_integrity,
)


if __name__ == "__main__":
    # Parses command line arguments
    parser = argparse.ArgumentParser(
        description="Generates a CSV file two columns containing random data."
    )
    parser.add_argument(
        "num_rows", type=int, default=20, help="Number of rows to generate."
    )
    parser.add_argument(
        "csv_name",
        type=str,
        default="20_rows",
        help="CSV filename with the .csv extension.",
    )
    args = parser.parse_args()

    # Writes the rows into a CSV file
    with open(
        f"questions/question_2/data/{args.csv_name}", "w", newline="", encoding="utf-8"
    ) as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["random_integer", "random_string"])  # Header
        for _ in range(args.num_rows):
            random_integer = random.randint(10000, 99999)
            random_string = "".join(random.choices(string.ascii_letters, k=20))
            csv_writer.writerow([random_integer, random_string])

    test_column_headers(args)
    test_number_of_rows(args)
    test_data_integrity(args)

    print("All tests were successfully completed")
