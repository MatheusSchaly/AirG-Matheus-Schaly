"""
This module converts a pipe-delimited CSV file to a comma-delimited
CSV file and surrounds strings with commas in them with double quotes.
"""

import csv
import argparse


def detect_delimiter_quotechar(data_path, input_file):
    """
    Tries to automatically detect the delimiter and quote character.

    Arguments:
    None

    Returns:
    None
    """

    with open(f"{data_path}{input_file}", "r", encoding="utf-8") as f_input:
        try:
            dialect = csv.Sniffer().sniff(f_input.readline())
            delimiter, quotechar = dialect.delimiter, dialect.quotechar
        except FileNotFoundError as exc:
            raise ValueError("The input file could not be found, please check the file path and name.") from exc
        except csv.Error as exc:
            raise ValueError("The input file is malformed and the script cannot proceed.") from exc

    return delimiter, quotechar


def parse_arguments(data_path):
    """
    Retrieve command line arguments for input/output file names, delimiter, and quotechar
    """

    default_delimiter = "|"
    default_quotechar = '"'

    parser = argparse.ArgumentParser(
        description="""
        Converts pipe-delimited CSV to comma-delimited CSV and surround strings with commas with double quotes.

        Run example: make question_3 ARGS="--input_file='input_file.csv' --output_file='output_file.csv' --delimiter='|' --quotechar='\\"'\"
        """
    )
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument("--input_file", required=True, type=str, help="input filename")
    required_args.add_argument("--output_file", required=True, type=str, help="output filename")
    parser.add_argument("--delimiter", type=str, help=f"delimiter to use, default={default_delimiter}")
    parser.add_argument("--quotechar", type=str, help=f"quote character to use, default={default_quotechar}")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    delimiter = args.delimiter
    quotechar = args.quotechar

    print("Inputs given:")
    print(f"input_file = {input_file}\noutput_file = {output_file}\ndelimiter = {delimiter}\nquotechar = {quotechar}\n")

    if not delimiter and not quotechar:
        print("As neither delimiter nor quotechar was given, we'll try to detect delimiter and quotechar.")
        delimiter, quotechar = detect_delimiter_quotechar(data_path, input_file)
        print(f"Delimiter detected: {delimiter}\nQuotechar detected: {quotechar}")
    else:
        if delimiter is None:
            print(f"As quotechar was given, we'll use use the default for delimiter: {default_delimiter}\n")
            delimiter = default_delimiter
        if quotechar is None:
            print(f"As delimiter was given, we'll use use the default for quotechar: {default_quotechar}\n")
            quotechar = default_quotechar

    return input_file, output_file, delimiter, quotechar


def normalize_csv():
    """
    Convert pipe-delimited CSV to comma-delimited CSV and surround strings with commas with double quotes.
    """

    data_path = "questions/question_3/data/"
    input_file, output_file, delimiter, quotechar = parse_arguments(data_path)
    input_file_path = f"{data_path}{input_file}"
    output_file_path = f"{data_path}{output_file}"

    with open(input_file_path, "r", encoding="utf-8") as f_input:
        with open(output_file_path, "w", newline="", encoding="utf-8") as f_output:
            input_csv = csv.reader(f_input, delimiter=delimiter)
            output_csv = csv.writer(f_output, delimiter=",", quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
            for row in input_csv:
                output_csv.writerow(row)


if __name__ == "__main__":

    normalize_csv()
