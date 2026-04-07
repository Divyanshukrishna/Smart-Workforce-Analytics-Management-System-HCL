import sqlite3

class DatabaseManager:
    def __init__(self, db_name="workforce.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL
        )
        """)
        self.conn.commit()

    def add_employee(self, employee):
        self.cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
                            (employee.name, employee.age, employee.department, employee.salary))
        self.conn.commit()

    def get_all_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()