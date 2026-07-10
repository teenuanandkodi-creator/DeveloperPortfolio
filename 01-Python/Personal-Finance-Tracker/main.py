MENU_WIDTH = 45

transactions = []

def display_menu():
    print("\n" + "=" * 45)
    print("       PERSONAL FINANCE TRACKER")
    print("=" * 45)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Help")
    print("6. Exit")
    print("=" * 45)


def get_user_choice():
    return input("Enter your choice (1-6): ")

def display_help():
    print("\n" + "=" * 45)
    print("               HELP MENU")
    print("=" * 45)
    print("1 -> Add Income")
    print("2 -> Add Expense")
    print("3 -> View Transactions")
    print("4 -> View Balance")
    print("5 -> Help")
    print("6 -> Exit")
    print("=" * 45)

def add_income():
    amount = float(input("Enter income amount: "))

    transaction = {
        "type": "Income",
        "amount": amount
    }

    transactions.append(transaction)

    print(f"\nIncome of ₹{amount:.2f} added successfully.")

def add_expense():
    amount = float(input("Enter expense amount: "))

    transaction = {
        "type": "Expense",
        "amount": amount
    }

    transactions.append(transaction)

    print(f"\nExpense of ₹{amount:.2f} added successfully.")

def view_transactions():

    if not transactions:
        print("\nNo transactions found.")
        return

    print("\nTransaction History")

    print("-" * MENU_WIDTH)

    for transaction in transactions:

        print(
            f"{transaction['type']} : ₹{transaction['amount']:.2f}"
        )

def view_balance():

    balance = 0

    for transaction in transactions:

        if transaction["type"] == "Income":
            balance += transaction["amount"]

        else:
            balance -= transaction["amount"]

    print(f"\nCurrent Balance : ₹{balance:.2f}")


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
    running = True

    while running:
        display_menu()

        choice = get_user_choice()

        running = process_choice(choice)


if __name__ == "__main__":
    main()