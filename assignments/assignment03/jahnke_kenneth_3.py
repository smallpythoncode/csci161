"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 03
Copyright (C) 2022 Kenneth W. Jahnke

# TODO - write assignment description
"""


def triangular_number_prompt():
    """Prompts the user for an n value for triangular number calculation.

    .. note::
        This function is designed to work in conjunction with
        triangular_number() from this same module.

    :except ValueError:
        The user is notified that the value for n may only be a positive
        integer.
    :return:
        The positive integer n for which the user has chosen to
        calculate a triangular number for.
    :rtype: int
    """
    print("A triangular number is the sum of the first n positive integers.")

    while True:
        prompt = input("Enter a value for n: ").strip()
        try:
            num = int(prompt)
        except ValueError:
            print("    n must be a positive integer.")
        else:
            if num < 1:
                print("    n must be a positive integer.")
            else:
                return num


def triangular_number(n=None):
    """Calculates the triangular number a given value n.

    A triangular number is the sum of the first n positive integers.

    For more info: https://en.wikipedia.org/wiki/Triangular_number

    :param n:
        If n=None, triangular_number_prompt() will be called so the user may
        input a value for n. Otherwise, n may be specified as an int at
        call. If not an int, the user will be prompted if they would like to
        specify a new value. If so, that new value will be used.
    :type n: int or None
    :return:
        If a valid n value was given, a tuple with the triangular number as
        the first element and the n value as the second element. Otherwise,
        a tuple with -1 as an indicator of invalidity as the first element
        and the n value as the second element (for uniform return as a
        tuple).
    :rtype: tuple[int, int]
    """
    # tri num will only be calculated if n is type int
    n_type_valid = True

    # will return a positive integer
    if n is None:
        n = triangular_number_prompt()

    # n type must be int for tri num calculation
    # non-positive integers cannot be used for tri num calculation
    elif (type(n) is not int) or (n < 1):
        print(f"    {n} is not a valid, i.e., a positive integer.")
        while True:
            type_prompt = \
                input("Would you like to change n? (y/n): ").lower().strip()
            if type_prompt in ["y", "yes"]:
                n = triangular_number_prompt()
                break
            elif type_prompt in ["n", "no"]:
                n_type_valid = False
                break
            else:
                print(f"    {type_prompt} is not a valid response.")

    if n_type_valid:
        one_to_n = [num for num in range(1, n + 1)]

        # this is the expedient method of finding the sum
        # tri_num = sum(one_to_n)

        # this is the method dictated by the assignment
        tri_num = 0
        iterations = 0
        # the while loop specified by the assignment
        while iterations < len(one_to_n):
            tri_num += one_to_n[iterations]
            iterations += 1

        return tri_num, n

    else:
        return -1, n


def prime_number_checker(num=None):
    """Checks if a number is prime.

    :param num:
        An integer to check for primality. If None, the user is prompted for
        an integer to check.
    :type num: int or None
    :except ValueError:
        If given value for num cannot be converted to an int, the first and
        second elements of return are marked False.
    :return:
        A tuple with three elements: Firstly, the value assigned to num.
        This value will be converted to an int if possible. Secondly, a bool
        indicating if the value of num is an int. Thirdly, a bool indicating
        if num is a prime number.
    :rtype: tuple[any, bool, bool]
    """
    num_is_int = True
    num_is_prime = True

    # code may be improved by adding a loop to verify an int was entered
    # alternatively, a separate function similar to triangular_number_prompt()
    if num is None:
        num = input("Enter an integer to check if it a prime number: ")\
            .strip()

    try:
        num = int(num)
    # code may be improved by asking user to modify num if ValueError
    except ValueError:
        num_is_int, num_is_prime = False, False
    else:
        if num <= 1:
            num_is_prime = False
        else:
            # the for loop specified by the assignment
            for i in range(2, num):
                if num % i == 0:
                    num_is_prime = False
                    break

    return num, num_is_int, num_is_prime


def odds_between_two_integers():
    """Identifies the odd integers between two user-defined integers.

    This function has two inputs: Firstly, an integer. Secondly, a greater
    integer. If the inputs are valid, the odd integers between the two
    inputs will be identified.

    ..note::
        The while loop specified by the assignment is implemented in
        'TASK 3' block of main().
    .. note::
        The assignment does not mandate any exception handling aside from
        displaying a message. This function may be improved by implementing
        a loop to correct exceptions as they arise.
    .. note::
        The functionality of this function may be improved by implementing
        default None parameters to indicate that integers are to be input
        at call.

    :except ValueError:
        Results in a return message indicating that integers are the only
        valid inputs.
    :return:
        If the inputs meet the conditions specified, the return is a list of
        odd integers between the two inputs. If the conditions are not met,
        the return is list with a single element, a str as a description of
        the fault. If the conditions are met but there are no odd integers
        between the inputs, the return is a list with single element, a str
        as an innocuous message.
    """
    odd_nums = []

    first_num = input("Enter an integer: ").strip()
    try:
        first_num = int(first_num)
    except ValueError:
        odd_nums.append("Integers are the only valid inputs for this "
                        "function.")
    else:
        second_num = input("Enter a greater integer: ").strip()
        try:
            second_num = int(second_num)
        except ValueError:
            odd_nums.append("Integers are the only valid inputs for this "
                            "function.")
        else:
            if first_num == second_num:
                odd_nums.append("The two integers input are identical.")
            elif first_num > second_num:
                odd_nums.append("The second integer must be greater than the "
                                "first.")
            else:
                for num in range(first_num + 1, second_num):
                    if num % 2 == 1:
                        odd_nums.append(num)

    if len(odd_nums) == 0:
        odd_nums.append("There are odd integers between the first integer and"
                        "the second integer.")

    return odd_nums


def print_this_string():
    """Prints the first four characters of the string 'CSCI161L'.

    .. note::
        The implementation of this function is bound to the assignment.
        If the assignment were different, the implementation would
        almost certainly be different.

    :return: None
    """

    this_string = "CSCI161L"
    chars_printed = 0
    for char in this_string:
        if char == "1":
            # the break statement specified by the assignment
            break
        else:
            print(char)


# TODO
def print_these_numbers():
    pass


def main():
    print("TASK 1")
    tri_num, n = triangular_number()
    if tri_num == -1:
        print("No valid value given for n. Triangular number not calculated.")
    else:
        print(f"{tri_num} is the triangular number for the first {n} "
              f"positive integers.")

    print("\nTASK 2")
    num_to_check, num_is_int, num_is_prime = prime_number_checker()
    if not num_is_int:
        print(f"{num_to_check} is not an integer, thus, it is not a prime "
              f"number.")
    elif num_is_prime:
        print(f"{num_to_check} is a prime number.")
    else:
        print(f"{num_to_check} is NOT a prime number.")

    print("\nTASK 3")
    # for my money, a for loop would be better than a while loop
    # odds = odds_between_two_integers()
    # for i in odds:
    #     print(i)

    # the while loop specified by the assignment
    odds = odds_between_two_integers()
    working_copy_odds = odds.copy()
    len_of_loop = len(working_copy_odds)

    while len_of_loop > 0:
        print(working_copy_odds[0])
        del working_copy_odds[0]
        len_of_loop -= 1

    print("\nTASK 4")
    print_this_string()

    print("\nTASK 5")
    # TODO


if __name__ == "__main__":


# All work and no play makes Jack a dull boy.

