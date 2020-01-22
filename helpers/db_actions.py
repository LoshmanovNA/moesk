from seleniumbase.core.mysql import DatabaseManager
from datetime import datetime
import json


class DataBase(DatabaseManager):
    """Действия с базой данных"""

    @staticmethod
    def open_json(path):
        with open(path, 'r', encoding='utf-8') as f:
            value = json.loads(f.read())
            return value

    def insert_new_row_db(self, path='path', table='table'):
        connect = DatabaseManager()
        json_obj = self.open_json(path)

        placeholders = ', '.join(['%s'] * len(json_obj))
        columns = ', '.join(json_obj.keys())
        values = list(json_obj.values())
        sql = f"INSERT INTO {table} ( {columns} ) VALUES ( {placeholders} );"
        connect.execute_query(sql, values)

    # @staticmethod
    # def activate_new_account_db(page):
    #     """Вносим изменения в тестовую БД для активации УЗ"""
    #     time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # Дата для сохранения в БД
    #     password = page.pass_hash  # Хэш пароля для сохранения в БД
    #     sql = f"UPDATE users SET confirmed_at='{time}', sms_confirmed_at='{time}', " \
    #           f"encrypted_password='{password}', first_password_changed=1 WHERE email=%s"
    #     value = page.email  # Email учетной записи, которую нужно активировать
    #     connect = DatabaseManager()  # Устанавливаем соединение с БД
    #     connect.execute_query(sql, value)  # Выполняем запрос

    # @staticmethod
    # def should_be_new_record_at_db(email):
    #     """Проверяем наличие новой записи в БД"""
    #     connect = DatabaseManager()
    #     sql = "SELECT email FROM users WHERE email=%s"
    #     assert connect.query_fetch_one(sql, email)
    #
    # @staticmethod
    # def delete_new_record_from_db(email):
    #     """Удаляем запись о созданной УЗ из БД и проверяем, что email не найден"""
    #     connect = DatabaseManager()
    #     sql_1 = "DELETE FROM users WHERE email=%s"
    #     connect.execute_query(sql_1, email)
    #     connect = DatabaseManager()
    #     sql_2 = "SELECT email FROM users WHERE email=%s"
    #     assert not connect.query_fetch_one(sql_2, email)



