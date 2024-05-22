# Import logo from art.py 
from art import logo

# Print the logo
print(logo)

# Welcome the user
greeting = "Welcome to the Band Name Generator."
print(greeting)

# Take input from user the name of city they grew up in and print it
user_city = input("What's is the name of city you grew in? ").upper()
print(user_city)

# Take input from user the name of their pet's name and print it
user_pet_name = input("What is your pet's name? ").upper()
print(user_pet_name)

# Combine the city name and pet name to generate a band name
band_name = f"Your band name could be {user_city} {user_pet_name}"
print(band_name)