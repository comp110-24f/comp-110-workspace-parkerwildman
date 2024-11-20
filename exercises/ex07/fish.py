"""File to define Fish class."""

__author__ = "730774700"


class Fish:
    """New object Fish."""

    age: int

    def __init__(self):  # initializes fish class
        """Initializes a fish creation."""
        self.age = 0  # age becomes zero
        return None

    def one_day(self):
        """Simulates how fish change per day."""
        self.age += 1  # with each day age increases by 1
        return None
