MENU_WIDTH = 50


def display_menu():
    print("\n" + "=" * MENU_WIDTH)
    print("        PERSONAL FINANCE TRACKER")
    print("=" * MENU_WIDTH)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Search Transactions")
    print("6. Edit Transaction")
    print("7. Delete Transaction")
    print("8. Reports")
    print("9. Export CSV")
    print("10. Import CSV")
    print("11. Backup Data")
    print("12. Help")
    print("13. Exit")
    print("=" * MENU_WIDTH)


def display_help():
    print("\n" + "=" * MENU_WIDTH)
    print("HELP")
    print("=" * MENU_WIDTH)
    print("1 -> Add Income")
    print("2 -> Add Expense")
    print("3 -> View Transactions")
    print("4 -> View Balance")
    print("5 -> Search Transactions")
    print("6 -> Edit Transaction")
    print("7 -> Delete Transaction")
    print("8. Reports")
    print("9. Export CSV")
    print("10. Import CSV")
    print("11. Backup Data")
    print("12. Help")
    print("13. Exit")
    print("=" * MENU_WIDTH)


def get_user_choice():
    return input("Enter your choice (1-13): ")