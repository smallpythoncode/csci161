"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 04
Copyright (C) 2022 Kenneth Wayne Jahnke

Assignment:
    Create menu function and print out the following options using while
    loop. Exit from the program when user enters option 5. The functions
    performed by each option is given below:

    Option 1: Ask the user to input a string “CSCI161L” and assign it to
    a variable. Use string operations to print the following: “CSCI”,
    ”161”, and reverse version of the string (“L161ICSC”) using string
    slicing.

    Option 2: Ask the user to input a string and assign it to a variable
    and check whether it is palindrome using string slicing.

    Option 3: Create a list which consists of 5 integers or input 5
    integers from users and assign to a list separated by comma and
    print out their squares using any loop.

    Option 4: Exit from the program.

Functions:
    option_one()
        - String 'CSCI161L' is input and sliced per assignment.
    option_two()
        - Checks if a user-input word or phrase is a palindrome.
    option_three()
        - Calculates and prints the squares of 5 user-input integers.
    menu()
        - Prints a menu and prompts the user for an option.
    break_loop()
        - Raises the LoopBreak exception.

Classes:
    LoopBreak(Exception)
     - The exception raised by the break_loop func.
"""

import string


def option_one():
    """String 'CSCI161L' is input and sliced per assignment.

    Prints the required slices.

    Slices required per assignment:
        1. 'CSCI'
        2. '161'
        3. 'L161ICSC' (original string reversed)

    .. note::
        Per assignment instructions, the user is to input str
        'CSCI161L'. If this is not input, the user is informed of an
        incorrect input and instructed to enter the required string.
        Implementation would likely be different if the mandates of the
        assignment were different.

    :return: None
    """
    required_string = "CSCI161L"

    input_string = input(f"Enter '{required_string}': ").upper().strip()
    while input_string != required_string:
        print("    That is not the correct string.")
        input_string = input(f"Enter '{required_string}': ").upper().strip()

    print(input_string[:4])
    print(input_string[4:7])
    print(input_string[::-1])


def option_two():
    """Checks if a user-input word or phrase is a palindrome.

    :return: None
    """
    print("Enter a word or phrase to check if it is a palindrome.")
    original_str = input(">>> ").strip()

    # converts to lower for easier evaluation
    eval_str = original_str.lower()
    # removes punctuation marks
    eval_str = eval_str.translate(
        str.maketrans("", "", string.punctuation)
    )
    # removes whitespace
    eval_str = eval_str.translate(
        str.maketrans("", "", string.whitespace)
    )
    reverse_str = eval_str[::-1]

    if len(eval_str) == 0:
        print("You did not enter a palindrome.\n"
              "In fact, you did not enter anything at all.")
    elif len(eval_str) == 1:
        print("Is a single character its own palindrome?")
    elif reverse_str == eval_str:
        print(f"'{original_str}' is a palindrome.")
    else:
        print(f"'{original_str}' is NOT a palindrome.")


def option_three():
    """Calculates and prints the squares of 5 user-input integers.

    :except ValueError:
        Only strings that can be converted to ints may be input. The
        user is notified of this in the event of a bad string input and
        prompted again for the target input.
    :return: None
    """
    user_ints = []
    print("You will be asked for 5 integers.\n"
          "The program will calculate the square of each integer.")

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

    square_statements = [f"{i} squared is {i ** 2}." for i in user_ints]
    for statement in square_statements:
        print(statement)


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
        "1": {"prompt": "String Operation 1", "trigger": option_one},
        "2": {"prompt": "String Operation 2", "trigger": option_two},
        "3": {"prompt": "List Operation 1", "trigger": option_three},
        "4": {"prompt": "Exit", "trigger": break_loop}
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
