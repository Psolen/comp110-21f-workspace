"""Practice with dictionaries."""

__author__ = "730247598"

# Define your functions below


def invert(invert_list: dict[str, str]) -> dict[str, str]:
    inverted_list: dict[str, str] = dict()
    value_list: list = list()


    for k in invert_list:
        if invert_list[k] == k:

            raise KeyError("Duplicate keys, cannot invert.")


    for k in invert_list:

        inverted_list[invert_list[k]] = k

    return inverted_list




