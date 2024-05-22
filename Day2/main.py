# Import logo from art.py 
from art import logo

# Print the logo
print(logo)

# Welcome to the user
greeting = "Welcome to the tip calculator!"
print(greeting)

# Total bill information + casting to str to int
total_bill = int(input("What was the total bill? $"))

# Tip request + casting to str to int
total_tip = int(input("How much tip would you like to give? "))

# Number of the person for splitting tip + casting to str to int
num_person = int(input("How many people to split the bill? "))

# Bill per person should pay
result = round((total_bill + total_tip) / num_person, 1)

print(f"Each customer should pay: ${result}")

