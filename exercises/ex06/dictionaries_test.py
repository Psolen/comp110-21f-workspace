"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730247598"


from exercises.ex06.dictionaries import count, invert, favorite_colors


def test_empty() -> None:
    """Empty dictionary test."""
    assert invert({}) == {}


def test_basic() -> None:
    """Standard values test."""
    assert invert({"UNC": "Duke"}) == {"Duke": "UNC"}


def test_edge_duplicate_values() -> None:
   """Double Key Test"""


def test_fav_colors() -> None:
   """Standard values for favorite color function."""
   assert favorite_colors({"Ezri" : "Blue", "Kaki": "Red", "Kris": "Blue"}) == "Blue"


def test_fav_colors_many() -> None:
   """Standard values for favorite color function."""
   assert favorite_colors({"Ezri" : "Black", "Kaki": "Red", "Kris": "Blue", "Phil": "Yellow", "Chad": "Black", "Tony": "Red"}) == "Red"


def test_fav_colors_equal() -> None:
   """Two values are were picked twice. The first value in the dictionary should be the one returned."""
   assert favorite_colors({"Ezri" : "Red", "Kaki": "Blue", "Kris": "Black", "Phil": "Yellow", "Chad": "Red", "Tony": "Blue"}) == "Blue"


def test_count() -> None:
   """Standard values for count function."""
   assert count(["Dog", "Cat", "Dog", "Lizard", "Cat", "Turtle"]) == {"Dog": 2, "Cat": 2, "Lizard": 1, "Turtle": 1}