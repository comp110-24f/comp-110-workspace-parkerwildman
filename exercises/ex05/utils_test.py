"""defining unit tests for list functions"""

__author__ = "730774700"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge() -> None:
    """Tests that when input list is empty an empty list is returned"""
    list_1 = []
    assert only_evens(list_1) == []


def test_only_evens_mutation() -> None:
    """Tests that original list is not mutated"""
    list_1 = [5, 6, 7, 8, 9]
    only_evens(list_1)
    assert list_1 == [5, 6, 7, 8, 9]


def test_only_evens_return() -> None:
    """Tests that the return value of only evens is correct"""
    list_1 = [1, 2, 3, 4, 5]
    assert only_evens(list_1) == [
        2,
        4,
    ]  # tests that only_evens returns the correct values


def test_sub_return() -> None:
    """Tests that the return value of sub is correct"""
    list_1 = [10, 30, 50, 70, 90]
    start_index: int = 1
    stop_index: int = 4
    assert sub(list_1, start_index, stop_index) == [30, 50, 70]


def test_sub_mutation() -> None:
    """Tests that original list is not mutated"""
    list_1 = [5, 6, 7, 8, 9]
    start_index: int = 1
    stop_index = 4
    sub(list_1, start_index, stop_index)
    assert list_1 == [5, 6, 7, 8, 9]


def test_sub_edge() -> None:
    list_1 = [1, 5, 7, 9]
    start_index = -1
    stop_index = 2
    assert sub(list_1, start_index, stop_index)[0] == list_1[0]


def test_add_at_index_return() -> None:
    """Test return value of add_at_index"""
    list_1 = [5, 6, 7, 9]
    at_index = 3
    num = 8
    add_at_index(list_1, num, at_index)
    assert list_1 == [5, 6, 7, 8, 9]


def test_add_at_index_mutation() -> None:
    list_1 = [5, 6, 7, 9]
    at_index = 3
    num = 8
    add_at_index(list_1, num, at_index)
    assert list_1[3] == 8


def test_edge_add_at_index() -> None:
    """Test that add_at_index raised an IndexError for an invalid index."""
    list_1 = [1, 2, 3, 5]
    at_index = -1
    num = 1
    with pytest.raises(IndexError):
        add_at_index(list_1, num, at_index)
