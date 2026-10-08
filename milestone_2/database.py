import sqlite3

DB_NAME = "trakerz.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_expense(category, amount, description, date):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (category, amount, description, date)
        VALUES (?, ?, ?, ?)
    """, (category, amount, description, date))

    connection.commit()
    connection.close()


def get_expenses():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, category, amount, description, date
        FROM expenses
        ORDER BY id DESC
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def delete_expense(expense_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()
    connection.close()


def update_expense(expense_id, category, amount, description, date):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET category = ?, amount = ?, description = ?, date = ?
        WHERE id = ?
    """, (category, amount, description, date, expense_id))

    connection.commit()
    connection.close()


def get_total_expense():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses")

    total = cursor.fetchone()[0]

    connection.close()

    return total