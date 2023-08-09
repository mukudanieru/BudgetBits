from budgetbits import AccountValidator, BudgetBits, clear
from data import InformationManager
from time import sleep
import sys
import os


def main():
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
        print(f"\n{f'Welcome back to BudgetBits, {username}!':^80}")

    while True:
        print(user)
        print(f"\n{'[P]ersonal | [A]dd | [S]how | [E]xit':^80}\n")
        prompt = input(" >> ").upper()
        if prompt == "P":
            print(
                f"Monthly budget: {user.monthly_budget}\nUser's expenses: {user.expenses}\nUser's remaining balance: {user.remaining_balance}"
            )
            prompt = input("(Press [B] to back.) >> ").upper()
            if prompt == "B":
                clear()
            else:
                sys.exit()
        elif prompt == "A":
            expense_added = adding_expense(user)
            if expense_added:
                users[username] = expense_added
                info.save(users)
            sleep(3)
            clear()
        elif prompt == "S":
            print("SOON!")
        elif prompt == "E":
            sys.exit()
        else:
            print("Invalid input.")


def current_account():
    account_manager = AccountValidator()
    return account_manager.account_validator()


def register_user(username: str):
    print(f"Personal information setup for {username}.")
    first = input("First: ").title()
    last = input("Last: ").title()
    monthly_budget = int(input("Monthly budget: "))

    return BudgetBits(username, first, last, monthly_budget, {}, monthly_budget)


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
    amount: int = int(input("Amount: "))
    notes: str = input("NOTES: ")

    prompt = input("Are you sure about adding this expense? (Y/N): ").upper()
    if prompt == "Y":
        print("Expense addition added.")
        return user.expense_entry(category, amount, notes)
    print("Expense addition cancelled.")
    return False


if __name__ == "__main__":
    main()
