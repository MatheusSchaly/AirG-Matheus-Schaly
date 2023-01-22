INCLUDE_FILES = ./questions

install:
	poetry install

question_1:
	poetry run python -m questions.question_1.main

question_2:
	poetry run python -m questions.question_2.src.main $(ARGS)

question_2_helper:
	poetry run python -m questions.question_2.src.main --help

question_3:
	poetry run python -m questions.question_3.src.main $(ARGS)

question_3_helper:
	poetry run python -m questions.question_3.src.main --help

pylint:
	poetry run pylint $(INCLUDE_FILES) --disable=import-error --fail-under=0.0 --max-line-length=120

black:
	poetry run black $(INCLUDE_FILES)

format:
	make pylint
	make black
