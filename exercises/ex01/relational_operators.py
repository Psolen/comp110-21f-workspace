"""A program to relate two integers with Python operators"""
___author___ = "730247598"

#Input
left_hand_val: int = int(input("Please enter a left hand value" + "\n"))
right_hand_val: int = int(input("Please enter a right hand value" + "\n"))

left_hand_side = str(left_hand_val)
right_hand_side = str(right_hand_val)

bool_val: bool = left_hand_val < right_hand_val

#Output
print("\nLeft-hand side: " + left_hand_side)
print("Right-hand side: " + right_hand_side + "\n")

print(left_hand_side + " < " + right_hand_side + " is ")
print(bool_val)

bool_val = left_hand_val >= right_hand_val

print(left_hand_side + " >= " + right_hand_side + ": ")
print(bool_val)

bool_val = left_hand_val == right_hand_val

print(left_hand_side + " == " + right_hand_side + ": ")
print(bool_val)

bool_val = left_hand_val != right_hand_val

print(left_hand_side + " != " + right_hand_side + ": ")
print(bool_val)
