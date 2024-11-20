"""File to define Bear class."""

__author__ = "730774700"


class Bear:
    """New object bears."""

    age: int
    hunger_score: int

    def __init__(self):  # initializes the bears
        """Initializes the bear class with age and hunger_score."""
        self.age = 0  # start at age 0
        self.hunger_score = 0  # and start with hunger of 0
        return None

    def one_day(self):
        """What changes in a day for each bear."""
        self.age += 1  # each day age increases one
        self.hunger_score -= 1  # each day hunger score decreases by one
        return None

    def eat(self, num_fish: int):
        """Updates hunger score based on how many fish are eaten."""
        self.hunger_score += num_fish  # hunger score reflects how many fish are eaten
        return None
