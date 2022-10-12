"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 6
Copyright (C) 2022 Kenneth Wayne Jahnke

Functions:
    display()
        - User creates a dictionary, then it is printed.
        - Option 1
    search()
        - Checks if a user-input string is a value in the_dict.
        - Option 2
    sort()
        - Sorts the_dict by key.
        - Option 3
    lists()
        - Prints keys and values of the_dict in separate sorted lists.
        - Option 4
    break_loop()
        - SEE NOTE IN FUNCTION DEFINITION.
        - Option 5
    menu()
        - Prints a menu and prompts the user for an option.
    main()
"""


def display(user_dict=None):  # option 1
    """User creates a dictionary, then it is printed.

    When prompted for a key, user must enter an int or the string
    'exit', which stops prompting user for more key-value pairs.
    For each key, user enters a string.

    :param user_dict:
        A user dict to add key-value pairs to. If argument is not
        passed (None), a new dict will be created.
    :type user_dict: dict or None
    :except ValueError:
        User attempted to enter a character that could not be
        converted to an int. Addressed by looping back to prompt.
    :return: The dict created by the user.
    :rtype: dict
    """
    if user_dict is None:
        user_dict = {}
    print("Let's create a dictionary.\n"
          "You will be asked for integers to be used as keys and\n"
          "    strings to be used as values.\n"
          "Note: previously entered dictionaries will be overwritten.\n"
          "To quit, type 'exit' at the key prompt.")

    while True:
        key = input("Enter a key: ").lower().strip()
        if key == "exit":
            break
        try:
            key = int(key)
        except ValueError:
            print("Invalid key entry. Enter an integer or 'exit'.")
        else:
            keep_old_key = False  # in case of duplicate keys
            if key in user_dict.keys():
                print("That is already a key in your dictionary.")
                while True:
                    key_overwrite = input(
                        "Do you want to overwrite the old key? (y/n): "
                        ).lower().strip()
                    if key_overwrite not in ["y", "yes", "n", "no"]:
                        print("    Invalid response.")
                    elif key_overwrite in ["n", "no"]:
                        keep_old_key = True
                        break
                    else:
                        break
            if keep_old_key:  # in case of duplicate keys
                continue

            while True:
                value = input("Enter a value: ")
                value_affirmed = True
                if len(value) == 0:
                    print("You entered an empty string for a value.")
                    while True:
                        verify_empty = input("Do you want to keep it? "
                                             "(y/n): ").lower().strip()
                        if verify_empty not in ["y", "yes", "n", "no"]:
                            print("    Invalid response.")
                        elif verify_empty in ["n", "no"]:
                            value_affirmed = False
                            break
                        else:
                            break
                if value_affirmed:
                    user_dict[key] = value
                    break

    print("Your dictionary:", user_dict, sep="\n")
    return user_dict


def search(the_dict):  # option 2
    """Checks if a user-input string is a value in the_dict.

    :param dict the_dict:
        The dict whose values are to be searched for a match of the
        user-input value.
    :return: None
    """
    print("Enter a string to see if it is a value in the dictionary.")
    user_str = input("String: ")

    for key, value in the_dict.items():
        if user_str == value:
            print(f"'{value}' is the value of key {key}.")
            break
    else:
        print(f"{user_str} is not a value in the dictionary.")


def sort(the_dict):  # option 3
    """Sorts the_dict by key.

    .. note::
        Per TA guidance, the original list is sorted, i.e., this func
        does not sort a copy while keeping the original intact.

    :param dict the_dict:
        The dict to be sorted.
    :return:
    """
    print(f"Original Dictionary:\n{the_dict}")

    # sorting criteria
    temp_dict = the_dict.copy()
    sort_keys = sorted(temp_dict.keys())

    # remove elements of old list
    for i in list(the_dict):
        del the_dict[i]

    # add sorted elements
    for i in sort_keys:
        for key, value in temp_dict.items():
            if key == i:
                the_dict[key] = value

    print(f"Key-Sorted Dictionary:\n{the_dict}")


def lists(the_dict):  # option 4
    """Prints keys and values of the_dict in separate sorted lists.

    :param dict the_dict:
        The dict whose keys and values are to be sorted into lists.
    :return: None
    """
    the_keys = sorted(the_dict.keys())
    the_values = sorted(the_dict.values())
    print("Sorted keys:", the_keys)
    print("Sorted values:", the_values)


def break_loop():  # option 5
    """SEE NOTE IN FUNCTION DEFINITION.

    ..note::
        For Assignment 6, this func is a "trigger" placeholder for
        Option 5 in options dict in main(), i.e., the break_loop object
        is referenced without call as only an indication to break the
        main loop.

    :return: None
    """
    pass


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
        print("    Option ", key, ": ", value["prompt"], sep="")
    option = input("Enter an option number: ")

    while True:
        if option in option_set:
            print()
            return option
        else:
            print(f"    {option} is not a valid option.")
            option = input("Enter an option number: ")


def main():
    options = {
        "1": {
            "prompt": "Create and Display the Dictionary",
            "trigger": display
        },
        "2": {
            "prompt": "Search a Value in the Dictionary",
            "trigger": search
        },
        "3": {
            "prompt": "Sort the Dictionary Based on Keys",
            "trigger": sort
        },
        "4": {
            "prompt": "Display the Keys and Values of the Dictionary as "
                      "Two Separate Lists",
            "trigger": lists
        },
        "5": {"prompt": "Exit", "trigger": break_loop}
    }

    user_dict = None
    while True:
        selected_option = menu(options)
        trigger = options[selected_option]["trigger"]
        if trigger is break_loop:  # see def break_loop() for more info
            print("Goodbye.")
            break
        elif trigger is display:
            user_dict = trigger(user_dict)  # display()
        elif not user_dict:
            print("No dictionary initialized.\n"
                  "Select Option 1 to initialize.")
        else:
            trigger(user_dict)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
