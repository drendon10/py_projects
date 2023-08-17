# A todo list app

import sys

todo = []

while True:
    print("TODO: ")
    for index, thing in enumerate(todo, start=1):
        print(f"{index}. {thing}")

    try:
        move = int(input("Enter 1 to add something to do, 2 to mark something as complete, or 3 to quit: "))
    except ValueError:
        sys.exit("Enter a number")

    if move == 1:
        todo.append(input("Enter todo: "))
    elif move == 2:
        n = int(input("What number on the list would you like to mark as complete? "))
        todo[n - 1] = todo[n - 1] + " #"
    elif move == 3:
        sys.exit()

