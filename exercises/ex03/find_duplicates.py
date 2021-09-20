"""Finding duplicate letters in a word."""

__author__ = "730247598"

# Variables and Input
word_inp: str = input("Enter a word: ")
index_num: int = 0
j: bool = False

# Output
while index_num < len(word_inp):
    current_letter: str = word_inp[index_num]
    i = index_num + 1

    while i < len(word_inp):
        if current_letter == word_inp[i]:
            j == True
        i += 1

index_num += 1

print("Found duplicate: ", j)
