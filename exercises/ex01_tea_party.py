"""Calculating amounts based on inputs of number of people for a tea party"""

__author__ = "730774700"


def main_planner(guests: int) -> None:
    """Combines dif functions to give cost, teabags and treats needed"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # calls teabags function to get # of teabags needed
    print(
        "Treats: " + str(treats(guests))
    )  # calls treats function to give number of treats needed
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # calls cost function so that total cost can be calculated


def tea_bags(people: int) -> int:
    """Calculates the number of tea_bags needed for each guest"""
    return people * 2  # two teabags needed per guest


def treats(people: int) -> int:
    """Calculates the number of treats needed per guest"""
    return int(
        tea_bags(people=people) * 1.5
    )  # 1.5 treats needed per cup of tea so teabags function is called


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the treats plus teabags for # of guests"""
    return (
        tea_count * 0.5 + treat_count * 0.75
    )  # parameters for this have to call previous functions to get the counts


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests?")))
