"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 5
Copyright (C) 2022 Kenneth Wayne Jahnke

.. note::
    The instructions of this assignment call for the use of global
    variables. For reasons I explained in an email with the subject
    "CSCI 161 - Assignment 5 Questions", I explained why that use is a
    poor choice given the context of the assignment. I proposed the
    alternate methodology of defining variables in the functions' local
    namespace. This alternate methodology was approved by TA Meera
    Gopinath Sujatha via email on 20220929.

Functions:
    minimum()
        - Prints the minimum between 2 user-input numbers.
    discount()
        - Calculates the discount of an integer.
    pythagorean()
        - A user guesses the hypotenuse of a right triangle.
    menu()
        - Prints a menu and prompts the user for an option.
    exit_func()
        - Exits the menu by raising the LoopBreak exception.
    main()

Classes:
    LoopBreak(Exception)
     - The exception raised by the break_loop func.
"""

from math import sqrt


def minimum():
    """Prints the minimum between 2 user-input numbers.

    :except ValueError:
        Only numbers may be input, i.e., strings that can be converted
        to floats. This error is handled by looping back around and
        re-prompting for a number.
    :return: None
    """
    compare_nums = {"first": None, "second": None}
    print("You will be prompted for 2 numbers.\n"
          "This function will identify the minimum between those 2 numbers.")

    while None in compare_nums.values():
        for key in compare_nums.keys():
            if not compare_nums[key]:
                try:
                    compare_nums[key] = \
                        float(input(f"Enter the {key} number: "))
                except ValueError:
                    print("    You don't follow instructions very well...")
                    break

    print(f"The minimum: {min(compare_nums.values())}")


def discount():
    """Calculates the discount of an integer.

    The user is prompted for an integer and a percentage rate (as an
    integer). The discount (the percentage off of the original integer)
    is then calculated and printed.

    .. note::
        It is presumed the user will provide coherent inputs. The
        current version of this function does not handle semantic errors
        such as the original integer being less than or equal to 0 (if
        the idea were to calculate price discounts), the discount rate
        being less than or equal to 0, or the discount rate being
        greater than or equal to 100.

    :except ValueError:
        Only integers may be input. This error is handled by looping
        back around and re-prompting for an integer.
    :return: None
    """
    the_numbers = {
        "an integer": None,
        "a percentage rate (%)": None
    }
    print("You will be prompted for an integer and a percentage rate "
          "(as an integer) by\nwhich to discount the original "
          "integer.")

    while None in the_numbers.values():
        for key in the_numbers.keys():
            if not the_numbers[key]:
                try:
                    the_numbers[key] = float(input(f"Enter {key}: "))
                except ValueError:
                    print("    These values must be integers.")
                    break

    the_int = the_numbers["an integer"]
    the_rate = the_numbers["a percentage rate (%)"]
    # marked 'the_discount' to avoid shadowing name of the function
    the_discount = the_int * (the_rate / 100)

    print(f"The discount: {the_discount:.2f}")


def pythagorean():
    """A user guesses the hypotenuse of a right triangle.

    The user is prompted for a height and base of a right triangle. The
    user is then prompted to guess the length of the hypotenuse of this
    triangle. The function will calculate the length of the hypotenuse
    and notify the user if his/her guess is correct.

    :except ValueError:
        Only numbers may be input, i.e., strings that can be converted
        to floats. This error is handled by looping back around and
        re-prompting for a number.
    :return:
        As required by the assignment instructions, returns a bool
        indicating whether the guessed hypotenuse length is correct
        given the user-input height and base of a right triangle.
    :rtype: bool
    """
    user_dimensions = {
        "height": None,
        "base": None,
        "hypotenuse": None
    }
    print("You will be prompted for a height and base for a right triangle.\n"
          "You will then be prompted to guess the length the triangle's "
          "hypotenuse.")

    while None in user_dimensions.values():
        for key in user_dimensions.keys():
            if not user_dimensions[key]:
                try:
                    user_dimensions[key] = float(input(f"Enter a {key}: "))
                except ValueError:
                    print("    The dimensions of a triangle are typically "
                          "expressed as integers or\n"
                          "    floating point numbers.")
                    break
                else:
                    if user_dimensions[key] <= 0:
                        print("    Any dimension of a triangle must be "
                              "greater than 0.")
                        user_dimensions[key] = None
                        break

    the_height = user_dimensions["height"]
    the_base = user_dimensions["base"]
    # the actual height of the triangle based on height and base
    the_hypotenuse = sqrt((the_height ** 2) + (the_base ** 2))

    if user_dimensions["hypotenuse"] == the_hypotenuse:
        print("You guessed the hypotenuse correctly!")
        return_bool = True
    else:
        print("Sorry, your guess of the hypotenuse was incorrect.")
        return_bool = False
    print(f"The hypotenuse length: {the_hypotenuse:.4f}")

    return return_bool


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


def exit_func():
    """Exits the menu by raising the LoopBreak exception.

    The 'break' keyword cannot be stored as dict value. This func is
    called to raise the LoopBreak exception created to be handled by
    inserting a break.

    :raise LoopBreak:
        The exception is designed to be handled by breaking a loop.
    :return: None
    """
    raise LoopBreak


def main():
    menu_options = {
        "1": {"prompt": "Minimum", "trigger": minimum},
        "2": {"prompt": "Calculate Discount", "trigger": discount},
        "3": {"prompt": "Pythagorean Theorem", "trigger": pythagorean},
        "4": {"prompt": "Exit", "trigger": exit_func}
    }

    while True:
        selected_option = menu(menu_options)
        trigger = menu_options[selected_option]["trigger"]
        try:
            return_value = trigger()
            # accounts for the return required by pythagorean()
            if return_value is not None:
                print(f"Return value: {return_value}")
        except LoopBreak:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
