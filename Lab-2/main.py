"""
Python Practice Tasks
=====================

Rules:
    - Everything must be written inside functions.
    - The file should run as a script.
    - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
    - The user chooses a number, and the program runs the corresponding function.
    - Each task should only run when chosen from the menu.
    - At ANY stage: if the user enters invalid input, the program must:
          * Show an error message
          * Display what valid input looks like
          * Let the user try again (do not crash or exit)
"""


# 1- Ask the user to enter 5 numbers.
#   Store them, then display them in ascending order and descending order.
def task_1():
    numbers = []
    while len(numbers) < 5:
        try:
            num = float(input(f"Enter number {len(numbers) + 1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid Input. Please Enter a Valid Number. (Ex: 3, 4.5, -2) : ")

    print("Ascending order:", sorted(numbers))
    print("Descending order:", sorted(numbers, reverse=True))


# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.
def task_2():
    while True:
        try:
            length = input("Enter How Many Numbers (Ex: 5 , 10 , ...) : ")
            start = input("Enter Starting Number (Ex: 1 , 10 , ...) : ")
            length = int(length)
            start = int(start)

            if length <= 0:
                print("Length must be a positive integer.")
                continue

            numbers = [start + i for i in range(length)]
            print("Generated Numbers: ", numbers)
            break
        except ValueError:
            print(
                "Invalid Input. Enter Valid Integers for Length and Start. (Ex: 5 , 10 , ...)"
            )
            continue


# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.
def task_3():
    total = 0
    count = 0

    while True:
        userInput = input("Enter a Number or Type (done) To Exit: ")
        if userInput.lower().strip() == "done":
            break
        try:
            number = float(userInput)
            total += number
            count += 1

        except ValueError:
            print("Invalid Input. You Must Enter a Positive Number. (Ex: 3, 4.5)")
            continue

    if count > 0:
        average = total / count
        print(f"The Total: {total}, Numbers Count: {count}, The Average: {average}")
    else:
        print("You Did Not Enter Any Valid Numbers.")


# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.
def task_4():
    while True:
        userInput = input("Enter Numbers Separated By Spaces: (Ex: 3 4.5 -2 3): ")
        try:
            numbers = [float(num.strip()) for num in userInput.split()]
            result = sorted(set(numbers))
            print(f"The Sorted Result: {result}")
            break

        except ValueError:
            print("Enter Valid Numbers Separated By Spaces !!")
            continue


# 5 - Ask the user to enter a sentence.
#     Count how many times each word appears in the sentence
#     and display the result.
def task_5():
    while True:
        userInput = input("Enter A Sentence: ")
        words = userInput.split()
        words_count = {}

        if len(words) == 0:
            print("You Must Enter A Valid Sentence !!")
            continue

        for word in words:
            # Remove Any Puctuation
            word = word.lower().strip(".,!?;:\"'()[]{}")
            if word:
                words_count[word] = words_count.get(word, 0) + 1
        print("Words Count:")
        for wrd, cnt in words_count.items():
            print(f"{wrd}: {cnt}")


# 6 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.
def task_6():
    students = {}
    while len(students) < 5:
        name = input(f"Enter The Name of Student No.{len(students)+1} :")
        if len(name) <= 3:
            print("Enter A Valid Name !!")
            continue
        while True:
            try:
                score = float(input(f"Enter Score For {name}: ").strip())
                if score < 0:
                    print("Score Can't Be Negative, Try Again !")
                    continue
                students[name] = score
                break
            except ValueError:
                print("Invalid Score, Try Again !")
                continue
    if students:
        scores = list(students.values())
        lowest_score = min(scores)
        highest_score = max(scores)
        average_score = sum(scores) / len(scores)

        print(f"Lowest Score: {lowest_score}")
        print(f"Highest Score: {highest_score}")
        print(f"Average Score: {average_score}")
    else:
        print("No Students Data Entered.")


# 7 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.
def task_7():
    print("\n--------------------------------------------------")
    print(" Welcome To Shopping Center ".center(50, "-"))

    total_cost = 0
    shopping_cart = {}

    while True:
        print("\n1. Add Item\n2. Remove Item\n3. View Cart\n4. Checkout and Exit")
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            item_name = input("Enter Item Name: ").strip().lower()
            if len(item_name) == 0:
                print("Item Name Can't Be Empty !")
                continue

            while True:
                try:
                    item_price = float(input("Enter Item Price: ").strip())
                    if item_price <= 0:
                        print("Price Can't Be Zero or Negative, Try Again !")
                        continue
                    shopping_cart[item_name] = item_price
                    total_cost += item_price

                    print("\n--------------------------------------------------")
                    print(f"{item_name} Added to Cart.")
                    print(f"Current Total: ${total_cost:.2f}")
                    print("--------------------------------------------------\n")
                    break

                except ValueError:
                    print("\n--------------------------------------------------")
                    print("Invalid Price, Try Again !")
                    print("--------------------------------------------------\n")
                    continue

        elif choice == "2":
            item_name = input("Enter Item Name to Remove: ").strip().lower()

            if item_name in shopping_cart:
                total_cost -= shopping_cart[item_name]
                del shopping_cart[item_name]
                print("\n--------------------------------------------------")
                print(f"{item_name} Removed from Cart.")
                print(f"Current Total: ${total_cost:.2f}")
                print("--------------------------------------------------\n")

            else:
                print("\n--------------------------------------------------")
                print(f"{item_name} not found in Cart.")
                print("--------------------------------------------------\n")

        elif choice == "3":
            if shopping_cart:
                print("\n--------------------------------------------------")
                print("Items in Cart: ")
                for item, price in shopping_cart.items():
                    print(f"{item}: ${price:.2f}")
                print(f"Total Cost: ${total_cost:.2f}")
                print("--------------------------------------------------\n")
            else:
                print("\n--------------------------------------------------")
                print("Your Cart is Empty !")
                print("--------------------------------------------------\n")

        elif choice == "4":
            print("\n--------------------------------------------------")
            print(f"Total Cost: ${total_cost:.2f}".center(50, "-"))
            print(" Thank You for Shopping ".center(50, "-"))
            print("--------------------------------------------------\n")
            break

        else:
            print("\n--------------------------------------------------")
            print("Invalid Choice. Please Select a Valid Option (1-4).")
            print("--------------------------------------------------\n")


# 8 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts.
def task_8():
    import random

    randomNum = random.randint(1, 20)
    attempts = 0

    print("\n--------------------------------------------------")
    print(" Welcome To Number Guessing Game ".center(50, "-"))
    print("Guess a number between 1 and 20".center(50))
    print("--------------------------------------------------\n")

    while True:
        userInput = input("Enter Your Guess (or type 'exit' to quit): ").strip().lower()

        if len(userInput) == 0:
            print("You Must Enter A Valid Input (1, 2, ... , 20) or 'exit' to quit !")
            continue

        if userInput == "exit":
            print("\n--------------------------------------------------")
            print(f" The Number Was: {randomNum} ")
            print(f" Total Attempts: {attempts} ".center(50))
            print(" Thank You for Playing ! ".center(50))
            print("--------------------------------------------------\n")
            break

        try:
            guess = int(userInput)
            attempts += 1
            if guess < 1 or guess > 20:
                print("The Number Must Be Between 1 and 20. Try Again !")
                continue

            if guess < randomNum:
                print("Too Low! Try Again.")
            elif guess > randomNum:
                print("Too High! Try Again.")
            else:
                print("\n--------------------------------------------------")
                print(
                    f"Well Done! You Got The Number {randomNum} in {attempts} attempts.".center(
                        50
                    )
                )
                print("--------------------------------------------------\n")
                break

        except ValueError:
            print("Invalid Input. Please Enter a Valid Integer Between 1 and 20.")
            continue


# The Main Function To Run The Application
def main():
    while True:
        print("\n===============================")
        print(" Python Practice Tasks Menu ")
        print("===============================\n")

        print("1. List Order")
        print("2. Generate Number Sequence")
        print("3. Number Statistics")
        print("4. Remove Duplicates and Sort")
        print("5. Word Count in Sentence")
        print("6. Gradebook System")
        print("7. Shopping Cart Simulator")
        print("8. Number Guessing Game")
        print("9. Exit\n")

        choice = input("Choose a task (1-9): ").strip()

        if choice == "1":
            task_1()
        elif choice == "2":
            task_2()
        elif choice == "3":
            task_3()
        elif choice == "4":
            task_4()
        elif choice == "5":
            task_5()
        elif choice == "6":
            task_6()
        elif choice == "7":
            task_7()
        elif choice == "8":
            task_8()
        elif choice == "9":
            print("Exiting the program ...")
            break
        else:
            print("Invalid Choice. Please Select a Valid Option (1-9).")


if __name__ == "__main__":
    main()
