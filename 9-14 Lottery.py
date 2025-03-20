# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 9-14 Lottery
# Due Date: March 23, 2025

import random

# Create a list of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 numbers and 1 letter
winning_combination = random.sample(lottery_pool, 4) + [random.choice(['A', 'B', 'C', 'D', 'E'])]
random.shuffle(winning_combination)  # Shuffle for randomness

# Convert to a string for easy comparison
winning_combination_str = ''.join(map(str, winning_combination))

# Get user input for their lottery guess
user_guess = input("Enter your lottery guess (4 numbers and 1 letter): ")

# Compare user's guess to the winning combination
if user_guess == winning_combination_str:
    print("🎉 Congratulations! You won the lottery!")
else:
    print(f"❌ Sorry, you lost. The winning combination was: {winning_combination_str}")
