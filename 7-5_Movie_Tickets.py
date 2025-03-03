# Author: Ashley Ramos
# Class: CSC-121-OA1
# Due Date: 3/2/2025
# Assignment: 7.5 Movie Tickets

# Initialize total cost
total_cost = 0

# Prompt user for number of tickets
num_tickets = int(input("How many movie tickets do you need? "))

# Loop to get ages and calculate ticket prices
for ticket in range(num_tickets):
    age = int(input(f"Enter the age of ticket holder {ticket + 1}: "))

    # Determine ticket price based on age
    if age < 3:
        price = 0  # Free for under 3
    elif 3 <= age <= 12:
        price = 10  # $10 for ages 3-12
    else:
        price = 15  # $15 for 13 and above

    total_cost += price

# Display the total cost
print(f"\nThe total cost for {num_tickets} ticket(s) is: ${total_cost}")
