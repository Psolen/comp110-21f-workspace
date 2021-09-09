"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730247598"

# Initializing Program.
from random import randint

fortune_one: str = ("If winter comes, can spring be far behind?")
fortune_two: str = ("You will become great if you believe in yourself.")
fortune_three: str = ("You cannot love life until you live the life you love.")
fortune_four: str = ("Fortune favors the brave.")

# Output.

r1: int = randint(0, 4)

if r1 == 1:
    print("Your fortune cookie says... ")
    print(fortune_one)
    print("Now, go spread positive vibes!")
else:
    if r1 == 2:
        print("Your fortune cookie says... ")
        print(fortune_two)
        print("Now, go spread positive vibes!")
    else:
        if r1 == 3:
            print("Your fortune cookie says... ")
            print(fortune_three)
            print("Now, go spread positive vibes!")
        else:
            print("Your fortune cookie says... ")
            print(fortune_four)
            print("Now, go spread positive vibes! \n")