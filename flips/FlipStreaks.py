import random


def main():
    number = int(input("Number: "))
    streak_count = count_streak(number)
    print(f'There was {streak_count} streaks of 6 total')
    
def count_streak(n):
    
    streak_count = 0
    current_streak = 0
    flips = []

    for _ in range(n):
        flips.append(random.randint(0, 1))

    for i in range(len(flips)):
        if i == 0:
            pass
        elif flips[i] == flips[i-1]:
            current_streak += 1
        else:
            current_streak = 0
        
        if current_streak == 6:
            streak_count += 1
            current_streak = 0

    print(flips)
    return streak_count

        









if __name__ == "__main__":
    main()