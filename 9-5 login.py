# Author: Ashley Ramos
# Class: CSC-121-OA1
# Assignment: 9-5 Login
# Due Date: March 23, 2025

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, location):
        """Initialize the user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0  # Added attribute for login attempts

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Prints a personalized greeting."""
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increments the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts to 0."""
        self.login_attempts = 0


# Create an instance of the User class
user = User('Ashley', 'Ramos', 25, 'Old Fort')

# Call increment_login_attempts() multiple times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the number of login attempts
print(f"\nLogin attempts: {user.login_attempts}")

# Reset login attempts and print again
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
