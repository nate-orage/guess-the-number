#!/home/nate/python/python_env/bin/python3
"""Guess the Number"""
import random


def mode_check(list):
    # This defines either easy or hard mode.
    mode = input(
        f"\nHello, {name}!\nWelcome to Guess the Number!! Would you like easy mode or hard mode?\n Easy mode consists of 10 numbers from 1 - 20. You will have 10 attempts.\n Hard mode consists of 20 numbers from 1 - 40. You will have 20 attempts.\n"
    )
    easy = ["easy", "Easy"]
    hard = ["hard", "Hard"]
    if mode in easy:
        list = [random.randint(1, 30) for i in range(10)]
        print(f"\nYou have selected {mode} mode.\n Good luck!!\n")
        return list
    elif mode in hard:
        list = [random.randint(1, 40) for i in range(20)]
        print(f"\nYou have selected {mode} mode.\n Good luck!!\n")
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
    while counter < 11:
        # I decided that the correct number will be in the same position every time. However the list will shuffle each time.
        correct_num = list[-5]
        winner = f"\nYou win! {correct_num} is the correct number!"
        incorrect = f"\nIncorrect. Please try again. You have {10 - counter} attempts remaining.\n"
        lose = "You lose. Goodbye"
        guess = input(
            f"Take a guess!\nYou have a total of {len(list)} numbers to choose from.\n\nYour choices are:\n{list}.\n"
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
            continue
        guess = int(guess)
        if guess is correct_num:
            print(winner)
            break
        if counter == 10:
            print(lose)
            break
        elif guess != correct_num:
            counter += 1
            print(incorrect)


def hard_counter():
    # This function outputs the list of numbers to choose from and tells you how many turns you have left based on a counter.
    global counter
    while counter < 21:
        # I decided that the correct number will be in the same position every time. However the list will shuffle each time.
        correct_num = list[-10]
        print(list)
        print(correct_num)
        winner = f"\nYou win! {correct_num} is the correct number!"
        incorrect = f"\nIncorrect. Please try again. You have {20 - counter} attempts remaining.\n"
        lose = "You lose. Goodbye"
        guess = input(
            f"Take a guess!\nYou have a total of {len(list)} numbers to choose from.\n\nYour choices are:\n{list}.\n"
        )
        try:
            int(guess)
        except ValueError:
            counter += 1
            print(incorrect)
            if counter == 20:
                print(lose)
                break
            continue
        guess = int(guess)
        if guess is correct_num:
            print(winner)
            break
        if counter == 20:
            print(lose)
            break
        elif guess != correct_num:
            counter += 1
            print(incorrect)


name = input(f"\nHello, what" "s your name?\n")
list = mode_check(list)
counter = 0
guess_the_number()
