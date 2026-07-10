import json
import os

MENU_WIDTH = 45
DATA_FILE = "data/transactions.json"

transactions = []


def display_menu():
    print("\n" + "=" * MENU_WIDTH)
    print("       PERSONAL FINANCE TRACKER")
    print("=" * MENU_WIDTH)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Help")
    print("6. Exit")
    print("=" * MENU_WIDTH)


def get_user_choice():
    return input("Enter your choice (1-6): ")


def display_help():
    print("\n" + "=" * MENU_WIDTH)
    print("               HELP MENU")
    print("=" * MENU_WIDTH)
    print("1 -> Add Income")
    print("2 -> Add Expense")
    print("3 -> View Transactions")
    print("4 -> View Balance")
    print("5 -> Help")
    print("6 -> Exit")
    print("=" * MENU_WIDTH)


def load_transactions():
    global transactions

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                transactions = json.load(file)
        except json.JSONDecodeError:
            transactions = []
    else:
        transactions = []


def save_transactions():
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


def add_income():
    try:
        amount = float(input("Enter income amount: ₹"))

        transaction = {
            "type": "Income",
            "amount": amount
        }

        transactions.append(transaction)

        save_transactions()

        print(f"\nIncome of ₹{amount:.2f} added successfully.")

    except ValueError:
        print("\nInvalid amount.")


def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))

        transaction = {
            "type": "Expense",
            "amount": amount
        }

        transactions.append(transaction)

        save_transactions()

        print(f"\nExpense of ₹{amount:.2f} added successfully.")

    except ValueError:
        print("\nInvalid amount.")


def view_transactions():

    if not transactions:
        print("\nNo transactions available.")
        return

    print("\nTransaction History")
    print("-" * MENU_WIDTH)

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. {transaction['type']:<8} ₹{transaction['amount']:.2f}"
        )


def view_balance():

    balance = 0

    for transaction in transactions:

        if transaction["type"] == "Income":
            balance += transaction["amount"]

        else:
            balance -= transaction["amount"]

    print("\n" + "-" * MENU_WIDTH)
    print(f"Current Balance : ₹{balance:.2f}")
    print("-" * MENU_WIDTH)


def process_choice(choice):

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        view_balance()

    elif choice == "5":
        display_help()

    elif choice == "6":
        print("\nThank you for using Personal Finance Tracker!")
        return False

    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")

    return True


def main():

    load_transactions()

    running = True

    while running:

        display_menu()

        choice = get_user_choice()

        running = process_choice(choice)


if __name__ == "__main__":
    main()