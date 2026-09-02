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

def update_leave_status(id, status):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE leave_requests
        SET status=?
        WHERE id=?
        """,
        (
            status,
            id
        )
    )

    connection.commit()

    connection.close()

def get_leave_statistics():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM leave_requests"
    )
    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM leave_requests
        WHERE status='Pending'
        """
    )
    pending = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM leave_requests
        WHERE status='Approved'
        """
    )
    approved = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM leave_requests
        WHERE status='Rejected'
        """
    )
    rejected = cursor.fetchone()[0]

    connection.close()

    return {
        "total": total,
        "pending": pending,
        "approved": approved,
        "rejected": rejected
    }

def search_leave_requests(employee_id="", status="", leave_type=""):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        SELECT *
        FROM leave_requests
        WHERE 1=1
    """

    parameters = []

    if employee_id:

        query += """
            AND employee_id LIKE ?
        """

        parameters.append(
            f"%{employee_id}%"
        )

    if status:

        query += """
            AND status = ?
        """

        parameters.append(status)

    if leave_type:

        query += """
            AND leave_type = ?
        """

        parameters.append(leave_type)

    query += """
        ORDER BY id DESC
    """

    cursor.execute(
        query,
        parameters
    )

    leaves = cursor.fetchall()

    connection.close()

    return leaves

def has_overlapping_leave(employee_id, start_date, end_date):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM leave_requests
        WHERE employee_id=?
        AND status IN ('Pending', 'Approved')
        AND start_date <= ?
        AND end_date >= ?
        """,
        (
            employee_id,
            end_date,
            start_date
        )
    )

    existing_leave = cursor.fetchone()

    connection.close()

    return existing_leave is not None