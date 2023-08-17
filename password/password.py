master_pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Accound name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")
        



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add, q): ")
    if mode =='q':
        break
    if mode == 'view':
        pass
    elif mode == 'add':
        pass
    else:
        print('Invalid mode')
        continue