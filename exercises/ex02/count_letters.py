"""Counting letters in a string."""

__author__ = "730247598"

# Input.

search_letter: str = input("What letter do you want to search for?: ")
word_search: str = input("Enter a word: ")
count: int = 0
i = 0

# Output

while i < len(word_search):

    if word_search[i] == search_letter:
        count = count + 1
        i = i + 1
    else:
        i = i + 1

print("Count: " + str(count)) 