

def main():
    print("1 for cm to inches\n2 for inches to cm\n3 for C to F\n4 for F to C\n0 to quit")
    answer = int(input("What would you like to do? "))
    if answer == 0:
        quit()
    elif answer == 1:
        n = float(input("Enter cm to convert to inches: "))
        print(f"inches: {cm_to_inches(n)}")
    elif answer == 2:
        n = float(input("Enter inches to convert to cm: "))
        print(f"cm: {inches_to_cm(n)}")
    elif answer == 3:
        n = float(input("Enter c to convert to f: "))
        print(f"F: {c_to_f(n)}")
    elif answer == 4:
        n = float(input("Enter f to convert to c: "))
        print(f"C: {f_to_c(n)}")





def cm_to_inches(cm):
    return float(cm / 2.54)

def inches_to_cm(inches):
    return float(inches * 2.54)

def c_to_f(c):
    return float((c * 9/5) + 32)

def f_to_c(f):
    return float((f - 32) * 5/9)





if __name__ == "__main__":
    main()