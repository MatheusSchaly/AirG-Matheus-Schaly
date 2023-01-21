"""
This module contains test functions to enrsure that the script that
generates a CSV file with randomly generated data is working as expected.
"""

import csv


def test_column_headers(args):
    """
    Checks that the CSV file has the appropriate column titles.
    """
    with open(
        f"questions/question_2/data/{args.csv_name}", encoding="utf-8"
    ) as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        assert headers == ["random_integer", "random_string"]


def test_number_of_rows(args):
    """
    Checks that the number of rows in the generated CSV
    file matches the number of rows specified in the command line argument.
    """
    with open(
        f"questions/question_2/data/{args.csv_name}", encoding="utf-8"
    ) as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        assert len(rows) == args.num_rows + 1  # +1 to include the header


def test_data_integrity(args):
    """
    Checks that the file has the correct number of columns,
    and that all values in the 'random_integer' column are integers,
    and all values in the 'random_string' column are strings.
    """
    with open(
        f"questions/question_2/data/{args.csv_name}", encoding="utf-8"
    ) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skips the header
        for row in reader:
            assert len(row) == 2
            assert isinstance(int(row[0]), int)
            assert isinstance(row[1], str)
