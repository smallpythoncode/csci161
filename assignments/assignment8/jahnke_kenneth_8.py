"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 161, Fall, Lecture Sect 02, Lab Sect L03 (Online)
Assignment 7
Copyright (C) 2022 Kenneth Wayne Jahnke

Classes:
    Account
        - A simple representation of various bank accounts.



=================
# TODO


=================



"""


class Account:
    """A simple representation of various bank accounts.
    """
    def __init__(self, name, savings=None, checking=None, card=None,
                 limit=None):
        """Constructor method.

        :param str name:
            The name of the person who owns the account.
        :param float savings:
            The Savings account balance.
        :param float checking:
            The Savings account balance.
        :param float card:
            The balance of the Card.
        :param int limit:
            The limit on the Card.

        """
        self.name = name
        self.savings = 100.0 if savings is None else float(savings)
        self.checking = 20.0 if checking is None else float(checking)
        self.card = 10.0 if card is None else float(card)
        self.limit = 50 if limit is None else int(limit)

    @staticmethod
    def balance_format(balance, max_figures=10):
        """Formats balance for printing.

        :param float balance:
            The balance for which the number of digits is calculated.
        :param int max_figures:
            With a fixed column width, the dollar figure (and only the
            dollar figure) is limited to 10 digits (by default) so
            displayBalance() is printed neatly. If this number of digits
            is exceeded, "CONTACT BANK" is printed. Let this indicate to
            the account holder that their balance is out of the bounds
            required by the account type.
        :return:
            A formatted balance string (e.g., '$420.69' or 'CONTACT
            BANK' if the account balance is out of the bounds specified
            by the account type (a greater-than-10-digit dollar figure.
        :rtype: str
        """
        digits = str(balance)
        dollars_cents = digits.split(".")

        if dollars_cents[0][0] == "-":  # a dollar amount
            if len(dollars_cents[0][1:]) > max_figures:
                return "CONTACT BANK"  # too much/too little $ for acct type
        elif len(dollars_cents[0]) > max_figures:
            return "CONTACT BANK"  # too much/too little $ for acct type

        if len(dollars_cents[1]) != 2:  # cents as 2 digits
            dollars_cents[1] = dollars_cents[1] + "0"
            # cents figure will ever be 1 or 2 digits
            # this is ensured by Account.cashServices()

        return "$" + dollars_cents[0] + "." + dollars_cents[1]

    def displayBalance(self):
        """Prints the current and available balances of the accounts.

        displayBalance method name (camelCase) used as specified by
        assignment instructions. This is in opposition to PEP 8
        convention of snake_case for method names.

        ..note ::
            Mimics the check_balance Account class method from
            Assignment 7. Assignment instructions specify that
            displayBalance should print using center alignment.
            check_balance specified different parts. Although assignment
            instructions indicate significant whitespace between "$"
            and the dollar figure, this implementation eliminates that
            whitespace for ease of implementation and aesthetics.

        :return: None
        """
        savings_available = 10 + self.savings
        checking_available = self.checking
        card_available = self.limit - self.card

        _savings = "Savings"
        _checking = "Checking"
        _card = "Card"

        buffer = 4
        _account_type = "Acc-Type"
        left_column = len(max([_savings, _checking, _card, _account_type],
                              key=lambda i: len(i)))
        _account_balance = "Account Balance"
        middle_column = len(_account_balance)
        _available_balance = "Available Balance"
        right_column = len(_available_balance)
        total_width = left_column + middle_column + right_column + buffer * 2

        # Interesting bit on formatting strings w/ center alignment
        # https://stackoverflow.com/questions/13383244/python-center-string-using-format-specifier

        owner = f"Account owner's name: {self.name}"
        print(f"{owner:^{total_width}}")

        print(
            f"{_account_type:^{left_column}}" + " " * buffer +
            f"{_account_balance:^{middle_column}}" + " " * buffer +
            f"{_available_balance:^{right_column}}"
        )
        print(
            f"{_savings:^{left_column}}" + " " * buffer +
            f"{self.balance_format(self.savings):^{middle_column}}"
            + " " * buffer +
            f"{self.balance_format(savings_available):^{right_column}}"
        )
        print(
            f"{_checking:^{left_column}}" + " " * buffer +
            f"{self.balance_format(self.checking):^{middle_column}}"
            + " " * buffer +
            f"{self.balance_format(checking_available):^{right_column}}"
        )
        print(
            f"{_card:^{left_column}}" + " " * buffer +
            f"{self.balance_format(self.card):^{middle_column}}"
            + " " * buffer +
            f"{self.balance_format(card_available):^{right_column}}"
        )

    def cashServices(self):
        """Prints the current and available balances of the accounts.

        cashServices method name (camelCase) used as specified by
        assignment instructions. This is in opposition to PEP 8
        convention of snake_case for method names.

        """
        pass
        # TODO


def menu(account):
    """A menu with options to check balance or exit the menu.

    :param account:
        This must be an instance of the Account class.
    :return: None
    """
    while True:
        print("\nMenu:",
              "    Option 1: Display Balance",
              "    Option 2: Cash Services",
              "    Option 3: Exit",
              sep="\n")
        prompt = input("Enter an option number: ").strip()

        if prompt == "3":
            print("\nGoodbye.")
            break
        elif prompt == "1":
            print()
            account.displayBalance()
        elif prompt == "2":
            print()
            account.cashServices()
        else:
            print("    That is not a valid menu option.")


def main():
    # current version does not check for name plausibility
    # person1 = input("Please enter your name: ").strip().title() # FIXME temp
    person1 = "butch"
    account1 = Account(person1)

    menu(account1)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

# TODO https://stackoverflow.com/questions/41383787/round-down-to-2-decimal-in-python
