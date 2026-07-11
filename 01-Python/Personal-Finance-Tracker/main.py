from src.menu import (
    display_menu,
    display_help,
    get_user_choice,
)

from src.storage import load_transactions

from src.transactions import (
    add_income,
    add_expense,
    view_transactions,
    view_balance,
)


def process_choice(choice, transactions):

    if choice == "1":

        add_income(transactions)

    elif choice == "2":

        add_expense(transactions)

    elif choice == "3":

        view_transactions(transactions)

    elif choice == "4":

        view_balance(transactions)

    elif choice == "5":

        display_help()

    elif choice == "6":

        print("\nThank you for using Personal Finance Tracker!")

        return False

    else:

        print("\nInvalid choice.")

    return True


def main():

    transactions = load_transactions()

    running = True

    while running:

        display_menu()

        choice = get_user_choice()

        running = process_choice(choice, transactions)


if __name__ == "__main__":
    main()