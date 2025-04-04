# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 10-4 Guest Book
# Due Date: April 6, 2025
# This program prompts users for their name, greets them and records their visit in guest_book.txt

filename = 'guest_book.txt'

print("Welcome to the Guest Book!")
print("Enter 'q' when you're done.\n")

while True:
    name = input("Enter your name (or 'q' to quit): ")

    if name.lower() == 'q':
        break

    print(f"Welcome, {name}!")

    with open(filename, 'a') as file:
        file.write(f"{name} visited.\n")

    print("Your visit has been recorded.\n")

print("Thank you for signing the guest book!")
