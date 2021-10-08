"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730247598"

from exercises.ex05.utils import only_evens, sub, concat


# Tests for only_evens.
def test_only_evens_basic() -> None:
    """Standard values test."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_none() -> None:
    """All incorrect values test."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_all() -> None:
    """All correct values test."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


# Tests for sub.
def test_sub_basic() -> None:
    """Standard values test."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_none() -> None:
    """Empty list test."""
    assert sub([], 1, 3) == []


def test_sub_edge_begin_neg() -> None:
    """Starting index negative test."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test_sub_edge_end_out_of_bounds() -> None:
    """Ending index out of bounds test."""
    assert sub([10, 20, 30, 40], 1, 100) == [20, 30, 40]


def test_sub_edge_end_small() -> None:
    """Ending index smaller than starting index test."""
    assert sub([10, 20, 30, 40], 100, 1) == []


def test_sub_edge_neg_end() -> None:
    """Ending index negative test."""
    assert sub([10, 20, 30, 40], 100, -1) == []


# Tests for concat. 
def test_concat_basic() -> None:
    """Standard values test."""
    assert concat([10, 20], [30, 40]) == [10, 20, 30, 40]


def test_concat_none() -> None:
    """Double empty list test."""
    assert concat([], []) == []


def test_concat_edge_list_one_empty() -> None:
    """First list empty test."""
    assert concat([], [30, 40]) == [30, 40]


def test_concat_list_two_empty() -> None:
    """Last list empty test."""
    assert concat([-100, 90], []) == [-100, 90]