"""List utility functions."""

__author__ = "730247598"


# TODO: Implement your functions here.
def all(int_list: list[int], i: int) -> bool:
    j: int = 0
    while j < len(int_list):
        if int_list[j] != i:
            return False
        j += 1
    return True


print(all([1, 2, 3], 1))
print(all([1, 1, 1], 2))
print(all([1, 1, 1], 1))


def is_equal(int_list_one: list[int], int_list_two: list[int]) -> bool:
    k: int = 0
    while k < len(int_list_one):
        if int_list_one[k] != int_list_two[k]:
            return False
        k += 1
    return True


print(is_equal([1, 0, 1], [1, 0, 1]))
print(is_equal([1, 1, 0], [1, 0, 1]))


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    p = 0
    max_num: int = 0
    while p < len(input):
        if input[p] > max_num:
            max_num = input[p]
        p += 1
    return max_num


print(max([1, 3, 2]))
print(max([100, 99, 98]))
print(max([]))