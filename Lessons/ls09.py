"""Practice with Conditionals and Variables and "elif" statements"""


def less_than_10(num: int) -> None:
    """Tell me if num is <10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


def number_info(num: int) -> int:
    if num < 10:
        print("Small number.")
    else:
        if num % 2 == 0:
            print("Even Number.")
        else:
            print("Odd number.")
    return num


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
