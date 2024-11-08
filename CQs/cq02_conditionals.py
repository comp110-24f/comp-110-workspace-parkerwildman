"""Writing a simple number guessing game"""

__author__ = "730774700"


def guess_a_number() -> None:  # signature of function
    secret = 7
    guess: str = input("Guess a number: ")  # asking for user input of their guess
    print("Your guess was " + guess)  # retelling what guess was
    if int(guess) == secret:  # telling if guess is the same as the secret number
        print("You got it!")
    elif int(guess) > secret:  # telling if guess is higher than the secret number
        print("Your guess was too high! The secret number is " + str(secret))
    else:  # telling if guess is lower than the secret number
        print("Your guess was too low! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
