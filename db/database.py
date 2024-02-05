import sqlite3


class DataBaseClass:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Успешное подключение к базе данных {self.db_name}")
        except sqlite3.Error as e:
            print(f"Ошибка при подключении к базе данных {self.db_name}: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(f"Отключение от базы данных {self.db_name}")

    def execute_query(self, query):
        try:
            if self.cursor:
                self.cursor.execute(query)
                self.connection.commit()
                print("Запрос выполнен успешно")
            else:
                print("Не удалось выполнить запрос. Нет активного курсора.")
        except sqlite3.Error as e:
            print(f"Ошибка при выполнении запроса: {e}")

    def fetch_data(self, query):
        try:
            if self.cursor:
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            else:
                print("Не удалось получить данные. Нет активного курсора.")
                return None
        except sqlite3.Error as e:
            print(f"Ошибка при получении данных: {e}")
            return None

    def is_user_exist(self, user_id):
        self.cursor.execute('SELECT id FROM users WHERE id=?', (user_id,))
        return bool(self.cursor.fetchone())

    def add_user(self, user_id):
        self.cursor.execute('INSERT INTO users (id) VALUES (?)', (user_id,))
        self.connection.commit()

    def add_settings(self, user_id, settings):
        self.cursor.execute('UPDATE users SET gpt = ? WHERE id = ?', (settings, user_id))
        self.connection.commit()

    def get_settings(self, user_id):
        self.cursor.execute('SELECT gpt FROM users WHERE id=?', (user_id,))
        return self.cursor.fetchone()[0]

    def add_degree(self, user_id, degree):
        self.cursor.execute('UPDATE users SET degree = ? WHERE id = ?', (degree, user_id))
        self.connection.commit()

    def get_degree(self, user_id):
        self.cursor.execute('SELECT degree FROM users WHERE id=?', (user_id,))
        return self.cursor.fetchone()[0]

    def get_voice(self, user_id):
        self.cursor.execute('SELECT synthes_voice FROM users WHERE id=?', (user_id,))
        return self.cursor.fetchone()[0]

    def add_voice(self, user_id, synthes_voice):
        self.cursor.execute('UPDATE users SET synthes_voice = ? WHERE id = ?', (synthes_voice, user_id))
        self.connection.commit()

    def get_rate(self, user_id):
        self.cursor.execute('SELECT synthes_speed FROM users WHERE id=?', (user_id,))
        return self.cursor.fetchone()[0]

    def add_rate(self, user_id, synthes_speed):
        self.cursor.execute('UPDATE users SET synthes_speed = ? WHERE id = ?', (synthes_speed, user_id))
        self.connection.commit()

    def get_premium(self, user_id):
        self.cursor.execute('SELECT premium FORM users WHERE id=?', (user_id,))
        return self.cursor.fetchone()[0]

    def close(self):
        self.disconnect()


db = DataBaseClass('./db/users.db')
db.connect()

