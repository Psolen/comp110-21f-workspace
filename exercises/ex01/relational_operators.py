"""A program to relate two integers with Python operators."""
__author__: str = "730247598"

# Input
left_hand_val: int = int(input("Please enter a left hand value" + "\n"))
right_hand_val: int = int(input("Please enter a right hand value" + "\n"))

left_hand_side = str(left_hand_val)
right_hand_side = str(right_hand_val)

# Output
print("Left-hand side: " + left_hand_side)
print("Right-hand side: " + right_hand_side)

bool_val: bool = left_hand_val < right_hand_val
print(left_hand_side + " < " + right_hand_side + " is {}".format(bool_val))

bool_val = left_hand_val >= right_hand_val
print(left_hand_side + " >= " + right_hand_side + " is {}".format(bool_val))

bool_val = left_hand_val == right_hand_val
print(left_hand_side + " == " + right_hand_side + " is {}".format(bool_val))

bool_val = left_hand_val != right_hand_val
print(left_hand_side + " != " + right_hand_side + " is {}".format(bool_val))
