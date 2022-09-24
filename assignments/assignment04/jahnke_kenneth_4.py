"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 04
Copyright (C) 2022 Kenneth Wayne Jahnke

"""


# TODO
def option_one():
    pass


# TODO
def option_two():
    pass


# TODO
def option_three():
    """

    :return:
    """
    user_ints = []
    print("You will be asked for 5 integers.\n"
          "The program will calculate the square of each integer.\n")

    while len(user_ints) < 5:
        if len(user_ints) == 0:
            prompt_text = "Enter an integer: "
        else:
            prompt_text = "Enter another integer: "

        while True:
            try:
                prompt = int(input(prompt_text).strip())
            except ValueError:
                print("    Integers are the only valid input type.")
            else:
                user_ints.append(prompt)
                break

    return user_ints


def main():
    pass


if __name__ == "__main__":
    option_three()

# All work and no play makes Jack a dull boy.
