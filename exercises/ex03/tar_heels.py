"""An exercise in remainders and boolean logic."""

__author__ = "730247598"

# Input
num_hold: int = int(input("Enter am int: "))

# Output

if num_hold % 2 == 0:

    if num_hold % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if num_hold % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")
