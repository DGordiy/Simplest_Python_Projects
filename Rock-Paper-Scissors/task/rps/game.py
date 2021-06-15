import random


def grade_user_choice():
    computer_choice = random.choice(VARIANTS)

    # if result = 0 it is DRAW
    # if result = -1 it is USER WON
    # if result = 1 it is COMPUTER WON
    if computer_choice == user_choice:
        print("There is a draw ({})".format(computer_choice))
        grade = 50
    else:
        new_list = VARIANTS[VARIANTS.index(user_choice) + 1:] + VARIANTS[: VARIANTS.index(user_choice)]
        index_slice = int(len(new_list) / 2)
        if computer_choice in new_list[:index_slice]:
            print("Sorry, but the computer chose {}".format(computer_choice))
            grade = 0
        else:
            print("Well done. The computer chose {} and failed".format(computer_choice))
            grade = 100

    return grade


def get_variants():
    variants = input().strip()
    if variants == '':
        return ['rock', 'paper', 'scissors']
    else:
        return variants.split(',')


user_name = input("Enter your name: ")
print("Hello,", user_name)

rating = 0

# read rating value
f = open("rating.txt", "r")
for r in f:
    data = r.split()
    if data[0] == user_name:
        rating = int(data[1])
f.close()

VARIANTS = get_variants()

# start the game
print("Okay, let's start")
user_choice = input()
while user_choice != '!exit':
    if user_choice in VARIANTS:
        rating += grade_user_choice()
    elif user_choice == '!rating':
        print("Your rating:", rating)
    else:
        print("Invalid input!")
    user_choice = input()

print("Bye!")
