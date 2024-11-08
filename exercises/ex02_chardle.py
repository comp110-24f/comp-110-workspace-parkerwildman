"""Exercise 02 writing a program that runs like wordle but not wordle yet"""

__author__ = "730774700"


def main() -> None:
    contains_char(input_word(), input_letter())


def input_word() -> str:
    word: str = input(
        "Enter a 5-character word: "
    )  # takes user input and stores it as word
    if len(word) == 5:  # checks if the word is 5 characters
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word


def input_letter() -> str:
    letter: str = input(
        "Enter a single character: "
    )  # stores user letter input as letter
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character")
        exit()
        return letter
        # have to exit so it doesn't go through the contains_char function when the


# intial requirements aren't met

"""Error message has to be printed because when it was returned it became associated"""
"""with letter and messed up later return statments"""


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count > 0:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


"""All the if statments are running through the index of the word to see if there is"""
"""a match with the input letter"""


if __name__ == "__main__":
    main()
