"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Final Exam, Part 2
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Take the function from Part 1 and place it into a loadable module
    called Players. Write a program that imports Players and calls the
    function, thus building the list, then prints the list returned by
    the module.
"""


def main():
    try:
        from Players import input_data
        player_data = input_data()
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "Ensure 'Players.py' is in the current working directory and\n"
            "rerun the program."
        )
    else:
        print(player_data)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
