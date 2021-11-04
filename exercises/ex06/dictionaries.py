"""Practice with dictionaries."""

__author__ = "730247598"

# Define your functions below


def invert(invert_list: dict[str, str]) -> dict[str, str]:
    inverted_list: dict[str, str] = dict()
    value_list: list = list()
    

    for k in invert_list:
        value_list.append(invert_list[k])
        
        i: int = 0

        # Output
        while i < len(value_list):
            j: int = i + 1
            while j < len(value_list):
                if value_list[i] == value_list[j]:
                    raise KeyError("Duplicate values, cannot duplicate dictionary.")
                j += 1
            i += 1


        inverted_list[invert_list[k]] = k

    return inverted_list




