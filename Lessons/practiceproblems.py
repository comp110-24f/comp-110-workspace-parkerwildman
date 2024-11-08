def name_eval(name: str) -> bool:
    return len(name) % 2 == 0


def name_size(name: str) -> int:
    return int(len(name))


def double(x: int) -> int:
    return x * 2


print(double(x=3))


def my_string(word: str) -> str:
    return "This is my word, " + word


def my_num(word: float) -> None:
    print("This is my number, " + str(word))


from random import random


def sum(num1: int, num2: int) -> int:
    return num1 + num2

function_name(param_1=arg_1, param_2=arg_2)