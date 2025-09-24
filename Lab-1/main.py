import re


# write a program that prints hello world
def hello(name):
    if len(name) == 0 or not isinstance(name, str):
        print("Hello, World!")
    else:
        print(f"Hello, {name}")


userInput = input("Enter your name: ")
hello(userInput)


# -------------------------------------------------------------------------
# application to take a number in binary form from the user, and print it as a decimal
def binaryToDecimal(x: str):
    if not isinstance(x, str) or len(x) == 0 or any(c not in "01" for c in x):
        return "Invalid Input"
    for c in list(x):
        if c not in ["0", "1"]:
            return "Invalid Input"
    return int(x, 2)


userInput = input("Enter a Binary Number: ")
print(binaryToDecimal(userInput))

# print(binaryToDecimal("111"))
# print(binaryToDecimal("11011"))


# -------------------------------------------------------------------------
# write a function that takes a number as an argument and if the number
# 	divisible b "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 	divisible by both return "FizzBuzz"
def fizzBuzz(x):
    if len(x) == 0 or not isinstance(x, int) or isinstance(x, float):
        return "Invalid Input, You Must Enter Decimal Number !!"

    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


userInput = input("Enter A Number For FizzBuzz Function: ")
print(fizzBuzz(userInput))

# print(fizzBuzz(6))
# print(fizzBuzz(10))
# print(fizzBuzz(15))


# -------------------------------------------------------------------------
# Ask the user to enter the radius of a circle print its calculated area and circumference
def getCircleRadius(radius):
    if len(radius) == 0 or isinstance(radius, float) or isinstance(radius, int):
        radius = float(radius)
        area = 3.14 * radius**2
        circumference = 2 * 3.14 * radius
        return f"Area: {area}, Circumference: {circumference}"
    else:
        return "Invalid Radius !!"


radius = input("Enter The Radius of The Circle: ")
circle = getCircleRadius(radius)
print(circle)


# -------------------------------------------------------------------------
# Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data


def getUserInfo(name, email):
    if len(name) == 0 or name.isdigit() or not isinstance(name, str):
        return "Invalid Name. Please Enter a Valid Name !!"

    # Advanced E-Mail Validation:
    if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
        return "Invalid Email"

    # Basic E-Mail Validation:
    # for c in list(email):
    #     if c == "@":
    #         break
    # else:
    #     return "Invalid Email"
    return f"Name: {name}, Email: {email}"


name = input("Enter Your Name: ")
email = input("Enter Your Email: ")
user_info = getUserInfo(name, email)
print(user_info)


# -------------------------------------------------------------------------
# Write a program that prints the number of times the substring 'iti' occurs in a string
def countSubString(string: str, substring: str) -> int:
    return string.count(substring)


print(countSubString("I Like ITI, ITI is a great place to learn.", "ITI"))
# -------------------------------------------------------------------------
