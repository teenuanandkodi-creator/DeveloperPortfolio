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

def get_employee_by_id(id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id=?",
        (id,)
    )

    employee = cursor.fetchone()

    connection.close()

    return employee

def get_total_employees():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def update_employee(id, employee_id, name, department):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE employees
        SET employee_id=?,
            name=?,
            department=?
        WHERE id=?
        """,
        (
            employee_id,
            name,
            department,
            id
        )
    )

    connection.commit()

    connection.close()

def delete_employee(id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=?",
        (id,)
    )

    connection.commit()

    connection.close()
