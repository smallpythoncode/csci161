"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Midterm, Program 2
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program that creates an empty list, and then has a for loop
    that asks the user to put in 5 names, adding each name to the list
    as the program goes (the names are single words). When this is done,
    sort the list alphabetically, and print it out.
"""

names = []
for i in range(1, 6):
    name = input(f"Enter Name {i}: ").strip().title()
    names.append(name)

sorted_names = sorted(names)

print(
    f"\nOriginal list: {names}"
    f"\nSorted list: {sorted_names}"
)

# All work and no play makes Jack a dull boy.
