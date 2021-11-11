"""Practice with dictionaries."""

__author__ = "730247598"

# Define your functions below


def invert(invert_list: dict[str, str]) -> dict[str, str]:
    """Switches the keys and values in a dictionary."""
    inverted_list: dict[str, str] = dict()

    for k in invert_list:

        inverted_list[invert_list[k]] = k

    return inverted_list


def favorite_colors(colors: dict[str, str]) -> str:
    """Finds the mode value in a dictionary."""
    fav_color: str = " "

    for color_keys in colors:
        # 

    return fav_color
