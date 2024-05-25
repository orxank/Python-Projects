# Import ASCII art logo
from art import logo

# Print logo
print(logo)

# Welcome the user and inform game aim
print("Welcome to Treasure Island\nYour mission is to find the treasure.")

# Game Code
user_first_step = input("You are at a cross road. You've two choices(\"left\" and \"right\"): ").lower()

if user_first_step == "left":
    print("Well done")
    user_second_step = input("swim or wait: ").lower()
    if user_second_step == "wait":
        print("Great")
        user_third_input = input("Choose the door. red, blue, or yellow: ")
        if user_third_input == "red":
            print("Game Over.\nYou burned by fire.")
        elif user_third_input == "blue":
            print("Game Over.\nEaten by beasts.")
        elif user_third_input == "yellow":
            print("You Win!")
        else:
            print("game Over.")
    else:
        print("Game Over.\nAttacked by trout.")
else:
    print("Game Over.\nYou fall into a hole.")
