"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Lab 02
Copyright (C) 2022 Kenneth Jahnke

Write a python program that prints a menu, with options performing the
following operations. The option number should be provided as user
input. The functions performed by each option is given below:

Option 1: User input your name and age store it in variables ‘name’
and ‘age’ respectively. Then print the statement as “My name is <<name>>
and my age is << age>>”.

Option 2: Accept two coordinate values as float and store them in
variables x1, y1, x2 and y2. Find the distance between two points (x1,
y1) and (x2, y2) using the formula, sqrt((x2 – x1) ** 2 + (y2 – y1) ** 2
) and print them. (Hint: You may need to import math module and use sqrt
() and pow ()).

Option 3: Exit from the program.
"""

import math


def menu(option_set):
    """Prints a menu and prompts the user for an option.

    :param dict option_set:
        The menu options. The keys are the numbered option as a str. The
        values are a dict. That dict has 2 elements: the prompt printed
        on the menu and the 'trigger', the func called if 'pulled'.
    :return: The option selected by the user.
    :rtype: str
    """
    print("\nMenu:")
    for key, value in option_set.items():
        print("    ", key, ". ", value["prompt"], sep="")
    prompt = input("Please enter an option: ")

    while True:
        if prompt in option_set:
            print()
            return prompt
        else:
            print(f"    {prompt} is not a valid option.")
            prompt = input("Please enter an option: ")


def name_age():
    """Prompts a user for their name, age and prints it back to them.

    :except ValueError:
        Ages must be represented as ints.
    :return: None
    """
    while True:
        name = input("Enter your name: ").title()
        if len(name) > 0:
            break
        else:
            print("    A man has no name.")

    while True:
        age = input("Enter your age: ")
        try:
            age = int(age)
            if age < 0:
                print("    Okay, Benjamin Button....")
                continue
            elif age == 0:
                age = "baby"
        except ValueError:
            print(f"    {age} is not a valid age.")
        else:
            break

    if age == "baby":
        print(f"\nMy name is {name} and I am just a baby.")
    else:
        print(f"\nMy name is {name} and my age is {age}.")


def coordinate_distance():
    """Prints the distance between two points given by the user.

    :except ValueError:
        Enter coordinates as integers or floats only.
    :return: None
    """
    coords = {
        "x1": {"prompt": "x-value of first coordinate", "coord": ""},
        "y1": {"prompt": "y-value of first coordinate", "coord": ""},
        "x2": {"prompt": "x-value of second coordinate", "coord": ""},
        "y2": {"prompt": "y-value of second coordinate", "coord": ""}
    }

    coords_entered = 0
    while coords_entered < len(coords):
        for key, value in coords.items():
            if value["coord"] == "":
                try:
                    prompt = value["prompt"]
                    coord = input(f"Enter the {prompt}: ")
                    coord = float(coord)
                except ValueError:
                    print("    Enter coordinates as integers or floats only.")
                    break
                else:
                    coords[key]["coord"] = coord
                    coords_entered += 1

    x1 = coords["x1"]["coord"]
    y1 = coords["y1"]["coord"]
    x2 = coords["x2"]["coord"]
    y2 = coords["y2"]["coord"]

    horizontal_distance = (x2 - x1) ** 2
    vertical_distance = (y2 - y1) ** 2
    hypotenuse = math.sqrt(horizontal_distance + vertical_distance)

    print(f"\nThe distance between (x1, y1) and (x2, y2): {hypotenuse:.4f}.")


class LoopBreak(Exception):
    """The exception raised by the break_loop func.

    The triggers within the options dict in main indicate what action to
    take based on the option chosen by the user. To exit the program,
    the option prompt loop must be broken. Since the 'break' keyword
    cannot be stored as a dictionary value, another method is required
    to 'call' a break. The trigger to break the loop calls break_loop
    which raises this exception which is then handled by breaking the
    loop.
    """
    pass


def break_loop():
    """Raises the LoopBreak exception.

    The 'break' keyword cannot be stored as dict value. This func is
    called to raise the LoopBreak exception created to be handled by
    inserting a break.

    :raise LoopBreak:
        The exception is designed to be handled by breaking a loop.
    :return: None
    """
    raise LoopBreak


def main():
    options = {
        "1": {"prompt": "Option 1", "trigger": name_age},
        "2": {"prompt": "Option 2", "trigger": coordinate_distance},
        "3": {"prompt": "Exit", "trigger": break_loop}
    }

    while True:
        selected_option = menu(options)
        trigger = options[selected_option]["trigger"]
        try:
            trigger()
        except LoopBreak:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
