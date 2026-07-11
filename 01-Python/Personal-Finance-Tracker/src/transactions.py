from src.models import Transaction
from datetime import datetime
from src.storage import save_transactions

INCOME_CATEGORIES = [
    "Salary",
    "Freelancing",
    "Investment",
    "Business",
    "Gift",
    "Other"
]

EXPENSE_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Healthcare",
    "Other"
]

def select_category(category_list):

    print("\nAvailable Categories")

    for index, category in enumerate(category_list, start=1):
        print(f"{index}. {category}")

    while True:

        try:

            choice = int(input("\nSelect category: "))

            if 1 <= choice <= len(category_list):
                return category_list[choice - 1]

            print("Please choose a valid option.")

        except ValueError:
            print("Please enter a number.")


def add_income(transactions):

    while True:

        try:

            amount = float(input("Enter income amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    category = select_category(INCOME_CATEGORIES)

    transaction = {
        "type": "Income",
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    transactions.append(transaction)

    save_transactions(transactions)

    print("\nIncome added successfully.")


def add_expense(transactions):

    while True:

        try:

            amount = float(input("Enter expense amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    category = select_category(EXPENSE_CATEGORIES)

    transaction = {
        "type": "Expense",
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    transactions.append(transaction)

    save_transactions(transactions)

    print("\nExpense added successfully.")


def view_transactions(transactions):

    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n" + "-" * 75)
    print(f"{'No.':<5}{'Type':<10}{'Category':<18}{'Amount':<15}{'Date'}")
    print("-" * 75)

    for index, transaction in enumerate(transactions, start=1):

        print(
            f"{index:<5}"
            f"{transaction['type']:<10}"
            f"{transaction['category']:<18}"
            f"₹{transaction['amount']:<14.2f}"
            f"{transaction['date']}"
        )


def view_balance(transactions):

    income = 0
    expense = 0

    for transaction in transactions:

        if transaction["type"] == "Income":
            income += transaction["amount"]
        else:
            expense += transaction["amount"]

    balance = income - expense

    print("\n" + "-" * 40)
    print(f"Total Income  : ₹{income:.2f}")
    print(f"Total Expense : ₹{expense:.2f}")
    print(f"Balance       : ₹{balance:.2f}")
    print("-" * 40)