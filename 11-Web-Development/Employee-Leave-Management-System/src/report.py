import csv
import io

from src.database import get_connection


def get_leave_report(
    employee_id="",
    status="",
    leave_type=""
):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            employee_id,
            leave_type,
            start_date,
            end_date,
            reason,
            status
        FROM leave_requests
        WHERE 1=1
    """

    parameters = []

    if employee_id:
        query += " AND employee_id LIKE ?"
        parameters.append(f"%{employee_id}%")

    if status:
        query += " AND status = ?"
        parameters.append(status)

    if leave_type:
        query += " AND leave_type = ?"
        parameters.append(leave_type)

    query += " ORDER BY start_date DESC"

    cursor.execute(query, parameters)

    leave_requests = cursor.fetchall()

    connection.close()

    return leave_requests


def create_leave_csv(leave_requests):

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Employee ID",
        "Leave Type",
        "Start Date",
        "End Date",
        "Reason",
        "Status"
    ])

    for leave in leave_requests:

        writer.writerow([
            leave["id"],
            leave["employee_id"],
            leave["leave_type"],
            leave["start_date"],
            leave["end_date"],
            leave["reason"],
            leave["status"]
        ])

    return output.getvalue()