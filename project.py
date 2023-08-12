from budgetbits import AccountValidator, BudgetBits, clear
from data import InformationManager
import sys
import os


def main():
    # check the registered users
    info = InformationManager(os.path.join("data", "data.json"))
    users = info.retrieve()

    # login process
    username = current_account()

    if username not in users:
        clear()
        user = register_user(username)
        users[username] = user.__dict__
        info.save(users)
        print(f"\n{f'Welcome to BudgetBits, {username}!':^80}")

    else:
        clear()
        user = existing_user(users[username])
        print(f"\n{f'Welcome back to BudgetBits, {username}!':^80}")

    if update := user.monthly_budget_update():
        users[username] = update
        info.save(users)
        clear()

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
            print("Invalid input.")

        retry('B', 'back')


def retry(letter, message):
    while True:
        prompt = input(
            f"(Press [{letter}] to {message} or [E] to exit.) >> ").upper()
        if prompt == f"{letter}":
            clear()
            break
        elif prompt == "E":
            sys.exit()
        else:
            continue


def current_account():
    account_manager = AccountValidator()
    return account_manager.account_validator()


def existing_user(data):
    return BudgetBits(
        data["_username"],
        data["_first"],
        data["_last"],
        data["_monthly_budget"],
        data["_expenses"],
        data["_remaining_balance"],
    )


def register_user(username: str):
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
                "Are you sure about your personal info? (Y/N) ").upper()
            if prompt == "Y":
                clear()
                return BudgetBits(username, first, last, monthly_budget, {}, monthly_budget)
            elif prompt == "N":
                continue
            else:
                sys.exit()

        except ValueError as message:
            print(message)
            retry('R', 'retry')


def get_valid_names():
    first = validate_name(input("First: ")).title()
    last = validate_name(input("Last: ")).title()
    return first, last


def adding_expense(user):
    print(f"{'--- ADDING EXPENSE ---':^80}")
    category: str = input("Category: ")
    while True:
        amount: int = validate_amount(input("Amount: ₱"))
        if amount:
            break
    notes: str = input("NOTES: ")

    prompt = input("\nAre you sure about adding this expense? (Y/N): ").upper()
    if prompt == "Y":
        print("Expense addition added.")
        return user.expense_entry(category, amount, notes)
    print("Expense addition cancelled.")
    return False


def validate_name(name):
    if not name or name.isspace():
        raise ValueError(
            "First name cannot be empty or consist of only whitespace."
        )
    return name


def validate_amount(amount):
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
