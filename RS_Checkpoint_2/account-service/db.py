import sqlite3

DB_NAME = "accounts.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            owner TEXT,
            balance REAL
        )
    """)

    # seed data (only if empty)
    cur.execute("SELECT COUNT(*) FROM accounts")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO accounts VALUES (1, 'User', 1000)")
        cur.execute("INSERT INTO accounts VALUES (2, 'Savings', 5000)")

    conn.commit()
    conn.close()
