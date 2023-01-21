# AirG-Matheus-Schaly

# How to set up:

Install Poetry:
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
The first 5 unique manufacturers are: ['Corellia Mining Corporation', 'Incom Corporation', 'SoroSuub Corporation', 'Sienar Fleet Systems', 'Kuat Drive Yards, Imperial Department of Military Research']
```

## Question 2:

1. To get information on the parameters to pass:
```console
$ make question_2_helper
```

Expected output:
```
usage: main.py [-h] num_rows csv_name

Generates a CSV file two columns containing random data.

positional arguments:
  num_rows    Number of rows to generate.
  csv_name    CSV filename with the .csv extension.

optional arguments:
  -h, --help  show this help message and exit
```

2. To run the script with the default parameters (num_rows=20, csv_name="20_rows.csv"):
```console
$ make question_2
```

Expected output:
```
All tests were successfully completed
```

Moreover, a file named "20_rows.csv" will be created in the directory "questions/question_2/data/". The data inside the file will be randomly generated, but here's an example of what it could look like:
```
random_integer,random_string
39280,WFGlhPNJngMibyrDrdHm
37129,bFgDLsObCNzRHHwvwqMA
88573,iVISBdjWScYcAfmBZFIf
75435,kQLETbEgmMKLRObfXuZQ
31491,MnuoMDdTHrgGzjVOktpq
26279,RDEfTYFOFHnLSdQMrWGR
80062,lRPrrMZpenlUXenwItNa
56904,KSSmQtnZpxruoiKFasEC
59128,ZiAJQpbWyjHnUoHZTjKV
61843,IbYskfVqpgctIIcXJYyL
22118,MHMfuEMdCJkDMsrgYCTO
80714,HVIUuFbaCuSvMFyNWzEw
76349,jdQFQkDJEbpEupgGqMGQ
48486,bDEiRxMmxZatfaxNJfJm
25897,JhwFqOmwOVNAmTtnLUVg
15879,pagdkVUHsJlPTUDFFvtS
17963,lfWhALBDHVvifurojpoI
52915,sazdDebwmmgrahBZWoyo
17752,zOUsjIndFEYqKHMoNgnE
48874,DCdGaFEUxWqYrbFMtTAC
```

3. To run the script with your own parameters:
```console
$ make question_2 num_rows=<your_num_rows> csv_name=<your_csv_name>
```

For example:
```
$ make question_2 num_rows=10 csv_name="10_rows.csv"
```

Expected output:
```
All tests were successfully completed
```

Moreover, a file named "10_rows.csv" will be created in the directory "questions/question_2/data/". The data inside the file will be randomly generated, but here's an example of what it could look like:
```
random_integer,random_string
54539,nKsfgtFNwIJnfuWXhKwQ
87035,NAgkrwelDRIqNdvdtRid
49818,KXrCbYkzDdtbdKGweHbU
71765,YXYxOYnytSYeGBoRNjqv
83481,iGGsSqQTgHklfzfcZIbS
70115,fOGAPrwXAOgADnnsMMhv
15840,jzKbSxgfgxwIBJAjUoxw
75390,nBCvmEbQXBdFZDgsEVSV
99188,kdMHDoZbGmxenCtzerDA
93166,fweHHTuudaCtPEAkxFYO
```

## How to format the questions folder:

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
