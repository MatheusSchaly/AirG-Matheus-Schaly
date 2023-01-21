# AirG-Matheus-Schaly

## How to set up:

1. Install Poetry:

```console
pip install poetry
```

## How to run the questions:

1. To run question 1:

```console
$ make question_1
```

The expected output is:

```
The first 5 unique manufacturers are: ['Corellia Mining Corporation', 'Incom Corporation', 'SoroSuub Corporation', 'Sienar Fleet Systems', 'Kuat Drive Yards, Imperial Department of Military Research']
```

2. To run question 2:

To get information on which parameters to pass:

```console
$ make question_2_helper
```

To run with the default parameters, that is, num_rows=20, csv_name="20_rows.csv":

```console
$ make question_2
```

To run by passing your own parameters:

```console
$ make question_2 num_rows=<your_num_rows> csv_name=<your_csv_name>
```
