from data import InformationManager
from pyfiglet import figlet_format
from datetime import datetime
from tabulate import tabulate
import calendar
import sys
import os


def budgetbits_title():
    title = figlet_format("BudgetBits", font="slant",
                          justify="center", width=80)
    return title


def clear():
    # clear terminal for windows os
    if os.name == "nt":
        os.system("cls")
    # clear terminal for unix-based systems (Linux and macOS)
    else:
        os.system("clear")


class Accounts:
    user_accounts = {}

    def __init__(self) -> None:
        """
        Accounts: a class to handle user accounts.
        A login and register system.
        """
        file_path = os.path.join("data", "accounts.json")
        self.data_manager = InformationManager(file_path)
        Accounts.user_accounts.update(self.data_manager.retrieve())

    def __str__(self) -> str:
        """
        This method simply returns the number
        of users.
        """
        return f"Current users: {len(Accounts.user_accounts)}"

    def register_account(self, username: str, password: str) -> None:
        """
        This method simply handle the registration process.
        """
        # username
        if not username or username.isspace():
            raise ValueError("Username cannot be empty. Please try again.")
        elif username in Accounts.user_accounts:
            raise ValueError(
                f"The username '{username}' is already taken. Please try a different one."
            )

        # password
        if not password or password.isspace():
            raise ValueError("Password cannot be empty. Try a strong one.")
        Accounts.user_accounts[username] = password
        self.data_manager.save(Accounts.user_accounts)

    def login_account(self, username: str, password: str) -> bool:
        if len(Accounts.user_accounts) <= 0:
            raise ValueError(
                "There isn't currently any account registered. Create an account first."
            )
        elif not username or username.isspace():
            raise ValueError("Username cannot be empty. Please try again.")
        elif username not in Accounts.user_accounts:
            raise ValueError(
                f"Username '{username}' is not currently registered. Create an account first."
            )
        elif (
            username in Accounts.user_accounts
            and Accounts.user_accounts[username] == password
        ):
            return True
        return False


class AccountValidator(Accounts):
    def account_validator(self) -> str:
        while True:
            clear()
            print(budgetbits_title())
            print(f"{'[L]ogin | [R]egister | [E]xit':^80}")
            prompt = input(" >> ").upper()
            if prompt == "L":
                if validation := self.login():
                    return validation
            elif prompt == "R":
                print(self.register())
                prompt = input("(Press [B] to back.) >> ").upper()
                if prompt == "B":
                    continue
                sys.exit()
            elif prompt == "E":
                sys.exit()
            else:
                print("Invalid input.")

            prompt = input("(Press [R] to retry.) >> ").upper()
            if prompt == "R":
                continue
            sys.exit()

    def login(self):
        print(f"\n{'--- Logging in an account ---':^80}")
        username: str = input("Username: ").strip()
        password: str = input("Password: ").strip()

        # error/exception
        try:
            validation = self.login_account(username, password)
        except ValueError as message:
            print(message)
        else:
            if validation:
                print("Login successfully")
                return username
            else:
                print("Login failed. Incorrect username or password")

    def register(self):
        while True:
            clear()
            print(budgetbits_title())
            print(f"{'[L]ogin | [R]egister | [E]xit':^80}")
            print(f"\n{'--- Register an account ---':^80}")
            username: str = input("Username: ").strip()
            password: str = input("Password: ").strip()

            prompt = input(
                "\nAre you sure about your username and password? (Y/N): ").upper()
            if prompt == "Y":
                # error/exception
                try:
                    self.register_account(username, password)
                except ValueError as message:
                    return message
                else:
                    return "Registration successful!\nYou may login now."
            elif prompt == "N":
                continue


class BudgetBits:
    def __init__(
        self,
        username: str,
        first: str,
        last: str,
        monthly_budget: int,
        expenses: dict,
        remaining_balance: int,
    ) -> None:
        """
        BudgetBits is a user-friendly and intuitive expense tracker designed to simplify personal finance
        management. BudgetBits empowers users to take control of their spending, set financial goals, and
        make informed budgeting decisions.
        """
        # user's personal information
        self.username = username
        self.first = first
        self.last = last
        self.monthly_budget = monthly_budget

        # user's expenses
        self.expenses = expenses
        self.remaining_balance = remaining_balance

        # others
        self.date = str(datetime.now().date())

    def __str__(self) -> str:
        return budgetbits_title()

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not username or username.isspace():
            raise ValueError(
                "Username cannot be empty or consist of only whitespace.")
        self._username = username

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        if not first or first.isspace():
            raise ValueError(
                "First name cannot be empty or consist of only whitespace."
            )
        self._first = first

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        if not last or last.isspace():
            raise ValueError(
                "Last name cannot be empty or consist of only whitespace.")
        self._last = last

    @property
    def monthly_budget(self):
        return self._monthly_budget

    @monthly_budget.setter
    def monthly_budget(self, monthly_budget):
        """
        Normal student (high school) - 2,500 to 3,000
        College student (no dorm) - 5,000 above
        """
        if not isinstance(monthly_budget, int):
            raise ValueError(f"{monthly_budget} should be a integer.")
        elif monthly_budget <= 0:
            raise ValueError(
                f"{monthly_budget} is not an ideal monthly budget. It literally means you are broke."
            )
        self._monthly_budget = monthly_budget

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, expenses):
        if not isinstance(expenses, dict):
            raise ValueError(
                "Invalid expenses: Expenses must be a dictionary.")
        self._expenses = expenses

    @property
    def remaining_balance(self):
        return self._remaining_balance

    @remaining_balance.setter
    def remaining_balance(self, remaining_balance):
        if not isinstance(remaining_balance, int):
            raise ValueError(f"{remaining_balance} should be an integer.")
        elif remaining_balance <= 0:
            raise ValueError(
                "It's sad to say that you exceeded your budget for this.")
        self._remaining_balance = remaining_balance

    def display_information(self):
        date_object = datetime.strptime(self.date, "%Y-%m-%d")
        month = calendar.month_name[date_object.month]
        headers = ["PERSONAL INFORMATION", f"MONTH: {month}"]
        personal_information = {
            "USERNAME:": self.username,
            "FULL NAME:": self.first + " " + self.last,
            f"CURRENT BUDGET ({month})": f"₱{self.monthly_budget:,}",
            f"TOTAL EXPENSES ({month})": f"₱{self.monthly_budget - self.remaining_balance:,}",
            f"REMAINING BALANCE ({month})": f"₱{self.remaining_balance:,}",
        }

        data = [[key, value] for key, value in personal_information.items()]
        return tabulate(data, headers=headers, tablefmt="heavy_outline")

    def expense_entry(self, category: str, amount: int, notes: str):
        """
        expense_entry (method): This allows the user to categorize their expenses into predefined categories
        such as grocies, utilities, entertainment, transportation, etc.

        Args:
            category (str):
            amount (str):
            notes (str):
        """
        if category not in self.expenses:
            self.expenses[category] = dict()

        # subtracting the entry from the remaining balance
        self.remaining_balance -= amount

        if self.date not in self.expenses[category]:
            self.expenses[category][self.date] = [
                {"amount": amount, "notes": notes}]
        else:
            self.expenses[category][self.date].append(
                {"amount": amount, "notes": notes})

        return self.__dict__

    def display_expenses(self):
        if len(self.expenses) <= 0:
            return "You haven't added any expenses, Press [A]dd to add expenses at home section."

        flattened_data = []
        for category, data_date in self.expenses.items():
            for date, transactions in data_date.items():
                for transaction in transactions:
                    flattened_data.append(
                        [category, date, transaction["amount"], transaction["notes"]])

        headers = ["Category", "Date", "Amount", "Notes"]

        return tabulate(flattened_data, headers=headers, tablefmt="grid")

    def monthly_budget_update(self, monthly_update):
        current_day = 1  # datetime.strptime(self.date, "%Y-%m-%d").day
        if current_day == 1:
            new_budget = monthly_update()
            self.monthly_budget = new_budget
            self.remaining_balance = new_budget

            return self.__dict__
