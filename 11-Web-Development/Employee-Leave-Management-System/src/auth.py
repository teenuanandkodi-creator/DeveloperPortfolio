from werkzeug.security import check_password_hash

from src.database import get_connection


def authenticate_user(username, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    connection.close()

    if user and check_password_hash(user["password"], password):
        return user

    return None