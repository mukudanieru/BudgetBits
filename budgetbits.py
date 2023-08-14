from data import InformationManager
from pyfiglet import figlet_format
from datetime import datetime
from tabulate import tabulate
import calendar
import sys
import os


def budgetbits_title() -> str:
    """Generate a stylized title for the BudgetBits application using ASCII art."""
    title = figlet_format("BudgetBits", font="slant",
                          justify="center", width=80)
    return title


def clear():
    """
    Clear the terminal screen.

    This function clears the terminal screen based on the operating system.
    It supports both Windows and Unix-based systems (Linux and macOS).
    """
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
        """
        This method simply handle the login process.
        """
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
    """
    AccountValidator:
    A class to handle account validation, login, and registration for the BudgetBits application.

    This class inherits from the Accounts class and provides methods to interact with user accounts,
    including account validation, login, and registration.
    """

    def account_validator(self) -> str:
        """
        Validate accounts, facilitate login, and registration.

        This method provides a user-friendly interface for account validation, login, and registration.
        Users can choose to log in, register, or exit the application.
        """
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
            elif prompt == "E":
                sys.exit()
            else:
                print("Invalid input.")

            self.retry()

    @staticmethod
    def retry() -> None:
        """
        Allow users to retry actions or exit the application.
        """
        while True:
            prompt = input("(Press [B] to back or [E] to exit.) >> ").upper()
            if prompt == "B":
                break
            elif prompt == "E":
                sys.exit()
            else:
                continue

    def login(self) -> str:
        """
        Perform user login and handle exceptions.

        This method guides users through the login process, handles exceptions,
        and returns the username of the successfully logged-in user.
        """
        print(f"\n{'--- Log in to BudgetBits ---':^80}")
        username: str = input("Username: ").strip()
        password: str = input("Password: ").strip()

        # error/exception
        try:
            validation = self.login_account(username, password)
        except ValueError as message:
            print(f"\n{message}")
        else:
            if validation:
                print("Login successfully")
                return username
            else:
                print("Login failed. Incorrect username or password")

    def register(self) -> str:
        """
        Perform user login and handle exceptions.

        This method guides users through the login process, handles exceptions,
        and returns the username of the successfully logged-in user.
        """
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
                    return f"\n{message}"
                else:
                    return "\nRegistration successful!\nYou may login now."
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

        Attributes:
        username (str): The username of the user.
        first (str): The user's first name.
        last (str): The user's last name.
        monthly_budget (int): The user's monthly budget.
        expenses (dict): A dictionary containing user's expenses categorized by type.
        remaining_balance (int): The remaining balance after deducting expenses from the budget.
        date (str): The current date when the BudgetBits instance is created.
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
        """Returns a stylized title for the BudgetBits application using ASCII art."""
        return budgetbits_title()

    @property
    def username(self):
        """Get the username."""
        return self._username

    @username.setter
    def username(self, username: str):
        """Set the username."""
        if not username or username.isspace():
            raise ValueError(
                "Username cannot be empty or consist of only whitespace.")
        self._username = username

    @property
    def first(self):
        """Get the first name."""
        return self._first

    @first.setter
    def first(self, first: str):
        """Set the first name."""
        if not first or first.isspace():
            raise ValueError(
                "First name cannot be empty or consist of only whitespace."
            )
        self._first = first

    @property
    def last(self):
        """Get the last name."""
        return self._last

    @last.setter
    def last(self, last: str):
        """Set the last name."""
        if not last or last.isspace():
            raise ValueError(
                "Last name cannot be empty or consist of only whitespace.")
        self._last = last

    @property
    def monthly_budget(self):
        """Get the monthly budget."""
        return self._monthly_budget

    @monthly_budget.setter
    def monthly_budget(self, monthly_budget: int):
        """Set the monthly budget."""
        # Normal student (high school) - 2,500 to 3,000
        # College student (no dorm) - 5,000 above
        if not isinstance(monthly_budget, int):
            raise ValueError(f"{monthly_budget} should be a integer.")
        elif monthly_budget <= 0:
            raise ValueError(
                f"{monthly_budget} is not an ideal monthly budget. It literally means you are broke."
            )
        self._monthly_budget = monthly_budget

    @property
    def expenses(self):
        """Get the expenses."""
        return self._expenses

    @expenses.setter
    def expenses(self, expenses: dict):
        """Set the expenses."""
        if not isinstance(expenses, dict):
            raise ValueError(
                "Invalid expenses: Expenses must be a dictionary.")
        self._expenses = expenses

    @property
    def remaining_balance(self):
        """Get the remaining balance."""
        return self._remaining_balance

    @remaining_balance.setter
    def remaining_balance(self, remaining_balance: int):
        """Set the remaining balance."""
        if not isinstance(remaining_balance, int):
            raise ValueError(f"{remaining_balance} should be an integer.")
        elif remaining_balance <= 0:
            raise ValueError(
                "It's sad to say that you exceeded your budget for this.")
        self._remaining_balance = remaining_balance

    def display_information(self):
        """
        Display user's personal finance information in a formatted table.

        Returns:
            str: A formatted table displaying personal finance information.
        """

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
        Record an expense entry with category, amount, and notes.

        Args:
            category (str): The category of the expense.
            amount (int): The amount of the expense.
            notes (str): Additional notes for the expense.
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
        """
        Display recorded expenses in a formatted table.

        Returns:
            str: A formatted table displaying recorded expenses.
        """
        if len(self.expenses) <= 0:
            return "\nYou currently have no recorded expenses. To start tracking your spending, use the [A]dd option in the 'Home' section."

        flattened_data = []
        for category, data_date in self.expenses.items():
            for date, transactions in data_date.items():
                for transaction in transactions:
                    flattened_data.append(
                        [category, date, transaction["amount"], transaction["notes"]])

        headers = ["Category", "Date", "Amount", "Notes"]

        return tabulate(flattened_data, headers=headers, tablefmt="grid")

    def monthly_budget_update(self):
        """
        Update the monthly budget if the current day is the first day of the month.

        Returns:
            dict: Updated dictionary of the BudgetBits instance.
        """
        current_day = datetime.strptime(self.date, "%Y-%m-%d").day
        if current_day == 1:
            while True:
                print("\nUpdate your monthly budget.")
                new_budget = int(input("New Monthly Budget: ₱"))
                if new_budget:
                    prompt = input(
                        f"Are you sure about your new monthly budget ₱{new_budget}? (Y/N) ")
                    if prompt == "Y":
                        self.monthly_budget = new_budget
                        self.remaining_balance = new_budget
                        return self.__dict__
                    else:
                        continue
