import os
import random
from statistics import mean, median, mode

# Constants
START = 1
STOP = 100

# Colors
os.system("")
CG = "\033[0m\033[32m"
CW = "\033[0m\033[37m"
CR = "\033[0m\033[31m"
CB = "\033[0m\033[34m"
CV = "\033[0m\033[35m"
CC = "\033[0m\033[36m"
CY = "\033[0m\033[33m"

# Styles
ST = "\033[0m"
BOLD = "\033[1m"
EM = "\033[3m"

# Emojis
WIN = "\U0001F3C6"
MEDAL = "\U0001F947"
UP = "\U00002B06"
DOWN = "\U00002B07"


print(f"{CG}" + r"""
           ⢀⣤⣾⣿⣿⣿⣿⣿⣷⣤⡀
        ⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
     ⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿         ⣠⣤⣴⣦⣄
 ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟       ⣴⣿⣿⣿⣿⣿⣿⣿⣦      ___ _   _ ___ ___ ___
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁       ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷    / __| | | | __/ __/ __|
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠛⠛⠛⠛⠉⠁        ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   | (_ | |_| | _|\__ \__ \
⣿⣿⣿⣿⣿⣿⣿⣿⣿                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    \___|\___/|___|___/___/
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣠⣾⣿⡿⠋          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   |_   _| || | __|
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋             ⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿     | | | __ | _|
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋      ⣤⣶⣶    ⢀⣤    ⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿    _|_| |_||_|___|__ ___ ___ ___
⣿⣿⣿⣿⣿⣿⣿⣿⣿     ⣰⣿⣿⣿⠇   ⣾⣿⣿⣿     ⠙⣿⣿⣿⣿⣿⣿⣿⣿   | \| | | | |  \/  | _ ) __| _ \
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣾⣿⣿⣿⡿   ⢰⣿⣿⣿⣿⣆    ⢀⣿⣿⣿⣿⣿⣿⣿⣿   | .` | |_| | |\/| | _ \ _||   /
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉    ⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿   |_|\_|\___/|_|  |_|___/___|_|_\
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋
  ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀   ⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋
     ⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁
         ⠈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁
             ⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉
                 ⠉⠛⠿⠿⠛⠉
""" + "\n")


def start_game():
    num = random.randint(START, STOP)
    guesses = 0
    high_score = 0
    tries = []
    while True:
        guesses += 1
        guess = get_guess()
        if guess < num:
            print(f"{CV}{UP} It's higher.")
        elif guess > num:
            print(f"{CC}{DOWN} It's lower.")
        else:
            print(f"{CG}\n{WIN} You guessed it in {guesses} tries! {ST}{WIN}")
            tries.append(guesses)
            handle_stats(tries)
            replay = handle_replay()
            if replay:
                if high_score == 0 or guesses < high_score:
                    high_score = guesses
                num = random.randint(START, STOP)
                guesses = 0
                print(f"\n{CY}HIGH SCORE: {BOLD}{high_score}{ST} {MEDAL}")
            else:
                print("\nThanks for playing!")
                break


def get_guess():
    while True:
        try:
            guess = int(input(
                f"{CW}Guess a whole number between {START} and {STOP}:{ST} "))
            if guess < START or guess > STOP:
                print(handle_errors(guess))
            else:
                return guess
        except ValueError as err:
            print(handle_errors(err))


def handle_replay():
    while True:
        replay = input("Play again? (y/n) ")
        if replay.lower() == "y":
            return True
        elif replay.lower() == "n":
            return False
        else:
            print(handle_errors(replay))


def handle_errors(err):
    err_msg = f"{CR}{EM}{err} is not a valid option. Please try again.{ST}"
    return err_msg.replace("invalid literal for int() with base 10: ", "")


def handle_stats(tries):
    print("\n\n₪₪₪ Overall Statistics ₪₪₪")
    print(f"Mean: {CB}{BOLD}{mean(tries):.2f}{ST}")
    print(f"Median: {CV}{BOLD}{median(tries)}{ST}")
    print(f"Mode: {CC}{BOLD}{mode(tries)}{ST}\n\n")


start_game()
