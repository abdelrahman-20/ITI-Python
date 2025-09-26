# 6) Random Data Generator
#    - Ask user how many random numbers to generate.
#    - Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - Print total count and average of the generated numbers.

import csv
import random


def random_data_generator():
    while True:
        try:
            count = int(input("How Many Random Numbers to Generate? "))
            if count <= 0:
                print("Enter a Valid Positive Integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please Enter a Valid Positive Number.")

    # random numbers between 1 and 100
    numbers = [random.randint(1, 100) for _ in range(count)]

    # Save to CSV
    with open("random_numbers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["index", "value"])
        for i, num in enumerate(numbers, start=1):
            writer.writerow([i, num])

    total_count = len(numbers)
    average_value = sum(numbers) / total_count if total_count > 0 else 0

    print(f"Generated {total_count} Numbers.")
    print(f"Average Value: {average_value:.3f}")


if __name__ == "__main__":
    random_data_generator()
# random_data_generator()
