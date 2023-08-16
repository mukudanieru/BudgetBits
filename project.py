from budgetbits import AccountValidator, BudgetBits, clear
from data import InformationManager
import sys
import os


def main():
    """
    The main function of the BudgetBits expense tracker.

    This function orchestrates the login and registration process, handles user interactions,
    and manages the overall flow of the BudgetBits application.
    """

    # check the registered users
    info = InformationManager(os.path.join("data", "data.json"))
    users = info.retrieve()

    # login process
    username = current_account()
    clear()

    if username not in users:
        user = register_user(username)
        users[username] = user.__dict__
        info.save(users)
        print(f"\n{f'Welcome to BudgetBits, {username}!':^80}")

    else:
        user = existing_user(users[username])

        clear()
        print(f"\n{f'Welcome back to BudgetBits, {username}!':^80}")

        if update := user.monthly_budget_update(monthly_update):
            users[username] = update
            info.save(users)

    while True:
        print(user)
        print(f"\n{'[P]ersonal | [A]dd | [S]how | [E]xit':^80}\n")
        prompt = input(" >> ").upper()
        if prompt == "P":
            print(user.display_information())
        elif prompt == "A":
            if expense_added := adding_expense(user):
                users[username] = expense_added
                info.save(users)
        elif prompt == "S":
            print(user.display_expenses())
        elif prompt == "E":
            sys.exit()
        else:
            print("\nInvalid input.")

        retry('B', 'back')


def monthly_update():
    while True:
        print("\nWelcome to a new month!\nTake a moment to update your monthly budget.\n")
        while True:
            new_budget: int = validate_amount(input("New Monthly Budget: ₱"))
            if new_budget:
                break

        prompt = input(
            f"Are you sure about your new monthly budget ₱{new_budget}? (Y/N) ")
        if prompt == "Y":
            clear()
            return new_budget
        else:
            clear()


def retry(letter: str = 'R', message: str = 'retry'):
    """
    Handle user retry choice in the BudgetBits application.

    This function prompts the user to choose between returning to a specific action
    (e.g., back to the previous menu) or exiting the application.

    Args:
        letter (str, optional): The letter corresponding to the action (e.g., 'B' for back).
            Defaults to 'R'.
        message (str, optional): A message describing the action (e.g., 'back').
            Defaults to 'retry'.
    """
    while True:
        prompt = input(
            f"(Press [{letter}] to {message} or [E] to exit.) >> ").upper()
        if prompt == f"{letter}":
            clear()
            return True
        elif prompt == "E":
            sys.exit()
        else:
            continue


def current_account():
    """
    Perform account validation or registration for the BudgetBits application.

    This function interacts with the AccountValidator class to either validate an existing user's login
    or facilitate user registration, ensuring the user's account is properly managed.

    Returns:
        str: The username of the validated or registered user.
    """
    account_manager = AccountValidator()
    return account_manager.account_validator()


def existing_user(data: dict):
    """
    Create a BudgetBits instance for an existing user using provided data.

    This function initializes a BudgetBits object for an existing user using the user's saved data,
    enabling seamless interaction with the user's expense tracking and management.

    Args:
        data (dict): User data containing relevant information.
    """
    return BudgetBits(
        data["_username"],
        data["_first"],
        data["_last"],
        data["_monthly_budget"],
        data["_expenses"],
        data["_remaining_balance"],
        data["last_updated"]
    )


def register_user(username: str):
    """
    Perform user registration and setup of personal information for the BudgetBits application.

    This function guides the user through the process of providing personal information, including
    first and last names, as well as setting a monthly budget. Once the information is validated, a new
    BudgetBits instance is created for the registered user.

    Args:
        username (str): The username for the new user.
    """
    while True:
        clear()
        print(f"Personal information setup for {username}.")
        try:
            first, last = get_valid_names()
            while True:
                monthly_budget: int = validate_amount(
                    input("Monthly budget (for this month): ₱"))
                if monthly_budget:
                    break
            print(
                "\n[Y]es - (to continue) | [N]o - (to provide your personal information again)")
            prompt = input(
                "Do you want to proceed with this personal information? (Y/N) ").upper()
            if prompt == "Y":
                clear()
                return BudgetBits(username, first, last, monthly_budget, {}, monthly_budget, None)
            elif prompt == "N":
                continue
            else:
                sys.exit()

        except ValueError as message:
            print(message)
            retry('R', 'retry')


def get_valid_names():
    """Returns the inputted first and last names"""
    first = validate_name(input("First: "), 'First').title()
    last = validate_name(input("Last: "), 'Last').title()
    return first, last


def adding_expense(user):
    """
    Add an expense entry for the user in the BudgetBits application.

    This function guides the user through the process of adding an expense entry, including selecting
    a category, specifying the amount, and adding optional notes. The entry is validated, and if confirmed,
    it is added to the user's expense records.

    Args:
        user (BudgetBits): The BudgetBits instance of the user.
    """

    print(f"{'--- ADDING EXPENSE ---':^80}")
    category: str = input("Category: ")
    while True:
        amount: int = validate_amount(input("Amount: ₱"))
        if amount:
            break
    notes: str = input("NOTES: ")

    prompt = input(
        "\nDo you want to proceed with adding this expense? (Y/N): ").upper()
    if prompt == "Y":
        try:
            user_expense = user.expense_entry(category, amount, notes)

        except ValueError as message:
            print(f"\n{message}")
            print("\nExpense addition cancelled.")
            return False

        else:
            print("\nExpense addition added.")
            return user_expense


def validate_name(name: str, message: str = 'Full'):
    """
    Validate the provided name for BudgetBits personal information.

    This function validates a provided name by checking if it is not empty or composed only of whitespace.

    Args:
        name (str): The name to be validated.
    """
    if not name or name.isspace():
        raise ValueError(
            f"\n{message} name cannot be empty or consist of only whitespace."
        )
    name = name.title()
    return name


def validate_amount(amount: str):
    """
    Validate the provided amount for BudgetBits expenses.

    This function validates a provided amount by converting it to an integer and checking if it's positive.

    Args:
        amount (str): The amount to be validated.

    Returns:
        int: The validated amount.
    """
    try:
        amount = int(amount.replace(',', '_'))
        if amount <= 0:
            print("Invalid input. Please enter a positive value for the amount.")
        else:
            return amount
    except ValueError:
        print("Invalid input. Please enter a valid integer for the monthly budget.")


if __name__ == "__main__":
    main()
