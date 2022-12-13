"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Final Exam, Part 1
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a python program which contains a user-defined function called
    'input_data'. This function should have a try/except block in it
    that will attempt to input a list of three players' last name and
    their associated number.  Each player name and number should be
    stored in an individual dictionary, one dictionary for each list
    element. In other words, you will have a list of dictionaries. For
    example, 'Jones', 44 would be one such pair of data. These
    name/number pairs should be placed in a dictionary object, and that
    object added to the list. The list should be returned by the
    function.  If there is an error inputting the names, the except
    block should set the player names to 'none', 0 for all three cases.

Functions:
    input_data():
        - Adds 3 player's names and numbers to list of player data.
"""


def input_data():
    """Adds 3 player's names and numbers to list of player data.

    :return:
        The list containing dictionary objects describing player data.
        Each list entry will change to {"last_nagit push origin masterme":
        "none", "number":
        0} if errors are raised during data entry.
    :rtype: list[dict]
    """
    data = []
    valid_entry = True
    print(
        "---NOTICE---\n"
        "Assignment instructions do not state that player numbers must be\n"
        "unique or must be only 1 or 2 digits. This function was developed\n"
        "within that specification. Assignment instruction do not state the\n"
        "player names must be unique. Semantic errors for player names\n"
        "(i.e., no name given or a names containing non-alphabetic\n"
        "characters) are handled by allowing the user to re-enter a name.\n"
        "------------\n"
    )

    while valid_entry and (len(data) < 3):
        try:
            while True:

                # name
                last_name = input("Enter a player's last name: ")\
                    .strip().title()
                if len(last_name) == 0:
                    print("    A player's name cannot be blank.")
                    continue
                keep_name = True
                if not last_name.isalpha():
                    print(f"    {last_name} contains a non-alphabetic "
                          f"character.")
                    while True:
                        confirm = input("Continue anyway? (y/n) ").lower()
                        if confirm in ["yes", "y"]:
                            break
                        elif confirm in ["no", "n"]:
                            keep_name = False
                            break
                        else:
                            print("    Invalid entry. Type 'y' or 'n'.")
                if not keep_name:
                    continue
                else:
                    break

                # number
            number = input(f"Enter number for {last_name}: ").strip()
            number = int(number)

        except ValueError:
            print("    Non-numeric character entered for player number.")
            valid_entry = False
        else:
            temp_dict = {
                "last_name": last_name,
                "number": number
            }
            data.append(temp_dict)

    if not valid_entry:
        data = [
            {"last_name": "none", "number": 0},
            {"last_name": "none", "number": 0},
            {"last_name": "none", "number": 0}
        ]

    return data


def main():
    print(
        "This file is not intended to be run as a script.\n"
        "This module is intended for import-use only.\n"
        "Please run 'jahnke_kenneth_final_part2.py' to test the\n"
        "    functionality of input_data()."
    )


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
