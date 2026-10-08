from milestone_2.database import connect_db


def category_totals():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    data = cursor.fetchall()

    connection.close()

    return data


def monthly_total():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total or 0