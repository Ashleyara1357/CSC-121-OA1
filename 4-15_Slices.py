# 4-10 Slices
# List of guests I want to invite

guest_list = ["Selena Quintanilla", "Jackie Chan", "Jim Carrey"]

print("Initial Invitations:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to a special dinner event!")

# Informing about the bigger table
print(
    "\nGreat news! We found a bigger dinner table, "
    "so we are inviting more guests.\n"
)

# Adding three more guests
guest_list.insert(0, "Sylvester Stallone")  # Beginning
guest_list.insert(len(guest_list) // 2, "Robin Williams")  # Middle
guest_list.append("Zendaya Maree Stoermer Coleman")  # End

# Sorting the guest list alphabetically
guest_list.sort()

# Printing updated invitations
print("Updated Invitations (Sorted List):")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to a special dinner event!")

# Slices Task - Printing specific parts of the list
print("\nThe first three items in the list are:")
print(guest_list[:3])  # Prints first three guests

print("\nThree items from the middle of the list are:")
middle_index = len(guest_list) // 2
print(guest_list[middle_index - 1:middle_index + 2])  # Prints three guests

print("\nThe last three items in the list are:")
print(guest_list[-3:])  # Prints last three guests
