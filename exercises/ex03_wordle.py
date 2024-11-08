"""Exercise 3: creating the wordle game"""

__author__ = "730774700"


def input_guess(secret_word_len: int) -> str:
    """Verifying the secret_word is the right length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # uses len of secret word so it is versatile for all word lengths
    return guess


def contains_char(secret_word: str, letter_guess: str) -> bool:
    """This function is searching for an existence of a letter in the guessed word"""
    assert len(letter_guess) == 1

    index: int = 0
    while index < len(secret_word):
        if (
            letter_guess == secret_word[index]
        ):  # tells if letter is found in the secret word
            return True
        index += 1  # to stop infinite loop
    return False  # if letter is not found in the secret word


def emojified(user_guess: str, secret_word: str) -> str:
    """This tells if the characters of the guess are in the secret word using emojis"""
    assert len(user_guess) == len(secret_word)
    empty: str = ""  # all the globals needed to run loop and print outcomes
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    index1: int = 0
    index2: int = 0
    contains: str = ""
    while index1 < len(secret_word):
        if contains_char(secret_word, user_guess[index2]) is True:
            contains += "True"  # tells if letter is found in the word
        else:
            contains += "False"  # tells if the letter is not found at all
        if secret_word[index1] == user_guess[index2] and contains == "True":
            empty += green_box  # if letter is in the right place and found in word
        if (
            user_guess[index2] != secret_word[index1] and contains == "True"
        ):  # if letter is in the wrong place, but is found in the word
            empty += yellow_box
        if contains == "False":  # letter is not found in the word
            empty += white_box
        index1 += 1
        index2 += 1
        contains = ""

    return empty


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turns: int = (
        1  # determines number of turns starts at one because wordle starts at 1
    )
    while turns < 7:  # when turns equal 7 the game is over
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # since return of input_guess is the guess, guess will input_guess(input)
        print(emojified(user_guess=guess, secret_word=secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            break  # if they win while loop needs broken
        if (
            guess != secret
        ):  # just increasing turn counter because user didn't get correct word
            turns += 1
        if (
            turns == 7
        ):  # this will print last statement to let user know the game is over
            print("X/6 Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
