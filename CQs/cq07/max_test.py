from CQs.cq07.find_max import find_and_remove_max


def test_return_value_conventional() -> None:
    nums: list[int] = [12, 15, 17, 22, 98, 13, 16, 98]
    assert find_and_remove_max(nums) == 98  # checks that correct value is returned


def test_mutates_list() -> None:
    nums: list[int] = [12, 15, 17, 22, 98, 13, 16, 98]
    find_and_remove_max(nums)
    assert nums == [12, 15, 17, 22, 13, 16]  # checks that max is removed from list


def test_return_value_unconventional() -> None:
    empty: list[int] = []
    assert find_and_remove_max(empty) == -1  # checks that max is -1 for weird lists
