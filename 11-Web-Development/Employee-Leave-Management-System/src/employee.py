from src.database import get_connection


def get_all_employees():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return employees


def insert_sample_data():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")

    total = cursor.fetchone()[0]

    if total == 0:

        sample_data = [

            ("EMP001", "Teenu Anand", "Artificial Intelligence"),

            ("EMP002", "John Smith", "Human Resources"),

            ("EMP003", "Alice Brown", "Finance"),

            ("EMP004", "David Wilson", "IT")

        ]

        cursor.executemany(

            """

            INSERT INTO employees

            (employee_id,name,department)

            VALUES(?,?,?)

            """,

            sample_data

        )

    connection.commit()

    connection.close()

def add_employee(employee_id, name, department):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO employees
        (employee_id, name, department)
        VALUES (?, ?, ?)
        """,
        (employee_id, name, department)
    )

    connection.commit()

    connection.close()