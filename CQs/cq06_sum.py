"""Summing the elements of a list using different loops"""

__author__ = "730774700"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):  # only works while index<0
        sum += vals[index]  # adds the float at vals[index] to the sum
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in vals:  # goes through every float in vals and adds it to sum
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in range(
        len(vals)
    ):  # makes a list of numbers from 0 up to but not including len(vals)
        sum += vals[
            i
        ]  # starts at 0 and works through numbers in range and adds them to sum
    return sum
