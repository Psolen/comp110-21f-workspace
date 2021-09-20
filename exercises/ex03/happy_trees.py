"""Drawing forests in a loop."""

__author__ = "730247598"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
i: int = 1

while i < (depth + 1):
    print(TREE * i)
    i += 1