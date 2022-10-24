"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Midterm, Program 1
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program that uses the input command to have the user enter
    an integer number. Recast the input string to an integer and a
    floating point number. Print the number as a string, as an integer,
    and as a float. Use the type() function and the id() function to
    print out the type and id of each of the items printed.
"""

while True:
    user_string = input("Enter an integer: ").strip()
    try:
        user_int = int(user_string)
    except ValueError:
        print(f"{user_string} is not an integer.")
    else:
        break

user_float = float(user_int)

print(
    f"\nUser input as string: {user_string}\n"
    f"Type: {type(user_string)}\n"
    f"String ID: {id(user_string)}"
)
print(
    f"\nUser input converted to integer: {user_int}\n"
    f"Type: {type(user_int)}\n"
    f"Integer ID: {id(user_int)}"
)
print(
    f"\nUser input converted to float: {user_float}\n"
    f"Type: {type(user_float)}\n"
    f"Float ID: {id(user_float)}"
)

# All work and no play makes Jack a dull boy.
