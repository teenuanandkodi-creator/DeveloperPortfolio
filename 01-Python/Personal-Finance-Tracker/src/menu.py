MENU_WIDTH = 45


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


def get_user_choice():
    return input("Enter your choice (1-6): ")