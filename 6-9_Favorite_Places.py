# Author: Ashley Ramos
# Assignment: 6.9 Favorite Places
# Due: 2/23/2025
# Class: CSC-121-OA1

# Dictionary storing favorite places for three people
favorite_places = {
    'Belen': ['Lauterbrunnen, Switzerland', 'Paris, France', 'Tokyo, Japan'],
    'Glenda': ['Rome, Italy', 'Athens, Greece'],
    'Jose': ['San Jose, Costa Rica', 'Buenos Aires, Argentina']
}

# Looping through the dictionary to print each person's favorite places
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite place(s):")
    for place in places:
        print(f"- {place}")
