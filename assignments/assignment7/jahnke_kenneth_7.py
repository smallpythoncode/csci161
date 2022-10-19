"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 7
Copyright (C) 2022 Kenneth Wayne Jahnke

Classes:
    Account
        - A simple representation of various bank accounts.

Functions:
    check_balance(account)
        - A menu with options to check balance or exit the menu.

"""


class Account:
    """A simple representation of various bank accounts.
    """
    def __init__(self, savings, checking, card, limit, name):
        """Constructor method.

        :param float savings:
            The Savings account balance.
        :param float checking:
            The Savings account balance.
        :param float card:
            The balance of the Card.
        :param int limit:
            The limit on the Card.
        :param str name:
            The name of the person who owns the account.
        """
        self.savings = 100.0
        self.checking = 20.0
        self.card = 10.0
        self.limit = 50
        self.name = name

    def check_balance(self):
        """Prints the current and available balances of the accounts.

        :return: None
        """
        savings_available = 10 + self.savings
        checking_available = self.checking
        card_available = self.limit - self.card

        buffer = 2
        left_column = len(max(["Savings", "Checking", "Card"], key=lambda i:
                              len(i)))
        account_balance = "Account Balance"
        middle_column = len(account_balance)
        available_balance = "Available Balance"
        right_column = len(available_balance)

        print(f"Account owner's name: {self.name}")
        print(" " * (left_column + buffer) + account_balance +
              " " * buffer + available_balance)
        print("Savings".ljust(left_column + buffer) +
              f"${self.savings:>{middle_column - 1 }.2f}" +
              " " * buffer +
              f"${savings_available:>{right_column - 1 }.2f}")
        print("Checking".ljust(left_column + buffer) +
              f"${self.checking:>{middle_column - 1 }.2f}" +
              " " * buffer +
              f"${checking_available:>{right_column - 1 }.2f}")
        print("Card".ljust(left_column + buffer) +
              f"${self.card:>{middle_column - 1 }.2f}" +
              " " * buffer +
              f"${card_available:>{right_column - 1 }.2f}")


def menu(account):
    """A menu with options to check balance or exit the menu.

    :param account:
        This must be an instance of the Account class to call
        check_balance().
    :return: None
    """
    while True:
        print("\nMenu:",
              "    Option 1: Check Balance",
              "    Option 2: Exit",
              sep="\n")
        prompt = input("Enter an option number: ").strip()

        if prompt == "2":
            print("\nGoodbye.")
            break
        elif prompt == "1":
            print()
            account.check_balance()
        else:
            print("    That is not a valid menu option.")


def main():
    # current version does not check for name plausibility
    person1 = input("Please enter your name: ").strip().title()
    account1 = Account(100.0, 20.0, 10.0, 50, person1)

    menu(account1)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
