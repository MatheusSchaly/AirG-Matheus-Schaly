# AirG-Matheus-Schaly

This README.md guides you through how to execute the scripts created to answer the proposed questions. The written answers can be found at **questions/answers.md**.

# How to set up:

Install Poetry:
```console
pip install poetry
```

Install the project dependencies.:
```console
pip install poetry
```

# How to run the questions:

## Question 1:

To run question 1:
```console
$ make question_1
```

Expected output:
```
Listing the first 5 unique manufacturers:
1: Corellia Mining Corporation
2: Incom Corporation
3: SoroSuub Corporation
4: Sienar Fleet Systems
5: Kuat Drive Yards, Imperial Department of Military Research
```

## Question 2:

1. To get information on the parameters to pass:
```console
$ make question_2_helper
```

Expected output:
```
usage: main.py [-h] [--num_rows NUM_ROWS] [--csv_name CSV_NAME]

Generates a CSV file two columns containing random data. Run example: make question_2 ARGS="--num_rows=10 --csv_name='10_rows.csv'"

optional arguments:
  -h, --help           show this help message and exit
  --num_rows NUM_ROWS  number of rows to generate, default=20
  --csv_name CSV_NAME  CSV filename with the .csv extension, default=20_rows.csv
```

2. To run the script with the default parameters (num_rows=20, csv_name="20_rows.csv"):
```console
$ make question_2
```

Expected output:
```
All tests were successfully completed.
A file containing 20 rows has been created at questions/question_2/data/20_rows.csv.
```

Moreover, a file named **20_rows.csv** containing 20 rows of randomly generated data will be created in the directory **questions/question_2/data/**.

3. To run the script with your own parameters:
```console
# make question_2 ARGS="--num_rows=<your_num_rows> --csv_name=<your_csv_name>"
```

For example:
```
$ make question_2 ARGS="--num_rows=10 --csv_name='10_rows.csv'"
```

Expected output:
```
All tests were successfully completed.
A file containing 10 rows has been created at questions/question_2/data/10_rows.csv.
```

Moreover, a file named **10_rows.csv** containing 10 rows of randomly generated data will be created in the directory **questions/question_2/data/**.

## Question 3:

1. To get information on the parameters to pass:
```console
$ make question_3_helper
```

Expected output:
```
usage: main.py [-h] --input_file INPUT_FILE --output_file OUTPUT_FILE [--delimiter DELIMITER] [--quotechar QUOTECHAR]

Converts pipe-delimited CSV to comma-delimited CSV and surround strings with commas with double quotes. Run example: make question_3 ARGS="--input_file='input_file.csv' --output_file='output_file.csv' --delimiter='|' --quotechar='\"'"

optional arguments:
  -h, --help            show this help message and exit
  --delimiter DELIMITER
                        delimiter to use, default=|
  --quotechar QUOTECHAR
                        quote character to use, default="

required arguments:
  --input_file INPUT_FILE
                        input filename
  --output_file OUTPUT_FILE
                        output filename
```

2. To run the script with so that it tries to detect the delimiter and quotechar:
```console
$ make question_3 ARGS="--input_file=<your_input_file> --output_file=<your_output_file>"
```

For example:
```console
$ make question_3 ARGS="--input_file='input.csv' --output_file='output.csv'"
```

Expected output:
```
Inputs given:
input_file = input.csv
output_file = output.csv
delimiter = None
quotechar = None

As neither delimiter nor quotechar was given, we'll try to detect delimiter and quotechar.
Delimiter detected: e
Quotechar detected: "
```

Moreover, a file named **output.csv** containing the normalized CSV will be created in the directory **questions/question_3/data/**. Notice that the example given by AirG cannot, as expected, be correctly detected by the script.

3. To run the script with defining the quotechar and using the default delimiter (default delimiter=|):
```console
$ make question_3 ARGS="--input_file=<your_input_file> --output_file=<your_output_file> --quotechar=<your_quotechar>"
```

For example:
```console
$ make question_3 ARGS="--input_file='input.csv' --output_file='output.csv' --quotechar='\"'"
```

Expected output:
```
Inputs given:
input_file = input.csv
output_file = output.csv
delimiter = None
quotechar = "

As quotechar was given, we'll use use the default for delimiter: |
```

Moreover, a file named **output.csv** containing the normalized CSV will be created in the directory **questions/question_3/data/**. Notice that the example given by AirG will, as expected, be correctly detected by the script.

4. To run the script with defining the delimiter and using the default quotechar (default quotechar="):
```console
$ make question_3 ARGS="--input_file=<your_input_file> --output_file=<your_output_file> --delimiter=<your_delimiter>"
```

For example:
```console
$ make question_3 ARGS="--input_file='input.csv' --output_file='output.csv' --delimiter='|'"
```

Expected output:
```
Inputs given:
input_file = input.csv
output_file = output.csv
delimiter = |
quotechar = None

As delimiter was given, we'll use use the default for quotechar: "
```

Moreover, a file named **output.csv** containing the normalized CSV will be created in the directory **questions/question_3/data/**. Notice that the example given by AirG will, as expected, be correctly detected by the script.

4. To run the script with your own parameters:
```console
$ make question_3 ARGS="--input_file=<your_input_file> --output_file=<your_output_file> --delimiter=<your_delimiter> --quotechar=<your_quote_char>"
```

For example:
```console
$ make question_3 ARGS="--input_file='input.csv' --output_file='output.csv' --delimiter='|' --quotechar='\"'"
```

Expected output:
```
Inputs given:
input_file = input.csv
output_file = output.csv
delimiter = |
quotechar = "
```

Moreover, a file named **output.csv** containing the normalized CSV will be created in the directory **questions/question_3/data/**. Notice that the example given by AirG will, as expected, be correctly detected by the script.

# How to format the questions folder:

1. To run both pylint and black:

```console
$ make format
```

2. To run only pylint:

```console
$ make pylint
```

3. To run only black:

```console
$ make black
```
