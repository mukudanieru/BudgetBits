from datetime import datetime
from data import InformationManager
import os
import sys


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
        if not username or username.isspace():
            raise ValueError("Username cannot be empty. Please try again.")
        elif username in Accounts.user_accounts:
            raise ValueError(
                f"The username '{username}' is already taken. Please try a different one.")
        Accounts.user_accounts[username] = password
        self.data_manager.save(Accounts.user_accounts)

    def login_account(self, username: str, password: str) -> bool:
        if len(Accounts.user_accounts) <= 0:
            raise ValueError(
                "There isn't currently any account registered. Create an account first.")
        elif username not in Accounts.user_accounts:
            raise ValueError(
                f"Username {username} is not currently registered. Create an account first.")
        elif username in Accounts.user_accounts and Accounts.user_accounts[username] == password:
            return True
        return False


class BudgetBits:
    def __init__(self, username: str, first: str, last: str, monthly_budget: int, expenses: dict, remaining_balance: int) -> None:
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

    def __str__(self) -> str:
        return f"Current user: {self.username}\nFull name: {self.first + ' ' + self.last}"

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
                "First name cannot be empty or consist of only whitespace.")
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
                f"{monthly_budget} is not an ideal monthly budget. It literally means you are broke.")
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

    def expense_entry(self, category: str, amount: int, notes: str):
        """
        expense_entry (method): This allows the user to categorize their expenses into predefined categories
        such as grocies, utilities, entertainment, transportation, etc.

        Args:
            category (str): 
            amount (str):
            notes (str):
        """
        # Date
        date = str(datetime.now().date())

        if date not in self.expenses:
            self.expenses[date] = dict()

        # subtracting the entry from the remaining balance
        self.remaining_balance -= amount

        if category not in self.expenses:
            self.expenses[date][category] = [
                {"amount": amount, "notes": notes}]
        else:
            self.expenses[date][category] = {"amount": amount, "notes": notes}

        return self.__dict__
