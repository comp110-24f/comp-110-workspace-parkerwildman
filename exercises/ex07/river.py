"""File to define River class."""

__author__ = "730774700"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """A new River definition."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self):
        """Checks the age of the bears and fish and removes those that are too old."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:  # might just be <3
                new_fish.append(fish)  # adds fish that aren't too old
        for bears in self.bears:
            if bears.age <= 5:  # might just be <5
                new_bears.append(bears)  # adds the bears that aren't too old
        self.fish = new_fish  # sets original id to the ids that were made
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int):
        """Removes front fish from fish list."""
        new_fish: list[Fish] = []
        for _ in range(amount, len(self.fish)):
            new_fish.append(self.fish[_])
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Bear can eat if there are more than 5 fish if not no eating."""  # checks if there are enough fish
        index: int = 0
        while (
            len(self.fish) >= 5
        ):  # the bear will eat 3 fish until there aren't at least 5
            self.bears[index].eat(3)
            self.remove_fish(3)  # removes 3 fish because 3 are eaten
            index += 1
        return None

    def check_hunger(self):
        """Checks the hunger levels of bears and removes those who starve."""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(
                    bear
                )  # only adds bears who have a hunger score above 0
        self.bears = full_bears  # sets original id equal to newly created id
        return None

    def repopulate_fish(self):
        """How fish reproduce."""
        new_fish_amount: int = (len(self.fish) // 2) * 4  # for every pair 4 fish born
        for _ in range(
            len(self.fish), (len(self.fish) + new_fish_amount)
        ):  # stars at end of list and goes to add fish
            self.fish.append(Fish())  # actually adds a new baby fish
        return None

    def repopulate_bears(self):
        """How bears reproduce."""
        new_bears_amount: int = len(self.bears) // 2  # only one bear born per pair
        for _ in range(len(self.bears), (len(self.bears) + new_bears_amount)):
            self.bears.append(Bear())  # adds new baby bear
        return None

    def view_river(self):
        """Represents what happens on the river each day."""
        print(f"~~~ Day {str(self.day)}: ~~~")
        print(f"Fish population: {str(len(self.fish))}")
        print(f"Bear population: {str(len(self.bears))}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(0, 7):  # runs through one day 7 times to sim a week
            self.one_river_day()
