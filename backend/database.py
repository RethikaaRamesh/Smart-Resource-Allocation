import sqlite3

DB_NAME = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        priority INTEGER,
        demand INTEGER
    )
    ''')

    conn.commit()
    conn.close()


def insert_task(name, priority, demand):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name, priority, demand) VALUES (?, ?, ?)",
              (name, priority, demand))
    conn.commit()
    conn.close()


def fetch_tasks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name, priority, demand FROM tasks")
    rows = c.fetchall()
    conn.close()

    return [{"name": r[0], "priority": r[1], "demand": r[2]} for r in rows]