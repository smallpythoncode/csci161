"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
# FIXME Assignment X
Copyright (C) 2022 Kenneth Wayne Jahnke

"""


# TODO
def display():  # option 1
    """ # TODO

    :return:
    """
    """
    the_dict = {}
    print("Let's create a dictionary.\n"
          "You will be asked for integers to be used as keys and strings to\n"
          "  be used as keys.\n"
          "Note: previously entered dictionaries will be overwritten.\n"
          "To quit, type 'exit' at the key prompt.")

    while True:
        key = input("Enter a key: ").lower()
        if len(key) == 0:  # if user enters nothing
            print("Please enter an integer or 'exit'.")
            continue
        # try:  # FIXME
    """
    print("called")  # FIXME - return original code, for testing only


# TODO
def search():  # option 2
    """ # TODO

    :return:
    """
    pass


# TODO
def sort():  # option 3
    """ # TODO

    :return:
    """
    # pass
    print("opt 3 called")  # FIXME - for testing only

# TODO
def lists():  # option 4
    """ # TODO

    :return:
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
    prompt = input("Enter an option number: ")

    while True:
        if prompt in option_set:
            print()
            return prompt
        else:
            print(f"    {prompt} is not a valid option.")
            prompt = input("Enter an option number: ")


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


def break_loop():  # option 5
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
    options = {  # FIXME - modify options, keep break_loop
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
    dict_init = False  # display() has been called, a dict initialized

    while True:
        print(dict_init)  # FIXME - delete, for testing only
        selected_option = menu(options)
        trigger = options[selected_option]["trigger"]
        if trigger is display:
            dict_init = True
        try:
            trigger()
        except LoopBreak:
            print("Goodbye.")
            break
        else:
            if not dict_init:
                print("no dict")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
