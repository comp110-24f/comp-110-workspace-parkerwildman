"""Basic syntax of lists"""

my_numbers: list[float] = list()  # this is a constructor
my_numbers: list[float] = []  # this is the literal


my_numbers.append(1.5)
my_numbers.append(2.3)


# create an already populated list
game_points: list[int] = [102, 86, 94]  # can't use list() here
"""list() is only for creating an empty list"""

# subscription notation/indexing
last_game: int = game_points[2]
# print(last_game)

# Modifying elements because lists are mutable
game_points[1] = 72  # can't do this with strings
# print(game_points)

# getting the length
# print(len(game_points))
y: int = len(game_points)
# print(y)

# removing items from a list
game_points.pop(1)
# print(game_points)

# write a function called display
# Input: list[int]
# Return Value: None
# loop over the input and print every value
# Try calling it on game points


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


# display(game_points)

print(["kris", "kaki", "Alyssa"][1])
