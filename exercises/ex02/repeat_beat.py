"""Repeating a beat in a loop."""

__author__ = "730247598"

# Input
beat_word: str = input("What beat do you want to repeat? ")
beat_bounce: int = int(input("How many times do you want to repeat it? "))
beat_print: str = beat_word
i: int = 0

# Output
if beat_bounce > 0:
    while i < (beat_bounce - 1):
        beat_print = beat_print + (" " + beat_word)
        i = i + 1

    print(beat_print)
else:
    print("No beat...")
