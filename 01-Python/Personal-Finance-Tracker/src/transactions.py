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


def search_transactions(transactions):

    if not transactions:
        print("\nNo transactions found.")
        return

    keyword = input(
        "\nEnter category or type to search: "
    ).strip().lower()

    found = False

    print("\nSearch Results")
    print("-" * 60)

    for index, transaction in enumerate(transactions, start=1):

        if (
            keyword in transaction["type"].lower()
            or
            keyword in transaction["category"].lower()
        ):

            found = True

            print(
                f"{index}. "
                f"{transaction['type']} | "
                f"{transaction['category']} | "
                f"₹{transaction['amount']:.2f} | "
                f"{transaction['date']}"
            )

    if not found:
        print("No matching transactions.")


def delete_transaction(transactions):

    if not transactions:

        print("\nNo transactions available.")
        return

    view_transactions(transactions)

    try:

        choice = int(
            input(
                "\nEnter transaction number to delete: "
            )
        )

        if 1 <= choice <= len(transactions):

            deleted = transactions.pop(choice - 1)

            save_transactions(transactions)

            print(
                f"\nDeleted {deleted['type']} "
                f"transaction successfully."
            )

        else:

            print("Invalid transaction number.")

    except ValueError:

        print("Please enter a valid number.")

def edit_transaction(transactions):

    if not transactions:

        print("\nNo transactions available.")
        return

    view_transactions(transactions)

    try:

        choice = int(
            input(
                "\nEnter transaction number to edit: "
            )
        )

        if not (1 <= choice <= len(transactions)):
            print("Invalid transaction.")
            return

        transaction = transactions[choice - 1]

        amount = float(
            input(
                f"Current Amount ₹{transaction['amount']}\n"
                "New Amount: ₹"
            )
        )

        transaction["amount"] = amount

        save_transactions(transactions)

        print("\nTransaction updated successfully.")

    except ValueError:

        print("Invalid amount.")
    

def generate_report(transactions):

    if not transactions:
        print("\nNo transactions available.")
        return

    total_income = 0
    total_expense = 0

    highest_income = 0
    highest_expense = 0

    category_summary = {}

    for transaction in transactions:

        if transaction["type"] == "Income":

            total_income += transaction["amount"]

            if transaction["amount"] > highest_income:
                highest_income = transaction["amount"]

        else:

            total_expense += transaction["amount"]

            if transaction["amount"] > highest_expense:
                highest_expense = transaction["amount"]

            category = transaction["category"]

            if category not in category_summary:
                category_summary[category] = 0

            category_summary[category] += transaction["amount"]

    balance = total_income - total_expense

    print("\n" + "=" * 55)
    print("              FINANCIAL REPORT")
    print("=" * 55)

    print(f"Total Income     : ₹{total_income:.2f}")
    print(f"Total Expense    : ₹{total_expense:.2f}")
    print(f"Current Balance  : ₹{balance:.2f}")

    print()

    print(f"Highest Income   : ₹{highest_income:.2f}")
    print(f"Highest Expense  : ₹{highest_expense:.2f}")

    print("\nExpense Breakdown")

    print("-" * 55)

    for category, amount in category_summary.items():

        print(f"{category:<20} ₹{amount:.2f}")

    print("=" * 55)