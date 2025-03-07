# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 8.5 Cities
# Due Date: March 9, 2025

def describe_city(city, country='USA'):
    """Display information about a city and its country."""
    if country.lower() == 'usa':  
        print(f"{city.title()} is in {country.upper()}.")  # Keep 'USA' uppercase
    else:
        print(f"{city.title()} is in {country.title()}.")

# Calling the function for three different cities
describe_city('new york')  # Uses the default country (USA)
describe_city('los angeles')  # Uses the default country (USA)
describe_city('paris', 'france')  # Specifies a different country
