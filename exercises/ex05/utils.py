"""List utility functions part 2."""

__author__ = "730247598"

# Define your functions below


def only_evens(int_list: list[int]) -> list[int]:
    """This a function to find and return even integers in a list of ints."""
    even_list: list[int] = []
    i: int = 0
    while i < len(int_list):
        if int_list[i] % 2 == 0:
            even_list.append(int_list[i])
        i += 1
    return even_list


def sub(a_list: list[int], start_i, end_i) -> list[int]:
    """This function returns the values between two inputed ints."""
    b_list: list[int] = []
    i: int = 0
    if start_i < 0:
        start_i = 0
    if end_i > len(a_list):
        end_i = len(a_list)
    if start_i > end_i:
        return b_list
    while i < len(a_list):
        if i >= start_i and i < end_i:
            b_list.append(a_list[i])
        i += 1
    return b_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """This function concatinates two lists together."""
    list_three: list[int] = []
    i: int = 0
    while i < len(list_one):
        list_three.append(list_one[i])
        i += 1

    i = 0

    while i < len(list_two):
        list_three.append(list_two[i])
        i += 1
    return list_three
