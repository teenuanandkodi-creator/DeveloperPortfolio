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

    connection.commit()

    connection.close()