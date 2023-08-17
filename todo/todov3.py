# Command line argument to do list

import sys

path = "todo.txt"

if len(sys.argv) == 1:
    with open(path) as file:
        print("TODO: ")
        print()
        lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            print(f"{index}. {line}".strip())
    sys.exit()



if len(sys.argv) != 3:
    sys.exit("Usage: python3 todov3.py (mode: a/r) (thing to add/remove)")


mode = sys.argv[1]
todo = sys.argv[2]
if mode == 'r':
    todo = int(todo)

with open(path, 'r+') as file:
    lines = file.readlines()
    if mode == 'a':
        file.write(f"{todo}\n")
    elif mode == 'r':
        lines.pop(todo - 1)
    
    with open(path, 'w') as file:
        file.writelines(lines)

with open(path, 'r') as file:
    lines = file.readlines()
    print("TODO: ")
    print()
    for index, line in enumerate(lines, start=1):
        print(f"{index}. {line}".strip())

