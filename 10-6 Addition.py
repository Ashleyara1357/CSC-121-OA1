# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 10-6 Addition
# Due Date: April 6, 2025
# This program prompts the user for two numbers,adds them together, and handles any input errors.

print("Enter two numbers and I'll add them together.")
print("Enter 'q' at any time to quit.\n")

while True:
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Oops! Please enter valid numbers only.\n")
    else:
        print(f"The sum of {num1} and {num2} is {result}.\n")
