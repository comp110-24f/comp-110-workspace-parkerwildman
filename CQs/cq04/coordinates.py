"""CQ04"""

__author__ = "730774700"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0  # need two indices to be able to run through both while loops
    index2: int = 0  # took me a while to figure out the use of two indices
    while index1 < len(xs):
        while index2 < len(ys):
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 += 1
        index1 += 1  # stops from being an infinite loop
        index2 = 0  # necessary so that it can run through the 2nd while loop again


get_coords("12", "34")
