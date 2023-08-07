from budgetbits import AccountValidator, BudgetBits
from data import InformationManager
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

    clear()
    print(f"\n{'[P]ersonal | [A]dd | [S]how | [E]xit':^80}\n")
    while True:
        prompt = input(" >> ").upper()
        if prompt == "P":
            print(f"{user}\nMonthly budget: {user.monthly_budget}\nUser's expenses: {user.expenses}\nUser's remaining balance: {user.remaining_balance}")
        elif prompt == "A":
            print(f"{'--- ADDING EXPENSE ---':^80}")
            category = input("Category: ")
            amount = int(input("Amount: "))
            notes = input("NOTES: ")
            users[username] = user.expense_entry(category, amount, notes)
            info.save(users)
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


def clear():
    # clear terminal for windows os
    if os.name == "nt":
        os.system("cls")
    # clear terminal for unix-based systems (Linux and macOS)
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
