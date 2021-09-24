"""Examples of using lists in a simple game."""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove the 1 from the list
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum of values of the rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")