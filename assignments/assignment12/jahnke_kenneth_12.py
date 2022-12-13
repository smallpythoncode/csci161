"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 12
Copyright (C) 2022 Kenneth Wayne Jahnke

"""


class Node:
    def __init__(self, data=None, next_ref=None):
        self.data = data
        self.next_ref = next_ref


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty.")
            return  # no need to evaluate additional conditions

        i = self.head
        printer = []

        while i:
            printer.append(i.data)
            i = i.next_ref

        for j in printer:
            print(j)

    def search(self, target):
        i = self.head
        found = False

        while i:
            if i.data == target:
                found = True
                break
            i = i.next_ref

        if found:
            return f"{target} is in the list!"
        else:
            return f"{target} is NOT in the list."


def main():
    linked_list = LinkedList()
    print_menu = True

    while True:
        menu = "\nMenu:\n" \
            "1. Add to list (at head)\n" \
            "2. Display list (last in, first out)\n" \
            "3. Search list\n" \
            "4. Exit"

        if print_menu:
            print(menu)

        prompt = input("Select an option number: ").strip()
        if prompt == "4":
            print("Goodbye.")
            break

        elif prompt == "1":
            while True:
                num = input("Integer to add: ").strip()
                try:
                    num = int(num)
                except ValueError:
                    print("    Only integers may be added to the list.")
                    continue
                linked_list.insert_at_head(num)
                again = False
                while True:
                    again_prompt = input("Add another integer? (y/n): ")\
                        .strip().lower()
                    if again_prompt not in ["y", "yes", "n", "no"]:
                        print("    Invalid response.")
                        continue
                    elif again_prompt in ["y", "yes"]:
                        again = True
                        break
                    else:
                        break
                if not again:
                    print_menu = True
                    break

        elif prompt == "2":
            linked_list.print_linked_list()
            print_menu = True

        elif prompt == "3":
            while True:
                search_prompt = input("Integer to search for: ").strip()
                try:
                    search_prompt = int(search_prompt)
                except ValueError:
                    print("    Integers are the only data types in the list.")
                    continue
                print(linked_list.search(search_prompt))
                again = False
                while True:
                    again_prompt = input(
                        "Search for another integer? (y/n): "
                    ).strip().lower()
                    if again_prompt not in ["y", "yes", "n", "no"]:
                        print("    Invalid response.")
                        continue
                    elif again_prompt in ["y", "yes"]:
                        again = True
                        break
                    else:
                        break
                if not again:
                    print_menu = True
                    break

        else:
            print(f"    {prompt} is not a valid option.")
            print_menu = False


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
