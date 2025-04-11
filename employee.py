# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 11-3 Employee
# Due Date: April 13, 2025

# This class represents an employee and includes a method to give a raise.
class Employee:
    """Represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a raise to the annual salary."""
        self.annual_salary += amount
