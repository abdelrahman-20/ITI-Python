"""
------------------------------------------------
Rules:
    1. Every user input must be validated.
       - If invalid, print error and ask again until valid.
    2. Each task must be implemented in a separate .py file.
       - Each file must contain a function that executes the task.
    3. A main.py file must import all task modules.
    4. When main.py runs:
         - Display a menu showing all tasks with their number & name.
         - Let the user select which task to execute by entering the task number.
         - Run only the selected task.
    5. Use if __name__ == "__main__": script only run in main.py`.
    6. Use functions and avoid code duplication.
    7. Add comments explaining each step.
    8. Automate as much as possible (e.g., file creation, processing).
    9. No hardcoding results.
    10. Decorators (Task 7) must be applied to at least two tasks.
------------------------------------------------

Tasks:

1) Math Automation
   - Create a file called "math_report.txt".
   - Ask the user for multiple numbers (comma-separated).
   - For each number, calculate:
        - floor, ceil, square root, area of a circle
   - Write the results into "math_report.txt".
   - Confirm file was created and print its content.

2) Regex Log Cleaner
   - Create a file called "access.log" with 10 fake log lines
     (mix valid emails and invalid strings).
   - Use regex to extract all valid emails.
   - Save them into "valid_emails.txt".
   - Print how many unique emails were found.

3) Datetime Reminder Script
   - Ask user for a date (YYYY-MM-DD).
   - Calculate how many days remain until that date.
   - If it is in the past, print "This date has already passed."
   - Otherwise, save the reminder into "reminders.txt" in format:
        "{date} -> {days_left} days left"
   - Append multiple reminders without overwriting.

4) Product Data Transformer (lambda, map, filter, zip)
   - Ask user for a list of product names (comma-separated).
   - Ask user for a list of product prices (comma-separated).
   - Process them by:
        - Pairing product with price.
        - Filtering out items where price <= 0.
        - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
   - Save the final result as JSON into "products.json".
   - Print a preview of the first 5 results.

5) OS File Manager
   - Ask user for a directory path.
   - Automatically:
        - Create a folder "backup" inside it if not exists.
        - Copy all .txt files into "backup".
        - Print summary: how many files copied.
   - If directory invalid, retry until correct.

6) Random Data Generator
   - Ask user how many random numbers to generate.
   - Save them into "random_numbers.csv" as:
        index,value
        1, 42
        2, 87
        ...
   - Print total count and average of the generated numbers.

7) Decorators Task
   - Create a decorator called "log_time" that:
        - Records the execution time of any function.
        - Saves the function name and runtime into "execution_log.txt".
   - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
   - Verify that the log file contains entries after running.
"""

from math_automation import math_automation
from regex_log_cleaner import regex_log_cleaner
from date_time_reminder import datetime_reminder
from product_data_transformer import product_data_transformer
from os_file_manager import os_file_manager
from random_data_generator import random_data_generator


def main():
    userInput = ""
    while userInput != "0" and userInput.strip().lower() != "quit":
        print("Enter The Task Number To Execute It:")
        print("1) Math Automation")
        print("2) Regex Log Cleaner")
        print("3) Date Time Reminder")
        print("4) Product Data Transformer")
        print("5) OS File Manager")
        print("6) Random Data Generator")
        print("0 or quit To Exit")

        userInput = input("Task Number: ")
        if userInput == "1":
            math_automation()
        elif userInput == "2":
            regex_log_cleaner()
        elif userInput == "3":
            datetime_reminder()
        elif userInput == "4":
            product_data_transformer()
        elif userInput == "5":
            os_file_manager()
        elif userInput == "6":
            random_data_generator()
        elif userInput == "0" or userInput.strip().lower() == "quit":
            print("Exiting...")
        else:
            print("Invalid input. Please try again.")


main()
