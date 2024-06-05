from library import word_list
import random
from stages import *
from art import *

print(logo)


chosen_word = random.choice(word_list)

lives = 6
display = []
word_length = len(chosen_word)
for _ in chosen_word:
    display += "_"


should_continue = False

while not should_continue:
    guess = input('Guess a letter: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        should_continue = True
        print("You win!")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            should_continue = True
            print("You lose!")
    
    print(stages[lives])

