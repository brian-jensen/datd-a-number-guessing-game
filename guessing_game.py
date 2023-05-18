from statistics import mean, median, mode

import random
# Add text color support for Windows Command Prompt and PowerShell
import os
os.system("")

START = 1
STOP = 100

# Colors
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

ERROR = f"""{CR}{EM}
Not a valid guess. Please enter a whole number between {START} and {STOP}.{ST}
""".strip()


num = random.randint(START, STOP)

print(
    f"{CG}"
    + r"""
           ⢀⣤⣾⣿⣿⣿⣿⣿⣷⣤⡀
        ⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
     ⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿         ⣠⣤⣴⣦⣄        ____ _   _ _____ ____ ____
 ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟       ⣴⣿⣿⣿⣿⣿⣿⣿⣦    / ___| | | | ____/ ___/ ___/
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁       ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷  | |  _| | | |  _| \___ \___ \
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠛⠛⠛⠛⠉⠁        ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  | |_| | |_| | |___ ___) |__) |
⣿⣿⣿⣿⣿⣿⣿⣿⣿                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   \____|\___/|_____|____/____/
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣠⣾⣿⡿⠋          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  |_   _| | | | ____|
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋             ⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    | | | |_| |  _|
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋      ⣤⣶⣶    ⢀⣤    ⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿    | | |  _  | |___
⣿⣿⣿⣿⣿⣿⣿⣿⣿     ⣰⣿⣿⣿⠇   ⣾⣿⣿⣿     ⠙⣿⣿⣿⣿⣿⣿⣿⣿   _|_|_|_| |_|_____| ____  _____ ____
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣾⣿⣿⣿⡿   ⢰⣿⣿⣿⣿⣆    ⢀⣿⣿⣿⣿⣿⣿⣿⣿  | \ | | | | |  \/  | __ )| ____|  _ \
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉    ⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿  |  \| | | | | |\/| |  _ \|  _| | |_) |
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋  | |\  | |_| | |  | | |_) | |___|  _ <
  ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀   ⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋    |_| \_|\___/|_|  |_|____/|_____|_| \_\
     ⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁
         ⠈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁
             ⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉
                 ⠉⠛⠿⠿⠛⠉
"""
    + "\n"
)


def start_game(num):
    guesses = 0
    high_score = 0
    tries = []
    while True:
        guesses += 1
        try:
            guess = int(input(
                f"{CW}Guess a whole number between {START} and {STOP}:{ST} "))
        except ValueError:
            print(ERROR)
        else:
            if guess < START or guess > STOP:
                print(ERROR)
            elif guess < num:
                print(f"{CV}Too low, try again.")
            elif guess > num:
                print(f"{CC}Too high, try again.")
            else:
                print(
                    f"{CG}\n{WIN} You guessed it in {guesses} tries! {ST}{WIN}"
                )
                tries.append(guesses)
                print("\n\n₪₪₪ Overall Statistics ₪₪₪")
                print(f"Mean: {CB}{BOLD}{mean(tries)}{ST}")
                print(f"Median: {CV}{BOLD}{median(tries)}{ST}")
                print(f"Mode: {CC}{BOLD}{mode(tries)}{ST}\n\n")
                replay = input("Play again? (y/n) ")
                if replay.lower() == "y":
                    if high_score == 0 or guesses < high_score:
                        high_score = guesses
                    num = random.randint(START, STOP)
                    guesses = 0
                    print(f"\n{CY}HIGH SCORE: {BOLD}{high_score}{ST} {MEDAL}")
                    continue
                else:
                    print("\nThanks for playing!")
                    break


start_game(num)
