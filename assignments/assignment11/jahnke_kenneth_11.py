"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 11
Copyright (C) 2022 Kenneth Wayne Jahnke

"""

import os
import sys


def file_check(*files):
    """Checks if *files are in the current working directory (CWD).

    :param str files:
        Checks if these file names are in the CWD.
    :return:
        List of checked file not found in the CWD. The length of this
        list will equal 0 if all files are found.
    :rtype: list
    """
    absent_files = []
    for file in files:
        present = os.path.isfile(os.path.join(sys.path[0], file))
        if not present:
            absent_files.append(file)
    return absent_files


def ssn_dict_creator(ssn_file):
    """Creates a dictionary of data from ssn_file.

    Line format:
        <employee_id>, <ssn>, <date_of_birth>

    .. note::
        Datum separator is ', ' (read 'comma space').

    :param str ssn_file:
        The .txt from which data is read-in.
    :return:
        Dict w/ keys: {employee_id: {ssn, date_of_birth}}
    """
    ssn_dict = {}

    with open(ssn_file) as f:
        for line in f:
            elements = line.split(", ")
            no_newline = elements[2].replace("\n", "")
            del elements[-1]
            elements.append(no_newline)

            ssn_dict[elements[0]] = {
                "ssn": elements[1],
                "date_of_birth": elements[2]
            }

    return ssn_dict


# TODO
def det_dict_creator(det_file):
    """Creates a dictionary of data from det_file.

    Line format:
        <employee_id>, <name>, <date_of_joining>, <department>,
        <annual_salary>

    .. note::
        Datum separator is ', ' (read 'comma space').

    :param str det_file:
        The .txt from which data is read-in.
    :return:
        Dict w/ keys: {employee_id: {name, date_of_joining,
        department, annual_salary}}
    """


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
    ssn_file = "Employee_SSN.txt"
    det_file = "Employee_Details.txt"

    missing_files = file_check(ssn_file, det_file)
    if len(missing_files) > 0:
        for file in missing_files:
            print(f"{ssn_file} not found.")
        print("Ensure these files are in the current working directory\n"
              "    then rerun the program.")
        exit()

    # TODO
    # menu_options = {
    #     "1": {"prompt":
    #           "Search for an employee using their SSN and display the "
    #           "employee details.",
    #           "trigger": add_student,
    #           "file": ssn_file},  # file searched for ssn
    #     "2": {"prompt":
    #           "Sort by Employee ID and display the employee details.",
    #           "trigger": add_faculty,
    #           "file": det_file},  # file to sort by employee_id
    #     "4": {"prompt": "Exit", "trigger": exit_func}
    # }


    ssn_dict_creator(ssn_file)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
