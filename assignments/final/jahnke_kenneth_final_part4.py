"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Final Exam, Part 4
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program that contains a class called Car. The Car class
    should have a constructor which defines a Car object with the
    following attributes: make, model, and year. Define a second class,
    which is derived from Car, called Entry, but adds attributes: driver
    and number. The derived class should also have a printEntry method
    which prints out the make, model, year, driver, and number of an
    Entry object. Finally, write a section of the program that creates a
    list of 3 Entry objects.  For each of these objects, prompt the user
    for the make, model, year, driver, and number.  Finally print out
    this list.

Classes:
    Car:
        - Representation of a car.
    Entry(Car):
        - A car to be entered into a race.
"""

import datetime as dt


class Car:
    """Representation of a car.

    :param str make:
        The make of the car.
    :param str model:
        The model of the car.
    :param int year:
        The car's year of manufacture.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Entry(Car):
    """A car to be entered into a race.

    :param str driver:
        The driver of the car.
    :param int number:
        The car's racing number.
    """
    def __init__(self, make, model, year, driver, number):
        super(Entry, self).__init__(make, model, year)
        self.driver = driver
        self.number = number

    @classmethod
    def user_input(cls):
        """Prompt the user for attributes for Entry.

        :return:
            Attributes for an Entry object.
        """
        min_year = 1886
        max_year = dt.date.today().year + 1
        print(
            "CARefully enter the data for each of the following prompts."
        )
        make = input("Make: ").strip().title()
        model = input("Model: ").strip().title()
        while True:
            year = input("Year: ").strip()
            try:
                year = int(year)
            except ValueError:
                print("    The years of vehicle must be expressed as "
                      "integers.")
            else:
                if year < min_year:
                    print(f"    Easy there, time traveller. The first car "
                          f"wasn't invented until {min_year}.")
                elif year > max_year:
                    print(f"    The {max_year + 1} models aren't even out "
                          f"yet, so why did you enter {year}?")
                else:
                    break
        driver = input("Driver: ").strip().title()
        while True:
            number = input("Number (0-99): ").strip()
            try:
                number = int(number)
            except ValueError:
                print("    Driver numbers must be expressed as integers.")
            else:
                if number in range(0, 99+1):
                    break
                else:
                    print("    The number entered is out of range.")
        return cls(make, model, year, driver, number)

    # def print_entry(self):
    # PEP8
    def printEntry(self):
        """Prints the attributes of Entry object.

        :rtype: None
        """
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Driver: {self.driver}")
        print(f"Number: {self.number}")


def main():
    entries = []
    while len(entries) < 3:
        print(f"\nENTRY {len(entries) + 1}")
        entry = Entry.user_input()
        entries.append(entry)

    print(
        "\nVerbatim instructions:\n"
        "\"Finally, write a section of the program that creates a list of 3\n"
        "Entry objects. For each of these objects, prompt the user for the\n"
        "the make, model, year, driver, and number. Finally print out this\n"
        "list.\"\n"
        "Printing the list of Entry objects:\n",
        entries,
        "\n"
    )

    entry_num = 1
    for entry in entries:
        print(f"---Printing details of ENTRY {entry_num}---")
        entry.printEntry()
        entry_num += 1


if __name__ == "__main__":
    # x = dt.date.today().year + 1
    # print(x)
    # print(type(x))
    # x = Entry.user_input()
    # print(x)
    # print(x.make)
    main()

# All work and no play makes Jack a dull boy.
