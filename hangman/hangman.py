import sys
import random

path = 'words.txt'
# Open file, read file, and choose random word from file
with open(path, 'r') as file:
    words = file.readlines()
word = random.choice(words)[:-1]

# init variables
guesses = []
run = True
errors_left = 10


while run:
    # Prints underscore if letter hasn't been guessed and prints letter if it has been guessed
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    # Get letter guess from user and add it to the list of guesses
    guess = input(f"{errors_left} errors left. Next guess: ")
    guesses.append(guess.lower())

    # Calculate if letter is in word
    if guess.lower() not in word.lower():
        errors_left -= 1
        if errors_left == 0:
            break
    run = False
    for letter in word:
        if letter.lower() not in guesses:
            run = True
if not run:
    print(f"You won, word was {word}")
else:
    print(f"Game over, word was {word}")
            
            
