"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Final Exam, Part 5
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program that will take in a string, and then compute all
    possible combinations of the letters in the string. For each of
    these scramblings, search for that particular 'word' in a dictionary
    file called dictionary.txt, which will be in the local directory. If
    a match is found, print "Found: <word>" where <word> is the
    scrambling. For instance, if the input string is 'tac', and the
    word 'cat' exists in dictionary.txt, the program should print out
    "Found: cat". The dictionary.txt file will be in the same directory
    as the program is run from, and will only contain about a dozen
    lines, each with a single word.

Functions:
    scrambling(word):
        - Computes all possible letter combinations of word.
"""

import itertools as it
import os


def scrambling(word):
    """Computes all possible letter combinations of word.

    :param str word:
        The word to be scrambled for letter combinations.
    :return:
        List of all possible letter combinations of word.
    :rtype: list
    """

    broken_scrambles = list(it.permutations(word))
    scrambles = []
    for i in broken_scrambles:
        x = "".join(i)
        scrambles.append(x)
    return scrambles


def main():
    dictionary_file = "dictionary.txt"
    if not os.path.isfile(dictionary_file):
        print(f"{dictionary_file} not found in current working directory.\n"
              f"    Ensure this file is present and rerun the program.")
        exit()

    print(
        "WARNING: Entering strings of length greater than 10 characters may\n"
        "    cause system memory issues!"
    )

    dictionary = []
    with open(dictionary_file) as f:
        for line in f:
            line = line.replace("\n", "")
            dictionary.append(line)

    while True:
        prompt = input("Enter a string: ").strip().lower()
        matching_word = False
        scrambles = scrambling(prompt)
        for word in scrambles:
            if word in dictionary:
                matching_word = True
                print(f"Found: {word}")
        if not matching_word:
            print(f"No scrambles of string '{prompt}' were found in the "
                  f"dictionary.")
        again_outer = True
        while True:
            again_inner = input("Search another string? (y/n) ")\
                .strip().lower()
            if again_inner in ["yes", "y"]:
                break
            elif again_inner in ["no", "n"]:
                again_outer = False
                break
            else:
                print("    Invalid response. Enter 'y' or 'n'.")
        if not again_outer:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
