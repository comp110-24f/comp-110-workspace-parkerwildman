def get_first(input: list[str]) -> str:
    """return first element"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """modifying list: removing first element of the list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """return the first element and removes while still returning the removed element"""
    first: str = get_first(input)
    remove_first(input)
    return first
