#!/home/nate/python/python_env/bin/python3
"""Guess the Number"""
import random
from os import system, name


def mode_check(list):
    # This defines either easy or hard mode.
    mode = input(
        f"\nHello, {name}!\nWelcome to Guess the Number!! Would you like easy mode or hard mode?\n Easy mode consists of 10 numbers from 1 - 20. You will have 10 attempts.\n Hard mode consists of 20 numbers from 1 - 40. You will have 20 attempts.\n"
    )
    easy = ["easy", "Easy"]
    hard = ["hard", "Hard"]
    mode_choice = f"\nYou have selected {mode} mode.\n Good luck, {name}!!\n"
    # Generate list for Easy Mode
    if mode in easy:
        list = [random.randint(1, 30) for i in range(10)]
        print(mode_choice)
        return list
    # Generate list for Hard Mode
    elif mode in hard:
        list = [random.randint(1, 40) for i in range(20)]
        print(mode_choice)
        return list
    else:
        return mode_check(list)


def guess_the_number():
    # Determines which function to choose next by examining the length of the list that is created.
    if len(list) == 10:
        easy_counter()
    else:
        hard_counter()


def easy_counter():
    # This function outputs the list of numbers to choose from and tells you how many turns you have left based on a counter.
    global counter
    # This chooses the winning number based on a random selection of an index position.
    correct_num = list[(random.randint(0, 9))]
    clear()
    while counter < 11:
        winner = f"\nYou win! {correct_num} is the correct number!"
        incorrect = f"\nIncorrect. Please try again. You have {10 - counter} attempts remaining.\n"
        lose = "You lose. Goodbye"
        guess = input(
            f"Take a guess!\nYou have a total of {len(list)} numbers to choose from.\n\nYour choices are:\n{list}\n"
        )
        try:
            # This verifies that the input is a whole number and not a float or str.
            int(guess)
        except ValueError:
            counter += 1
            print(incorrect)
            if counter == 10:
                print(lose)
                break
            # continue
        guess = int(guess)
        if guess is correct_num:
            print(winner)
            break
        if counter == 10:
            clear()
            print(lose)
            break
        elif guess != correct_num:
            clear()
            counter += 1
            print(incorrect)


def hard_counter():
    # This function outputs the list of numbers to choose from and tells you how many turns you have left based on a counter.
    global counter
    # This chooses the winning number based on a random selection of an index position.
    correct_num = list[(random.randint(0, 19))]
    clear()
    while counter < 21:
        winner = f"\nYou win! {correct_num} is the correct number!"
        incorrect = f"\nIncorrect. Please try again. You have {20 - counter} attempts remaining.\n"
        lose = "You lose. Goodbye"
        guess = input(
            f"Take a guess!\nYou have a total of {len(list)} numbers to choose from.\n\nYour choices are:\n{list}\n"
        )
        try:
            int(guess)
        except ValueError:
            counter += 1
            print(incorrect)
            if counter == 20:
                print(lose)
                break
        guess = int(guess)
        if guess is correct_num:
            print(winner)
            break
        if counter == 20:
            clear()
            print(lose)
            break
        elif guess != correct_num:
            clear()
            counter += 1
            print(incorrect)


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


name = input(f"\nHello, what" "s your name?\n")
counter = 0
list = mode_check(list)
guess_the_number()
