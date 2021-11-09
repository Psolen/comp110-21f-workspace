"""Finding duplicate letters in a word."""

__author__ = "730247598"

# Variables and Input
word_inp: str = input("Enter a word: ")
dup: bool = False
i: int = 0

# Output
while i < len(word_inp):
    j: int = i + 1
    char: str = word_inp[0]
    while j < len(word_inp):
        if word_inp[i] == word_inp[j]:
            dup = True
        j += 1
    i += 1

print("Found duplicate: " + str(dup))
