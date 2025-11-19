import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def create(self, user_id, name):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (id, name) VALUES (?, ?)",
                (user_id, name)
            )
            self.connection.commit()
            return True, "Usuario creado"
        except sqlite3.IntegrityError:
            return False, "El ID ya existe"

    def read_all(self):
        self.cursor.execute("SELECT id, name FROM usuarios")
        return self.cursor.fetchall()

    def read_one(self, user_id):
        self.cursor.execute("SELECT name FROM usuarios WHERE id = ?", (user_id,))
        return self.cursor.fetchone()

    def update(self, user_id, new_name):
        self.cursor.execute(
            "UPDATE usuarios SET name = ? WHERE id = ?",
            (new_name, user_id)
        )
        self.connection.commit()
        return self.cursor.rowcount

    def delete(self, user_id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        self.connection.commit()
        return self.cursor.rowcount