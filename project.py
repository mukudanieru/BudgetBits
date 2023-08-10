from budgetbits import AccountValidator, BudgetBits, clear
from data import InformationManager
import sys
import os


def main():
    # check the registered users
    info = InformationManager(os.path.join("data", "data.json"))
    users = info.retrieve()

    # login process
    username = "lone"  # current_account()

    if username not in users:
        user = register_user(username)
        users[username] = user.__dict__
        info.save(users)
        clear()
        print(f"\n{f'Welcome to BudgetBits, {username}!':^80}")

    else:
        clear()
        user = existing_user(users[username])
        print(f"\n{f'Welcome back to BudgetBits, {username}!':^80}")

    while True:
        print(user)
        print(f"\n{'[P]ersonal | [A]dd | [S]how | [E]xit':^80}\n")
        prompt = input(" >> ").upper()
        if prompt == "P":
            print(f"{user.display_information():^80}")
        elif prompt == "A":
            expense_added = adding_expense(user)
            if expense_added:
                users[username] = expense_added
                info.save(users)
        elif prompt == "S":
            print(user.display_expenses())
        elif prompt == "E":
            sys.exit()
        else:
            print("Invalid input.")

        prompt = input("(Press [B] to back.) >> ").upper()
        if prompt == "B":
            clear()
        else:
            sys.exit()


def current_account():
    account_manager = AccountValidator()
    return account_manager.account_validator()


def register_user(username: str):

    while True:
        clear()
        print(f"Personal information setup for {username}.")
        first: str = input("First: ").title()
        last: str = input("Last: ").title()
        try:
            monthly_budget: int = int(input("Amount: ₱").replace(',', '_'))
        except ValueError:
            print("Invalid input. Please enter a valid integer for the monthly budget.")

        print(
            "\n[Y]es - (to continue) | [N]o - (to provide your personal information again)")
        prompt = input("Are you sure about your personal info? (Y/N) ").upper()
        if prompt == "Y":
            return BudgetBits(username, first, last, monthly_budget, {}, monthly_budget)
        elif prompt == "N":
            continue
        else:
            sys.exit()


def existing_user(data):
    return BudgetBits(
        data["_username"],
        data["_first"],
        data["_last"],
        data["_monthly_budget"],
        data["_expenses"],
        data["_remaining_balance"],
    )


def adding_expense(user):
    print(f"{'--- ADDING EXPENSE ---':^80}")
    category: str = input("Category: ")

    while True:
        try:
            amount: int = int(input("Amount: ₱").replace(',', '_'))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the amount.")

    notes: str = input("NOTES: ")

    prompt = input("Are you sure about adding this expense? (Y/N): ").upper()
    if prompt == "Y":
        print("Expense addition added.")
        return user.expense_entry(category, amount, notes)
    print("Expense addition cancelled.")
    return False


if __name__ == "__main__":
    main()
