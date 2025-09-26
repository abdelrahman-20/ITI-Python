# 1) Math Automation
#    - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.

from math import floor, ceil, sqrt, pi
from decorators_task import log_time


@log_time
def math_automation():
    while True:
        # Get User Input
        input_data = input("Enter Multiple Numbers (Comma-Separated): ")
        try:
            if len(input_data.strip()) == 0:
                print("Empty Input, Enter Numbers Separated by Commas (,)")
                continue

            numbers = [float(num.strip()) for num in input_data.split(",")]

            with open("math_report.txt", "w") as file:
                file.write(
                    "Number,\t\tFloor,\t\tCeil,\t\tSqr.Root,\tCircle Area\n"
                    + "*" * 75
                    + "\n"
                )
                for num in numbers:
                    ceil_val = ceil(num)
                    floor_val = floor(num)
                    sqrt_val = sqrt(num) if num >= 0 else "N/A"
                    area_circle = pi * (num**2) if num >= 0 else "N/A"

                    file.write(
                        f"{num:.2f},\t\t{floor_val:.2f},\t\t{ceil_val:.2f},\t\t{sqrt_val:.2f},\t\t{area_circle:.2f}\n"
                    )
                file.write("*" * 75 + "\n")
            file.close()

            # Displaying the content of the report
            print("math_report.txt Created Successfully.")
            with open("math_report.txt", "r") as file:
                content = file.read()
                print("Content of math_report.txt:")
                print(content)
                file.close()
            break

        except ValueError:
            print("Invalid Input. You Should Enter Numbers Separated by Commas (,)")
            continue


if __name__ == "__main__":
    math_automation()
