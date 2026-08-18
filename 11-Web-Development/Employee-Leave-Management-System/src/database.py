import sqlite3


DATABASE = "data/employee.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        employee_id TEXT,

        name TEXT,

        department TEXT

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leave_requests(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        employee_id TEXT,

        leave_type TEXT,

        start_date TEXT,

        end_date TEXT,

        reason TEXT,

        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        role TEXT
    )
    """)

def initialize_users():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    total = cursor.fetchone()[0]

    if total == 0:

        users = [

            (
                "admin",
                "admin123",
                "Admin"
            ),

            (
                "employee",
                "employee123",
                "Employee"
            )

        ]

        cursor.executemany(
            """
            INSERT INTO users
            (
                username,
                password,
                role
            )

            VALUES(?,?,?)
            """,
            users
        )

    connection.commit()

    connection.close()