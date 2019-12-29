from seleniumbase.core.mysql import DatabaseManager
from ..data import TestData as TD
from datetime import datetime


class DataBase(DatabaseManager):
    """Действия с базой данных"""

    def activate_new_account_at_db(self):
        """Вносим изменения в тестовую БД для активации УЗ"""
        time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # Дата для сохранения в БД
        password = TD.pass_hash  # Хэш пароля для сохранения в БД
        sql = f"UPDATE users SET confirmed_at='{time}', sms_confirmed_at='{time}', " \
              f"encrypted_password='{password}', first_password_changed=1 WHERE email=%s"
        value = TD.email  # Email учетной записи, которую нужно активировать
        connect = DatabaseManager()  # Устанавливаем соединение с БД
        connect.execute_query(sql, value)  # Выполняем запрос

    def should_be_new_record_at_db(self, email):
        """Проверяем наличие новой записи в БД"""
        connect = DatabaseManager()
        sql = "SELECT email FROM users WHERE email=%s"
        assert connect.query_fetch_one(sql, email)

    def delete_new_record_from_db(self, email):
        """Удаляем запись о созданной УЗ из БД и проверяем, что email не найден"""
        connect = DatabaseManager()
        sql_1 = "DELETE FROM users WHERE email=%s"
        connect.execute_query(sql_1, email)
        connect = DatabaseManager()
        sql_2 = "SELECT email FROM users WHERE email=%s"
        assert not connect.query_fetch_one(sql_2, email)
