"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Final Exam, Part 3
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program that will open a text file called textfile1.txt for
    reading, and reads the contents. Determine how many lines are in the
    textfile, and print out the number as such: "The file contains X
    lines.", where X is the number of lines in the file. Then have the
    program print the contents of the file to a second text file called
    textfile2.txt, which your program will create when it runs.

Functions:
    remove_target_file(file):
        - Removes file.
    copy_file(original, new):
        - Copies a file.
    files_absent(*files):
        - Checks if *files are in the current working directory (CWD).
    line_count(file):
        - Counts the number of lines in file.
"""

import os
import shutil
import sys


def remove_target_file(file):
    """Removes file.

    :param str file:
        The name of the file to be removed.
    :rtype: None
    """
    if os.path.isfile(file):
        os.remove(file)


def copy_file(original, new):
    """Copies a file.

    Current version of this function does no exception handling because
    all predicted errors are handled in the context of this module as a
    script.

    :param str original:
        The name of the file to copy. This file must be present in the
        current working directory (CWD).
    :param str new:
        The name of the newly copied file. This file is copied to the
        CWD.
    :rtype: None
    """
    remove_target_file(new)
    shutil.copy(original, new)


def files_absent(*files):
    """Checks if *files are in the current working directory (CWD).

    :param str files:
        Checks if these file names are in the CWD.
    :return:
        List of checked files not found in the CWD. The length of this
        list will equal 0 if all files are found.
    :rtype: list
    """
    absent_files = []
    for file in files:
        present = os.path.isfile(os.path.join(sys.path[0], file))
        if not present:
            absent_files.append(file)
    return absent_files


def line_count(file):
    """Counts the number of lines in file.

    :param str file:
        The number of lines are counted from this file.
    :return:
        The number of lines in file
    :rtype: int
    """
    lines = 0
    with open(file) as f:
        for line in f:
            lines += 1
    return lines


def main():
    tf1 = "textfile1.txt"
    tf2 = "textfile2.txt"

    # removes tf2 if already present
    remove_target_file(tf2)

    absent_files = files_absent(tf1)
    if tf1 in absent_files:
        print(f"{tf1} not found in the current working directory.\n"
              f"Ensure this file is present and rerun the program.")

    else:
        lines = line_count(tf1)
        print(f"{tf1} contains {lines} lines.")
        copy_file(tf1, tf2)
        if os.path.isfile(tf2):
            print(f"{tf2} successfully created in the current working "
                  f"directory.")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
