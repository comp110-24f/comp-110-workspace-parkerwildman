"""Challenge question 3! Practicing while loops"""

__author__ = 730774700


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0  # starts the function at index 0
    count: int = 0  # starts count at 0
    while index < len(
        phrase
    ):  # this allows function to run through the length of the word
        if (
            phrase[index] == search_char
        ):  # searchs throughout the word for the specific char
            count += 1  # if character is found at given index the count increases by 1
        else:
            count += (
                0  # if character isn't found at the given index count doesn't increase
            )
        index += 1  # so loop isn't infinite and the loop will run through the word
    return count  # returns the count
