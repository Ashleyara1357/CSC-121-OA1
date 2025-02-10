# List of animals with a common characteristic
animals = ["eagle", "falcon", "hawk"]

# Printing each animal name
for animal in animals:
    print(animal.title())

# Printing a statement about each animal with correct grammar
for animal in animals:
    article = "An" if animal[0] in "aeiou" else "A"
    print(f"{article} {animal} is an incredible bird of prey.")

# Common characteristic statement
print("\nAll of these animals are powerful birds that soar through the sky!")
