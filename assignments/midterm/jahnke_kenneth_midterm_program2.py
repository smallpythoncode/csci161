"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Midterm, Program 1
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program that imports the math module.  Prompt the user to
    enter an integer value, the number of degrees in an angular measure.
    Use functions from the math module to convert the degrees into
    radians, and to calculate the cosine of the resulting radians.
    Print out the degrees, radians, and the cosine value.
"""

import math


print("This program will convert a degree value (as an integer) to radians\n"
      "and calculate the cosine of the resulting radians.")

while True:
    degrees = input("Enter an angular measure in degrees: ").strip()
    try:
        degrees = int(degrees)
    except ValueError:
        print("Enter degrees as an integer.")
    else:
        break

radians = math.radians(degrees)
cosine = math.cos(radians)

print(
    f"\nDegrees: {degrees}"
    f"\nRadians: {radians:.4f} or {radians / math.pi:.4f}π"
)
