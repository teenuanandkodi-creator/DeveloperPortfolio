from src.storage import save_transactions


def add_income(transactions):

    try:

        amount = float(input("Enter income amount: ₹"))

        transaction = {
            "type": "Income",
            "amount": amount
        }

        transactions.append(transaction)

        save_transactions(transactions)

        print(f"\nIncome of ₹{amount:.2f} added successfully.")

    except ValueError:

        print("Invalid amount.")


def add_expense(transactions):

    try:

        amount = float(input("Enter expense amount: ₹"))

        transaction = {
            "type": "Expense",
            "amount": amount
        }

        transactions.append(transaction)

        save_transactions(transactions)

        print(f"\nExpense of ₹{amount:.2f} added successfully.")

    except ValueError:

        print("Invalid amount.")


def view_transactions(transactions):

    if not transactions:

        print("\nNo transactions available.")
        return

    print("\nTransaction History")
    print("-" * 45)

    for index, transaction in enumerate(transactions, start=1):

        print(
            f"{index}. {transaction['type']:<8} ₹{transaction['amount']:.2f}"
        )


def view_balance(transactions):

    balance = 0

    for transaction in transactions:

        if transaction["type"] == "Income":

            balance += transaction["amount"]

        else:

            balance -= transaction["amount"]

    print(f"\nCurrent Balance : ₹{balance:.2f}")