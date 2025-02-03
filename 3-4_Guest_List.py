# List of guests I want to invite
guest_list = ["Selena Quintanilla", "Jackie Chan", "Jim Carrey"]

print("Initial Invitations:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to a special dinner event!")

# Informing about the bigger table
print("\nGreat news! We found a bigger dinner table, so we are inviting more guests.\n")

# Adding three more guests
guest_list.insert(0, "Sylvester Stallone")  # Beginning
guest_list.insert(len(guest_list)//2, "Robin Williams")  # Middle
guest_list.append("Zendaya Maree Stoermer Coleman")  # End

# Sorting the guest list alphabetically
guest_list.sort()

# Printing updated invitations
print("Updated Invitations (Sorted List):")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to a special dinner event this afternoon!")