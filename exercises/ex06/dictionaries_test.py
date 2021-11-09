"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730247598"


from exercises.ex06.dictionaries import invert


def test_empty() -> None:
    """Empty dictionary test."""
    assert invert({}) == {}


def test_basic() -> None:
    """Standard values test."""
    assert invert({"UNC" : "Duke"}) == {"Duke" : "UNC"}


def test_edge_duplicate_values() -> None:
    """Standard values test."""
    assert invert({"Phillip" : "Hooper", "Chad" : "Hooper"}) == {"Hooper" : "Phillip", "Hooper" : "Chad"} # KeyError("Duplicate keys, cannot invert.")