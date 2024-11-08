"""Function Practice Questions"""

__author__ = "730774700"


def mimic(message: str) -> str:
    """Repeats your input back to you"""
    return message


def main() -> None:
    """Prints the result of mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
