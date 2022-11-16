"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 9
Copyright (C) 2022 Kenneth Wayne Jahnke

Functions:
    data_retrieval(file, delimiter="\t")
        - Gathers data from file into a list.
    grade_append(student_grades, file):
        - Calculates student grade and appends the data to file.
"""

import csv
import os
import sys


def data_retrieval(file, delimiter="\t"):
    """Gathers data from file into a list.

    :param file:
        The file to pull data from. Must be a .tsv, .csv, or other
        similar file type.
    :param str delimiter:
        The delimiting character.
    :return:
        All the data from file with each line as list.
    :rtype: list
    """
    with open(file) as f:
        file = csv.reader(f, delimiter=delimiter)

        row_data = []
        for row in file:
            row_data.append(row)

    return row_data


def grade_append(student_grades, file):
    """Calculates student grade and appends the data to file.

    .. note::
        See data formatting structure of the student_grades parameter
        below. Current version of this func does not implement any
        error checking.

    :param list student_grades:
        The student in a list with last name (str) at index 0, first
        name (str) at index 1, and all remaining indexes as grades
        (int).
    :param str file:
        The file to append data to.
    :rtype: None
    """
    append_data = student_grades.copy()

    counter = 0
    grades_sum = 0
    for grade in append_data[2:]:
        grade = int(grade)
        grades_sum = grades_sum + grade
        counter += 1
    average = grades_sum // counter

    if average >= 90:
        letter_grade = "A"
    elif 80 <= average < 90:
        letter_grade = "B"
    elif 70 <= average < 80:
        letter_grade = "C"
    elif 60 <= average < 70:
        letter_grade = "D"
    else:
        letter_grade = "E"  # yup...it's E per assignment instructions

    append_data.append(letter_grade)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(append_data)


def main():
    input_file = "studentinfo.tsv"
    output_file = "report.txt"

    while True:
        file_prompt = input(f"Use {input_file} "
                            f"as data file? (y/n) ").strip().lower()
        if file_prompt in ["y", "yes"]:
            break
        elif file_prompt in ["n", "no"]:
            input_file = input("Enter name of new data file: ")
        else:
            print("    Invalid response.")

    # for testing purposes
    # overwrites existing 'report.txt'
    # f = open(output_file, "w")
    # f.close()

    tsv_present = os.path.isfile(os.path.join(sys.path[0], input_file))

    if not tsv_present:
        print(f"Data file not found.\n"
              f"Ensure '{input_file}' is in the current working directory\n"
              f"    and the script again.")
        exit()

    data = data_retrieval(input_file)

    if (
        len(data) < 1 or
        len(data) > 20
    ):
        print("Number of data points in the .tsv should be at least 1 but no\n"
              "    more than 20.")
        while True:
            prompt = input("Proceed anyway? (y/n): ").strip().lower()
            if prompt in ["n", "no"]:
                exit()
            elif prompt in ["y", "yes"]:
                break
            else:
                print("    Invalid response.")

    for student in data:
        grade_append(student, output_file)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
