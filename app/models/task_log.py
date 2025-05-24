import sqlite3
from datetime import datetime

DB_PATH = "task_logs.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS task_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT,
                status TEXT,
                start_time TEXT,
                end_time TEXT,
                duration REAL
            )
        ''')
init_db()

def log_task(task_id, status, start_time, end_time=None):
    duration = (end_time - start_time).total_seconds() if end_time else None
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO task_log (task_id, status, start_time, end_time, duration)
            VALUES (?, ?, ?, ?, ?)
        ''', (task_id, status, start_time.isoformat(), end_time.isoformat() if end_time else None, duration))
        conn.commit()
