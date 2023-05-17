import random
# Add text color support for Windows Command Prompt and PowerShell
import os
os.system("")

START = 1
STOP = 100
ERROR = f"\033[31m\033[3mNot a valid guess. Please enter a whole number between {START} and {STOP}.\033[0m"

num = random.randint(START, STOP)

print(
    "\033[32m"
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
    while True:
        guesses += 1
        try:
            guess = int(input(
                f"\033[37m\033[40mGuess a whole number between {START} and {STOP}:\033[0m "))
        except ValueError:
            print(ERROR)
        else:
            if guess < START or guess > STOP:
                print(ERROR)
            elif guess < num:
                print("\033[35mToo low, try again.")
            elif guess > num:
                print("\033[36mToo high, try again.")
            else:
                print(
                    f"\033[32m\n\U0001F3C6 You guessed it in {guesses} tries!\033[0m \U0001F3C6")
                replay = input("Play again? (y/n) ")
                if replay.lower() == "y":
                    if high_score == 0 or guesses < high_score:
                        high_score = guesses
                    num = random.randint(START, STOP)
                    guesses = 0
                    print(f"\n\033[33mHIGH SCORE: {high_score} \U0001F947")
                    continue
                else:
                    print("\nThanks for playing!")
                    break


start_game(num)
