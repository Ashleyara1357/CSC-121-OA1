# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 8-14 Cars
# Due Date: March 9, 2025

def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    # Create a new dictionary to avoid modifying the input
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    # Add the additional key-value pairs
    car.update(car_info)
    return car

car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)  # Prints the first car dictionary

# Calling the function with a different car brand/model
car2 = make_car('honda', 'civic', color='red', sunroof=True)
print(car2)  # Prints the second car dictionary
