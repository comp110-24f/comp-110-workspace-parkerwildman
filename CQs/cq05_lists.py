"""Mutating Functions"""

__author__ = "730774700"


def manual_append(list: list[int], number: int) -> None:
    list.append(number)  # appends number to the end of the list


def double(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        list[index] = list[index] * 2  # resets int at index to int at index times 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
# I think the same list will be printed for both list_1 and list_2
