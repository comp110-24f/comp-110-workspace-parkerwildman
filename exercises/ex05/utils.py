"""implementing list utility functions"""

__author__ = "730774700"


def only_evens(given: list[int]) -> list[int]:
    evens: list[int] = []  # empty list where evens will be stored
    for i in given:
        if i % 2 == 0:  # determines if a number is even
            evens.append(i)  # adds number to evens list
    return evens  # returns only the even numbers


def sub(input: list[int], start_index: int, stop_index: int) -> list[int]:
    subset: list[int] = []  # new list for new numbers within specified range
    if start_index < 0:  # if index is negative it starts at the beginning which is 0
        start_index = 0
    if stop_index > len(
        input
    ):  # if index is longer than length of list it stops at len
        stop_index = len(input)
    if len(input) == 0 or start_index >= stop_index or stop_index <= 0:  # for odd cases
        return subset
    while start_index < stop_index:  # if indices work out enter while loop
        subset.append(input[start_index])  # adds numbers within index to subset list
        start_index += 1
    return subset  # returns numbers within range


def add_at_index(modify: list[int], add_num: int, at_index) -> None:
    if at_index > len(modify):  # raises an error if at index is too large
        raise IndexError("Index is out of bounds for the input list")
    if at_index < 0:  # raises error if at index is too small
        raise IndexError("Index is out of bounds for the input list")
    modify.append(0)  # adds a space into the list so it can be modified
    index: int = len(modify) - 1  # starts at the back of the list to move items
    while (
        index > at_index
    ):  # moves numbers one space to the right before the index of where num needs added
        modify[index] = modify[
            index - 1
        ]  # allows for nums to be moved on index to the right
        index -= 1  # stops infinite loop
    modify[at_index] = add_num  # adds the number in at the given index
