"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Midterm, Program 2
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program with a user-defined function called 'clamp', which
    takes as an input a single integer. If the input number is negative,
    have the function return 0 (zero).  If the value is positive and
    greater than 255, have the function return 255. If the value is
    between 0 and 255 inclusive, have the function return the number
    unaltered. Write a main program section that prompts the user to
    enter a number, recasts it to an integer, and calls the clamp
    function. The program should then print out the value returned by
    the function call.

Functions:
    clamp(integer)
        - Wrangles integer into range 0-255, if applicable.
"""


def clamp(integer):
    """Wrangles integer into range 0-255, if applicable.

    - If integer is within range, it is not modified.
    - If integer is less than 0, it is modified to 0.
    - If integer is greater than 255, it is modified to 255.

    :param int integer:
        The number to be wrangled into range, if applicable.
    :return:
        The wrangled integer in range 0-255, inclusive.
    :rtype: int
    """
    if integer < 0:
        integer = 0
    if integer > 255:
        integer = 255

    return integer


def main():
    print("This program checks in as integer is in range 0-255. If outside\n"
          "this range, it will change the integer to 0 or 255, whichever is\n"
          "closest.")
    while True:
        prompt = input("Enter an integer: ").strip()
        try:
            prompt = int(prompt)
        except ValueError:
            print("Input must be represented as an integer.")
        else:
            break

    print(f"Clamped integer: {clamp(prompt)}")


if __name__ == '__main__':
    main()

# All work and no play makes Jack a dull boy.
