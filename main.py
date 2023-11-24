# IMPORT ALL LIBRARIES
import argparse
import random

# INSTANTIATE PARSER & ADD ARGS
parser = argparse.ArgumentParser(prog="THE EASTER EGG GAME", description="A game where you find different easter eggs and add them to the catalog.", epilog="THIS IS A PRE-RELEASE GAME, LOTS OF UPDATES ARE EXPECTED!! Type \"therealgame\" in the guess spot to get more info.")

parser.add_argument("guess", help="your guess to find an easter egg")
parser.add_argument("--value", "-v", required=False, help="some easter eggs require a value, not all")

args = parser.parse_args()

# PROCESS ARGS
__guess = args.guess
guess = __guess.lower()

__value = None
value = None

if args.value != None:
    __value = args.value
    value = __value.lower()

# FUNCTIONS
def update():
    # COMING SOON #
    pass

def catalog(full):
    fs = open("HISTORY", "a")
    fs.write(full[0] + " - " + full[1] + "\n")
    fs.close()

def run():
    if guess == "therealgame":
        if value == None:
            print("TO LEARN MORE ABOUT THE GAME, TYPE THESE IN THE VALUE OPTION:")
            print("1. \"pre\" - Learn more about the updates upcoming to the game")
        elif value == "pre":
            print("This game is still in pre-release. We are coming up ways to update the game everytime we find a new easter egg.")
            print("This game is open-source and all updates will be on the GitHub page.")
        else:
            print("Huh... I have no idea what that means.")
    elif guess == "42":
        print("The answer to life, the universe, and everything. Yeah, we already knew it.")
        catalog(["42", "The answer to life, the universe, and everything."])
    elif guess == "yay":
        print("MY FAVORITE WORD EVER!! - M. West (Creator)")
        catalog(["YAY", "MY FAVORITE WORD EVER!!"])
    elif guess == "yes":
        temp = 0
        while (temp < 30000):
            print("y")
            temp = temp + 1
        print("Seriously, why does Linux do this?")
        catalog(["YES", "Seriously, why does Linux do this?"])
    elif guess == "googlein1998":
        print("Hey! That's a Google easter egg... and hopefully not copyright.")
        catalog(["GOOGLE IN 1998", "Hey! That's a Google easter egg... and hopefully not copyright."])
    elif guess == "up up down down left right left right b a start":
        print("Does anyone even know which game that came from?")
        catalog(["UPDOWN", "Does anyone even know which game that came from?"])
    else:
        temp = random.randint(0, 5)

        if temp == 0:
            print("Nope.")
        elif temp == 1:
            print("Nada.")
        elif temp == 2:
            print("Yeah... no.")
        elif temp == 3:
            print("Uhhhhhhhh... that's wrong.")
        elif temp == 4:
            print("This isn't the game for you.")
        elif temp == 5:
            print("No, just no.")

run()