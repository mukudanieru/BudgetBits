# **_BudgetBits_**

```
                 ____            __           __  ____  _ __
                / __ )__  ______/ /___ ____  / /_/ __ )(_) /______
               / __  / / / / __  / __ `/ _ \/ __/ __  / / __/ ___/
              / /_/ / /_/ / /_/ / /_/ /  __/ /_/ /_/ / / /_(__  )
             /_____/\__,_/\__,_/\__, /\___/\__/_____/_/\__/____/
                               /____/
```

**BudgetBits | A CS50P final project**

BudgetBits is an interactive command line interface project that is a user-friendly and intuitive expense tracker designed to simplify personal finance management.

_Video demo:_ (youtube link)

## Features

- **Login and Registration:** Securely access your budget and expense information using the built-in login and registration system. Your data is protected and only accessible to you.

```
                 ____            __           __  ____  _ __
                / __ )__  ______/ /___ ____  / /_/ __ )(_) /______
               / __  / / / / __  / __ `/ _ \/ __/ __  / / __/ ___/
              / /_/ / /_/ / /_/ / /_/ /  __/ /_/ /_/ / / /_(__  )
             /_____/\__,_/\__,_/\__, /\___/\__/_____/_/\__/____/
                               /____/

                         [L]ogin | [R]egister | [E]xit
 >>
```

- **Expense Entry:** Easily add your expenses along with category and notes. The system keeps track of your spending history.

```
                          Welcome to BudgetBits, [username]!
                 ____            __           __  ____  _ __
                / __ )__  ______/ /___ ____  / /_/ __ )(_) /______
               / __  / / / / __  / __ `/ _ \/ __/ __  / / __/ ___/
              / /_/ / /_/ / /_/ / /_/ /  __/ /_/ /_/ / / /_(__  )
             /_____/\__,_/\__,_/\__, /\___/\__/_____/_/\__/____/
                               /____/


                      [P]ersonal | [A]dd | [S]how | [E]xit

 >> A
                             --- ADDING EXPENSE ---
Category: University expenses
Amount: ₱350
NOTES: uni uniform

Do you want to proceed with adding this expense? (Y/N): Y
```

- **Monthly Budget:** Set a monthly budget to keep your spending in check. BudgetBits also lets you update your monthly budget of each month, ensuring your financial information is always up-to-date.

```
                       Welcome back to BudgetBits, [username]!
                 ____            __           __  ____  _ __
                / __ )__  ______/ /___ ____  / /_/ __ )(_) /______
               / __  / / / / __  / __ `/ _ \/ __/ __  / / __/ ___/
              / /_/ / /_/ / /_/ / /_/ /  __/ /_/ /_/ / / /_(__  )
             /_____/\__,_/\__,_/\__, /\___/\__/_____/_/\__/____/
                               /____/


                      [P]ersonal | [A]dd | [S]how | [E]xit

 >> P
+----------------------------+-------------------+
| PERSONAL INFORMATION       | MONTH: August     |
+============================+===================+
| USERNAME:                  | [username]        |
| FULL NAME:                 | [user's full name]|
| CURRENT BUDGET (August)    | ₱                 |
| TOTAL EXPENSES (August)    | ₱                 |
| REMAINING BALANCE (August) | ₱                 |
+----------------------------+-------------------+
(Press [B] to back or [E] to exit.) >>
```

```
                 ____            __           __  ____  _ __
                / __ )__  ______/ /___ ____  / /_/ __ )(_) /______
               / __  / / / / __  / __ `/ _ \/ __/ __  / / __/ ___/
              / /_/ / /_/ / /_/ / /_/ /  __/ /_/ /_/ / / /_(__  )
             /_____/\__,_/\__,_/\__, /\___/\__/_____/_/\__/____/
                               /____/


                      [P]ersonal | [A]dd | [S]how | [E]xit

 >> S
+---------------------+------------+----------+-------------+
| Category            | Date       |   Amount | Notes       |
+=====================+============+==========+=============+
| University expenses | 2023-08-16 |      350 | uni uniform |
+---------------------+------------+----------+-------------+
(Press [B] to back or [E] to exit.) >>
```

_The monthly update:_

```
                       Welcome back to BudgetBits, lone!

Welcome to a new month!
Take a moment to update your monthly budget.

New Monthly Budget: ₱4,000
Are you sure about your new monthly budget ₱4000? (Y/N) Y
```

With BudgetBits, you can take control of your finances, make informed decisions, and work towards your financial goals.

## Installation

1. Clone this repository to your local machine using git:

```bash
git clone https://github.com/mukudanieru/BudgetBits
```

or you can download install the project manually by following these steps:

- Click the green "Code" button at the top of the repository
- Choose "Download ZIP"
- Extract the ZIP archive to your desired location.

2. Navigate to the project directory:

- Open a terminal/cli and navigate to the project directory using the `cd` command

```bash
cd BudgetBits-main
```

3. Install the required dependencies:

- Install the project's dependencies using the following command

```bash
pip install -r requirements.txt
```

## Usage/Examples

### _Starting the app/program_

Run the application using:

```bash
python project.py
```

When you run BudgetBits, you'll be presented with the following options:

- **[L]ogin:** Log in to your existing account.
- **[R]egister:** Create a new account if you're a first-time user.
- **[E]xit:** Exit the BudgetBits application.

### _Registration Setup_

If you choose **[R]egister**, the application will guide you through the registration setup:

1. Enter your desired username.
2. Enter your password for the new account.
3. Provide your personal information:

- First name
- Last name
- Monthly budget for the current month

Once you've completed the registration setup, you'll be prompted to confirm your personal information. You can choose to continue with the provided details or restart the registration if needed.

### _Login_

After registering, you can choose **[L]ogin** to access your existing account. Enter your username and password to log in.

If you're a returning user, you'll be greeted with a welcome message:

```bash
- Welcome back to BudgetBits, [username]!
```

### _Main Page_

Once logged in, you'll be taken to the main page where you can manage your expenses:

- **[P]ersonal:** View your personal information, including your username, first name, last name, and remaining budget.
- **[A]dd:** Add new expenses for the current month. You'll provide information such as the expense category, amount, and any notes.

When adding expenses, the application will prompt you for details about the expense, including the category, amount, and optional notes. You can confirm the expense entry, and it will be added to your expense records.

- **[S]how:** Display a summary of your expenses, including details like dates, categories, amounts, and notes.
- **[E]xit:** Exit the BudgetBits application.

### _Monthly Budget Update_

Every month, you'll be prompted:

```bash
Welcome to a new month!
```

At this point, you have the opportunity to update your monthly budget for the upcoming month. The application will assist you through the process, ensuring that your financial records remain current and accurate.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request.

## Acknowledgements

- This project was developed as a final project for CS50P.

## Authors

For any inquiries or feedback, please contact: [@mukudanieru](https://github.com/mukudanieru)
