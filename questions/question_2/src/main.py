"""
This module generates a CSV file with random data. It takes in two command line arguments:
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


def apply_tests(file_path, num_rows):
    """
    Runs test functions on a file.

    Arguments:
    num_rows: Number of rows to generate (int)
    file_path: CSV file path (str)

    Returns:
    None
    """

    test_column_headers(file_path)
    test_number_of_rows(file_path, num_rows)
    test_data_integrity(file_path)
    print("All tests were successfully completed.")


def generate_csv(file_path, num_rows):
    """
    Generates a CSV file with two columns containing random data.

    Arguments:
    num_rows: Number of rows to generate (int)
    file_path: CSV file path (str)

    Returns:
    None
    """

    with open(file_path, "w", newline="", encoding="utf-8") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(["random_integer", "random_string"])  # Header
        for _ in range(num_rows):
            random_integer = random.randint(10000, 99999)
            random_string = "".join(random.choices(string.ascii_letters, k=20))
            csv_writer.writerow([random_integer, random_string])


def parse_arguments():
    """
    Parses command line arguments.

    Arguments:
    None

    Returns:
    None
    """

    default_csv_name = "20_rows.csv"
    default_num_rows = 20

    parser = argparse.ArgumentParser(
        description="""
        Generates a CSV file two columns containing random data.
        
        Run example: make question_2 ARGS="--num_rows=10 --csv_name='10_rows.csv'"
        """
    )
    parser.add_argument(
        "--num_rows", type=int, default=default_num_rows, help=f"number of rows to generate, default={default_num_rows}"
    )
    parser.add_argument(
        "--csv_name",
        type=str,
        default="20_rows.csv",
        help=f"CSV filename with the .csv extension, default={default_csv_name}",
    )
    args = parser.parse_args()

    csv_name = args.csv_name
    num_rows = args.num_rows

    return csv_name, num_rows


if __name__ == "__main__":

    output_csv_name, num_of_rows = parse_arguments()
    data_path = "questions/question_2/data/"
    output_file_path = f"{data_path}{output_csv_name}"
    generate_csv(output_file_path, num_of_rows)
    apply_tests(output_file_path, num_of_rows)

    print(f"A file containing {num_of_rows} rows has been created at {output_file_path}.")
