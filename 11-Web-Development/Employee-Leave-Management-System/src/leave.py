from src.database import get_connection


def add_leave_request(
    employee_id,
    leave_type,
    start_date,
    end_date,
    reason
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO leave_requests
        (
            employee_id,
            leave_type,
            start_date,
            end_date,
            reason,
            status
        )

        VALUES(?,?,?,?,?,?)
        """,
        (
            employee_id,
            leave_type,
            start_date,
            end_date,
            reason,
            "Pending"
        )
    )

    connection.commit()

    connection.close()


def get_all_leave_requests():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM leave_requests
        ORDER BY id DESC
        """
    )

    leaves = cursor.fetchall()

    connection.close()

    return leaves