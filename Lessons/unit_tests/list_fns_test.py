from Lessons.unit_tests.lists_fns import *


def test_get_first() -> None:
    animals: list[str] = ["dog", "cat", "penguin"]
    assert get_first(animals) == "dog"


def test_remove_first() -> None:
    animals: list[str] = ["dog", "cat", "penguin"]
    assert remove_first(animals) is None


def test_remove_first_behavior() -> None:
    animals: list[str] = ["dog", "cat", "penguin"]
    remove_first(animals)
    assert animals == ["cat", "penguin"]
