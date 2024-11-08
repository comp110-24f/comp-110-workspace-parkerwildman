"""Some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty str to copy calues over
    index: int = 0  # local variables
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]  # copy + msg[index]
        index += 1
    return copy


# remove_chars("football", "o") -> "ftball"
if __name__ == "__main__":
    word: str = "yoyo"
    print(remove_chars(msg=word, char="y"))
    print(remove_chars(word, "o"))
