from src.menu import (
    display_menu,
    display_help,
    get_user_choice,
)

from src.export_import import(
    export_to_csv,
    import_from_csv,
    create_backup1
)

from src.storage import load_transactions

from src.transactions import (
    add_income,
    add_expense,
    view_transactions,
    view_balance,
    search_transactions,
    edit_transaction,
    delete_transaction,
    generate_report
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

        search_transactions(transactions)
    
    elif choice == "6":

        edit_transaction(transactions)
    
    elif choice == "7":

        delete_transaction(transactions)
    
    elif choice == "8":

        generate_report(transactions)
    
    elif choice == "9":

        export_to_csv(transactions)
    
    elif choice == "10":

        import_from_csv(transactions)
    
    elif choice == "11":

        create_backup()
    
    elif choice == "12":

        display_help()
    

    elif choice == "13":

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