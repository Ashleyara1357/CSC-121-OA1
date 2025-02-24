# Author: Ashley Ramos
# Assignment: 6.5 Rivers
# Due: 2/23/2025
# Class: CSC-121-OA1

# Dictionary of rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Loop to print only the names of the rivers
print("\nThe following rivers are included in the dictionary:")
for river in rivers.keys():
    print(river.title())

# Loop to print only the names of the countries
print("\nThe following countries are included in the dictionary:")
for country in rivers.values():
    print(country.title())
