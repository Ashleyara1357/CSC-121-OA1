# Author: Ashley Ramos
# Class: CSC-121-OA1
# Due Date: 3/2/2025
# Assignment: 7-8. Deli Sandwiches

# List of sandwich orders
sandwich_orders = ["tuna", "ham and cheese", "chicken", "veggie", "turkey"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Remove the first sandwich from the list
    print(f"I made your {current_sandwich} sandwich.")  # Print message
    finished_sandwiches.append(current_sandwich)  # Move it to finished sandwiches list

# Print final message listing all sandwiches made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.capitalize()} sandwich")
