"""Practice with dictionaries."""

__author__ = "730247598"

# Define your functions below


def invert(invert_list: dict[str, str]) -> dict[str, str]:
    """Switches the keys and values in a dictionary."""
    inverted_list: dict[str, str] = dict()

    for k in invert_list:

        inverted_list[invert_list[k]] = k

    return inverted_list


def favorite_colors(color_list: dict[str, str]) -> str:
    """Finds the mode value in a dictionary."""
    color_count: dict[str, int] = {}
    inverted_dict: dict[int, str] = dict()
    fav_color: str = ""
    current: int = 0
    max: int = 0


    for keys in color_list:
        is_color_present: bool = color_list[keys] in color_count

        if is_color_present == False:
            color_count[color_list[keys]] = 1
        elif is_color_present == True:
            color_count[color_list[keys]] += 1

    for k in color_count:
        inverted_dict[color_count[k]] = k
    
    for j in inverted_dict:

        current = j

        if current > max:
            max = current
        
        fav_color = inverted_dict[max]

    return fav_color


def count(num_list: list[str]) -> dict[str, int]:
    answer: dict[str, int] = {}

    for i in num_list:
        if i in num_list:
            answer[i] += 1
        else:
            answer[i] = 1
    return answer

