"""Practicing with lists and lists functions"""

__author__ = "730774700"


def all(list: list[int], num: int) -> bool:
    if len(list) == 0:
        return False
    index: int = 0
    total: int = 0
    while index < len(list):
        if list[index] == num:
            total += 1
            index += 1
        else:
            index += 1
    if (
        total == index
    ):  # if total is the same as index(because index is 1+ the length of the list)
        return (
            True  # this tells if every number in the list was equal to the target value
        )
    else:  # any number that is not equal to index will mean that not all were equal
        return False


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # raises error message if len is 0

    largest = list[0]  # starts by comparing with the int at the start of the list
    for i in list:
        if i > largest:
            largest = i  # replaces largest value with the true largest
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):  # tests for lists that aren't the same length
        return False
    index: int = 0
    while index < len(list1):
        if (
            list1[index] != list2[index]
        ):  # if the numbers at the given index don't equal then it's false
            return False
        else:  # everything else needs to continue through the lists
            index += 1
    return True  # true if it goes through entire list and doesn't return false


def extend(list1: list[int], list2: list[int]) -> None:
    for i in list2:
        list1.append(i)  # puts every value in list2 onto the end of list1
