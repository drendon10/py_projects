import sys

path = "todo.txt"
while True:
    print("TODO: ")
    with open(path, "r+") as file:
        lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            print(f"{index}. {line}".strip())

        try:
            move = int(input("\n1 to add something to do, 2 to mark something as complete, 3 to remove all completed things, 4 to quit: "))
        except ValueError:
            sys.exit("Enter a number")

        
        if move == 1:
            text = input("Enter todo: ")
            file.write(f"{text}\n")
            
        elif move == 2:
            n = int(input("What number on the list would you like to mark as complete? "))
            lines[n - 1] = f"{lines[n-1][:-1]} #\n"
            with open(path, "w") as file:
                for line in lines:
                    file.write(line)

        elif move == 3:
            new_lines = [line for line in lines if not line.strip().endswith("#")]
            with open(path, "w") as file:
                for line in new_lines:
                    file.write(line)
        elif move == 4:
            sys.exit()

