import random
from art import * # import ASCII text (rock, paper, scissors)



choices_list = [rock, paper, scissors]

# Ask from user to choose the one option(rock paper, or scissors)
player_choice = input("Hey, Player! What do you choose? (rock, paper, scissors): ").lower()
# Execute randomly computer choice
computer_choice = random.choice(choices_list)


if player_choice not in ['rock', 'paper', 'scissors']:
    print("Please choose valid option for playing game.")
else:
    print("Your Choice: ")
    print(choices_list[['rock', 'paper', 'scissors'].index(player_choice)])
    print("Computer's choice:")
    print(computer_choice)

    # Conditional coding part for choosing the game winner
    if player_choice == 'rock':
        if computer_choice == rock:
            print("It's a tie!")
        elif computer_choice == scissors:
            print("You win! Rock smashes scissors.")
        else:
            print("You lose! Paper covers rock.")
    if player_choice == 'paper':
        if computer_choice == paper:
            print("It's a tie!")
        elif computer_choice == rock:
            print("You win! Paper covers rock.")
        else:
            print("You lose! Scissors cut paper.")
    if player_choice == 'scissors':
        if computer_choice == scissors:
            print("It's a tie!")
        elif computer_choice == rock:
            print("You lose! Rock smashes scissors.")
        else:
            print("You win! Scissors cut paper.")








