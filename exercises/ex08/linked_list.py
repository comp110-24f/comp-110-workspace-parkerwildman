"""Practice with recursive structures and processes."""

from __future__ import annotations


class Node:
    """New type called Node with two inputs value and next."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes the Node class."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the last node
    if head.next is None:
        return head.value
    else:
        # Recursive Case:
        rest: int = last(head.next)
        return rest


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the node that is present at the inputted index."""
    # edge case
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # base case
    if index == 0:
        return head.value
    # recursive case
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finds the max value within the Nodes and returns it."""
    # base case
    if head is None:
        raise IndexError("Cannot call max with None")
    # finding the last value in the list
    if head.next is None:
        return head.value
    # recursive case to find the max in the rest of the list
    maximum: int = max(head.next)
    if head.value > maximum:
        return head.value
    else:
        return maximum


def linkify(items: list[int]) -> Node | None:
    if len(items) == 0:
        return None
    else:
        
