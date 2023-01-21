INCLUDE_FILES = ./questions
num_rows ?= 20
csv_name ?= 20_rows.csv

question_1:
	poetry run python -m questions.question_1.main

question_2:
	poetry run python -m questions.question_2.src.main $(num_rows) $(csv_name)

question_2_helper:
	poetry run python -m questions.question_2.src.main --help

pylint:
	poetry run pylint ${INCLUDE_FILES} --disable=import-error --fail-under=0.0

black:
	poetry run black ${INCLUDE_FILES}

format:
	make pylint
	make black
