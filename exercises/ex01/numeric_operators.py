"""A program to demonstrate four different operators in Python"""
___author___ = "730247598"

#Input
left_hand_val: int = int(input("Please enter a left hand value" + "\n"))
right_hand_val: int = int(input("Please enter a right hand value" + "\n"))

left_hand_side = str(left_hand_val)
right_hand_side = str(right_hand_val)

total_val = str(left_hand_val ** right_hand_val)

#Output
print("\nLeft-hand side: " + left_hand_side)
print("Right-hand side: " + right_hand_side + "\n")

print(left_hand_side + " ** " + right_hand_side + ": " + total_val)
total_val = str(left_hand_val / right_hand_val)
print(left_hand_side + " / " + right_hand_side + ": " + total_val)
total_val = str(left_hand_val // right_hand_val)
print(left_hand_side + " // " + right_hand_side + ": " + total_val)
total_val = str(left_hand_val % right_hand_val)
print(left_hand_side + " % " + right_hand_side + ": " + total_val)