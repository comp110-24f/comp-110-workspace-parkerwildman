"""Practice with dicts"""

__author__ = "730774700"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Takes the values of the input dict and makes them keys and the keys values"""
    new_dict: dict[str, str] = {}  # makes an empty dict
    for key in input:  # runs through the keys in the input dict
        value = input[key]  # makes the value equal to the value of the input
        if value in new_dict:  # checks if the value is in the dict
            raise KeyError(
                "Duplicate key found during inversion"
            )  # if it is it raises and error
        new_dict[value] = (
            key  # sets the key in the new dict as the value and the value as the key
        )
    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that is seen the most within the dict"""
    color_count: dict[str, int] = (
        {}
    )  # makes an empty dict to count the occurances of the colors
    for key in colors:  # goes through the names in colors
        if (
            colors[key] in color_count
        ):  # tells if the color is already a key in color_count
            color_count[
                colors[key]
            ] += 1  # if it is the the value at the given color key increases by 1
        else:
            color_count[colors[key]] = (
                1  # if it isn't already a key it is added and set to the value 1
            )
    max_count: int = 0
    most_frequent: str = ""
    for color in color_count:
        if max_count >= color_count[color]:
            max_count = max_count
        if max_count < color_count[color]:
            max_count = color_count[color]
            most_frequent = color
    return most_frequent


def count(input: list[str]) -> dict[str, int]:
    """counts the instances of a value in a list and adds them to a dict"""
    count_dict: dict[str, int] = {}  # creates empty dict for values to be added
    for i in input:  # goes through the values in the list
        if i in count_dict:  # if str in list is a key it adds 1 to the count
            count_dict[i] += 1
        else:  # if str in list is not a key it adds a new key and value
            count_dict[i] = 1
    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes words by their first letter"""
    alphabet_dict: dict[str, list[str]] = {}  # empty dict to start
    for word in words:
        first_letter = word[
            0
        ].lower()  # gathers the lowercase of the first letter of the words
        if (
            first_letter not in alphabet_dict
        ):  # if the letter isn't already a key it adds it
            alphabet_dict[first_letter] = []  # creates an empty list value for each key
        alphabet_dict[first_letter].append(
            word
        )  # adds the word to the list at the correct first_letter
    return alphabet_dict


def update_attendance(
    attendance_dict: dict[str, list[str]], day_of_the_week: str, student_name: str
) -> None:
    """Update an attendance dictionary that uses a day and a list of names"""
    if (
        day_of_the_week not in attendance_dict
    ):  # If day isn't already in attendance it adds as a key with empty list
        attendance_dict[day_of_the_week] = []

    if (
        student_name not in attendance_dict[day_of_the_week]
    ):  # if student isn't already accounted for adds student to the day
        attendance_dict[day_of_the_week].append(student_name)
