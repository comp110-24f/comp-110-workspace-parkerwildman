"""CQ04"""

__author__ = "730774700"


def concat(word1: str, word2: str) -> str:
    return word1 + word2


if __name__ == "__main__":  # these inputs will only be used when this frame is run
    word1: str = "happy"  # stops the inputs from being called if the function concat is
    word2: str = "tuesday"  # imported to another frame
    print(concat(word1, word2))
