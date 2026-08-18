from src.database import get_connection


def authenticate_user(username, password):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?
        """,
        (
            username,
            password
        )
    )

    user = cursor.fetchone()

    connection.close()

    return user