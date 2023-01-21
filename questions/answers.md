The Information about how to run the questions' code and their expected output can be found in the **README.md** file.

# Question 1:
The script for question 1 can be found at **questions/question_1/main.py**.

# Question 2:
The script for question 2 can be found at **questions/question_2/src/main.py**.

**Question:**

If you had to generate a large number of rows (millions or more), is there anything you would do differently to handle this?

**Answer:**

Instead of storing all the rows in memory before writing to the CSV file, I'd use a technique called **streaming**. This involves writing the rows to the file as they are generated, thus saving memory and preventing the script from crashing due to lack of memory.

This is the part of the code that implements this technique:
```python
for _ in range(args.num_rows):
    random_integer = random.randint(10000, 99999)
    random_string = "".join(random.choices(string.ascii_letters, k=20))
    csv_writer.writerow([random_integer, random_string])
```

**Question:**

If this script had to run in a production environment, what tests would you include to ensure it's running correctly?

**Answer:**

The tests can be found at **questions/question_2/tests/tests.py**. I can run the tests one by one like I do in **questions/question_2/src/main.py**, or I could use a test runner like **unittest** to run all the test functions automatically. Additionally, I could include test cases to check the following:

1. Verify that the script can handle large number of rows.
2. Verify that the script can handle edge cases and handle them gracefully.
3. Verify that the script is writing the correct data to the CSV file.
4. Verify that the script is generating random values for each row.

**Question:**

If you were having this code reviewed, what else would you do with your code to ensure the code is clean and well-formatted?

**Answer:**

To make the code easy to read and understand, I would:
- Use clear names for variables and functions.
- Keep the indentation and naming style consistent throughout the code.
- Add explanations to the code to show how it works.
- Divide the code into smaller parts.
- Handle any errors that may occur in the code.
- Check if the code works as it should.
- Add information about the code and its functions.
- Remove any unnecessary code.
- Use proper capitalization and punctuation.
- Format the code using a tool to meet standards;
- Put all the library imports at the beginning of the code;
- Make sure the code is easy to read and follows good practices.

Moreover, when submitting a pull request, I'd do the following:
1. Pull from the main branch to ensure that my branch is up-to-date with the latest changes.
2. Create a new branch for my changes, which would keep them separate from the main branch until they are ready to be merged.
3. Group my changes into logical and self-contained commits, each with a clear and concise message that describes the changes made.
4. Rebase my branch to ensure that it is up-to-date with the main branch and that any conflicts have been resolved.
5. Push the branch to the remote repository.
6. Write a clear and concise description of the changes made and the reasoning behind them.
7. Request reviews from other team members.
8. Make any necessary adjustments based on feedback.
9. Merge the branch into the main branch once the code has been reviewed and approved.
Pull request steps may vary by company.
