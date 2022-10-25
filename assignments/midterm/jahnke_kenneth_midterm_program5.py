"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Midterm, Program 2
Copyright (C) 2022 Kenneth Wayne Jahnke

Instructions:
    Write a program with a class definition 'Aircraft'. The constructor
    should take in arguments for tail_number, latitude, longitude,
    altitude, heading, and speed. These should be stored in a
    dictionary. The key is the parameter name (e.g., 'tail_number'), and
    the value will be the argument passed to the constructor (e.g.,
    'N51123ND'). Also have a method definition in the class called
    'print_plane', which prints out all of these values for a given
    instantiation of the class.  In the main section of the program,
    have the user enter the arguments listed above, call the
    constructor, and make three different instantiations of the class,
    called plane1, plane2, and plane3.  Print the contents of these
    three objects by calling the 'print_plane' method from them.

Classes:
    Aircraft
        - A representation a plane in flight.
"""


class Aircraft:
    """A representation a plane in flight."""

    def __init__(self, tail_number, latitude, longitude, altitude, heading,
                 speed):
        """Constructor method.

        .. note::
            No format checking (e.g., speed in MPH) or error handling
            (e.g., impossible latitude/longitude) is implemented in this
            function's current version as the midterm instructions
            don't require them or dictate specific formats/data types.

        :param str tail_number: The tail number of the aircraft.
        :param str latitude: The latitude of the aircraft.
        :param str longitude: The longitude number of the aircraft.
        :param str altitude: The altitude of the aircraft.
        :param str heading: The tail number of the aircraft.
        :param str speed: The tail number of the aircraft.
        """
        self.data = {
            "tail_number": tail_number,
            "latitude": latitude,
            "longitude": longitude,
            "altitude": altitude,
            "heading": heading,
            "speed": speed
        }

    def print_plane(self):
        """Prints the data for the aircraft.

        :return: None
        """
        for key, value in self.data.items():
            print(f"{key}: {value}")


def main():
    print("You will be asked for data for 3 airplanes.")

    aircraft = {1: {}, 2: {}, 3: {}}
    for i in range(1, 4):
        aircraft[i]["tail_number"] = input(f"Plane {i} tail number: ").strip()
        aircraft[i]["latitude"] = input(f"Plane {i} latitude: ").strip()
        aircraft[i]["longitude"] = input(f"Plane {i} longitude: ").strip()
        aircraft[i]["altitude"] = input(f"Plane {i} altitude: ").strip()
        aircraft[i]["heading"] = input(f"Plane {i} heading: ").strip()
        aircraft[i]["speed"] = input(f"Plane {i} speed: ").strip()

    plane1 = Aircraft(
        aircraft[1]["tail_number"],
        aircraft[1]["latitude"],
        aircraft[1]["longitude"],
        aircraft[1]["altitude"],
        aircraft[1]["heading"],
        aircraft[1]["speed"]
    )
    plane2 = Aircraft(
        aircraft[2]["tail_number"],
        aircraft[2]["latitude"],
        aircraft[2]["longitude"],
        aircraft[2]["altitude"],
        aircraft[2]["heading"],
        aircraft[2]["speed"]
    )
    plane3 = Aircraft(
        aircraft[3]["tail_number"],
        aircraft[3]["latitude"],
        aircraft[3]["longitude"],
        aircraft[3]["altitude"],
        aircraft[3]["heading"],
        aircraft[3]["speed"]
    )

    print("\nPLANE 1")
    plane1.print_plane()
    print("\nPLANE 2")
    plane2.print_plane()
    print("\nPLANE 3")
    plane3.print_plane()


if __name__ == '__main__':
    main()

# All work and no play makes Jack a dull boy.
