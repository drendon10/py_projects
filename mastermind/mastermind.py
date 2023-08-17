# Mastermind game

import random

# Constant variables
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

# Function that generates code for the game
def genereate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code
# Function that allows user to guess the code
def guess_code():
    while True:
        # Creates a list with all the colors the user chose
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue # Makes you guess again

        # Check if color is in the colors available
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        # This will init the color if it's not already in the dictionary setting it = 0 then incrementing after to avoid errors
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # Zip takes both arguments and turns them into tuples then creates a new list with both tuples in it
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            # Get rid of color from the count to make sure I don't count it when dealing with incorrect pos
            color_counts[guess_color] -= 1
        
    for guess_color, real_color in zip(guess, real_code):
        # Asking if the color exists in the color_counts dict and if it's greater than zero
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to Mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)
    code = genereate_code()
    for attempts in range(1, TRIES + 1): # Goes from 1 to 11 not inlcuding 11 so basically 10
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
        print(f"You have {TRIES - attempts} left")
        
    else:
        print("You ran out of tries, the code was: ", *code)    # '*' unpacks the list and prints it without commas


if __name__ == "__main__":
    game()



