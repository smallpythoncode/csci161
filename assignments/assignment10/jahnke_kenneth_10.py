"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 10
Copyright (C) 2022 Kenneth Wayne Jahnke

"""


class Person:
    """A representation of a student."""
    def __init__(self, name, id_num, address, phone_num, email):
        self.name = name
        self.id_num = id_num
        self.address = address
        self.phone_num = phone_num
        self.email = email


class Student(Person):
    """A representation of university student.
    """
    def __init__(self, name, id_num, address, phone_num, email, class_status,
                 major):
        super(Student, self).__init__(name, id_num, address, phone_num, email)
        self.class_status = class_status
        self.major = major

    @classmethod
    def user_input(cls):
        print(
            "Enter the data for each of the following prompts.\n"
            "NOTE: The data will be recorded exactly as entered.\n"
            "    Please take care to enter data correctly with regards to\n"
            "    capitalization, punctuation, etc.\n"
        )
        name = input("Name: ")
        id_num = input("ID Number: ")
        address = input("Address: ")
        phone_num = input("Phone Number: ")
        email = input("Email: ")
        while True:
            cs_prompt = input("Class Status: ").upper()  # class status prompt
            if cs_prompt == "U":
                class_status = "undergraduate"
                break
            elif cs_prompt == "G":
                class_status = "graduate"
                break
            else:
                print(f"{cs_prompt} is not a valid entry.\n"
                      "    Enter 'U' for undergraduate or 'G' for graduate.")
        major = input("Major: ")
        return cls(name, id_num, address, phone_num, email, class_status,
                   major)


class Employee(Person):
    """A representation of a university employee.
    """
    def __init__(self, name, id_num, address, phone_num, email,
                 date_of_joining, department, salary):
        super(Employee, self).__init__(name, id_num, address, phone_num, email)
        self.date_of_joining = date_of_joining
        self.department = department
        self.salary = salary


class Faculty(Employee):
    """A representation of a university faculty member.
    """
    def __init__(self, name, id_num, address, phone_num, email,
                 date_of_joining, department, salary, title, room_no):
        super(Faculty, self).__init__(name, id_num, address, phone_num,
                                      email, date_of_joining, department,
                                      salary)
        self.title = title
        self.room_no = room_no

    @classmethod
    def user_input(cls):
        print(
            "Enter the data for each of the following prompts.\n"
            "NOTE: The data will be recorded exactly as entered.\n"
            "    Please take care to enter data correctly with regards to\n"
            "    capitalization, punctuation, etc.\n"
        )
        name = input("Name: ")
        id_num = input("ID Number: ")
        address = input("Address: ")
        phone_num = input("Phone Number: ")
        email = input("Email: ")
        date_of_joining = input("Date of Joining (YYYYMMDD): ")
        department = input("Department: ")
        salary = input("Salary (as integer): ")
        title = input("Title: ")
        room_no = input("Room Number: ")
        return cls(name, id_num, address, phone_num, email, date_of_joining,
                   department, salary, title, room_no)


class Staff(Employee):
    """A representation of a university staff member.
    """
    def __init__(self, name, id_num, address, phone_num, email,
                 date_of_joining, department, salary, title):
        super(Staff, self).__init__(name, id_num, address, phone_num,
                                    email, date_of_joining, department,
                                    salary)
        self.title = title

    @classmethod
    def user_input(cls):
        print(
            "Enter the data for each of the following prompts.\n"
            "NOTE: The data will be recorded exactly as entered.\n"
            "    Please take care to enter data correctly with regards to\n"
            "    capitalization, punctuation, etc.\n"
        )
        name = input("Name: ")
        id_num = input("ID Number: ")
        address = input("Address: ")
        phone_num = input("Phone Number: ")
        email = input("Email: ")
        date_of_joining = input("Date of Joining (YYYYMMDD): ")
        department = input("Department: ")
        salary = input("Salary (as integer): ")
        title = input("Title: ")
        return cls(name, id_num, address, phone_num, email, date_of_joining,
                   department, salary, title)


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


def add_student(students):
    """Add a student's information to students.

    :param list students:
        All the students.
    :rtype: None
    """
    student = Student.user_input()
    student_dict = {
        "name": student.name,
        "id": student.id_num,
        "address": student.address,
        "phone_num": student.phone_num,
        "email": student.email,
        "class_status": student.class_status,
        "major": student.major
    }

    student_info = list(student_dict.values())
    students.append(student_info)


def add_faculty(faculty):
    """Add a faculty member's information to faculty.

    :param list faculty:
        All the faculty.
    :rtype: None
    """
    faculty_member = Faculty.user_input()
    faculty_member_dict = {
        "name": faculty_member.name,
        "id": faculty_member.id_num,
        "address": faculty_member.address,
        "phone_num": faculty_member.phone_num,
        "email": faculty_member.email,
        "date_joined": faculty_member.date_of_joining,
        "department": faculty_member.department,
        "salary": faculty_member.salary,
        "title": faculty_member.title,
        "room_no": faculty_member.room_no
    }

    faculty_member_info = list(faculty_member_dict.values())
    faculty.append(faculty_member_info)


def add_staff(staff):
    """Add a staff member's information to staff.

    :param list staff:
        All the staff.
    :rtype: None
    """
    staff_member = Staff.user_input()
    staff_member_dict = {
        "name": staff_member.name,
        "id": staff_member.id_num,
        "address": staff_member.address,
        "phone_num": staff_member.phone_num,
        "email": staff_member.email,
        "date_joined": staff_member.date_of_joining,
        "department": staff_member.department,
        "salary": staff_member.salary,
        "title": staff_member.title
    }

    staff_member_info = list(staff_member_dict.values())
    staff.append(staff_member_info)


def main():
    student_file = "Student.txt"
    faculty_file = "Faculty.txt"
    staff_file = "Staff.txt"

    _student_clear = open(student_file, "w")
    _student_clear.close()
    _faculty_clear = open(faculty_file, "w")
    _faculty_clear.close()
    _staff_clear = open(staff_file, "w")
    _staff_clear.close()

    student_all = []
    faculty_all = []
    staff_all = []

    menu_options = {
        "1": {"prompt": "Add a Student's Details",
              "trigger": add_student},
        "2": {"prompt": "Add a Faculty Member's Details",
              "trigger": add_faculty},
        "3": {"prompt": "Add a Staff Member's Details",
              "trigger": add_staff},
        "4": {"prompt": "Exit", "trigger": exit_func}
    }

    while True:
        selected_option = menu(menu_options)
        trigger = menu_options[selected_option]["trigger"]
        try:
            if trigger is add_student:
                trigger(student_all)
            elif trigger is add_faculty:
                trigger(faculty_all)
            elif trigger is add_staff:
                trigger(staff_all)
            else:
                trigger()
        except LoopBreak:
            print("Goodbye.")
            break

    with open(student_file, "a", newline="") as f_student:
        for student in student_all:
            line = " ".join(student) + "\n"
            f_student.write(line)
    with open(faculty_file, "a", newline="") as f_faculty:
        for fm in faculty_all:  # faculty member
            line = " ".join(fm) + "\n"
            f_faculty.write(line)
    with open(staff_file, "a", newline="") as f_staff:
        for sm in staff_all:  # staff member
            line = " ".join(sm) + "\n"
            f_staff.write(line)






if __name__ == "__main__":
    # x = Student()
    # # non-special methods
    # reg_attr = [a for a in dir(x) if not a.startswith("__")]
    # print(reg_attr)

    # studentt = []
    # print(studentt)
    # add_student(studentt)
    # print(studentt)
    # poop = " ".join(studentt[0])
    # print(poop)

    main()


# All work and no play makes Jack a dull boy.
