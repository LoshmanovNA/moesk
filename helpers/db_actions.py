from seleniumbase.core.mysql import DatabaseManager
from datetime import datetime


class DataBase(DatabaseManager):
    """Действия с базой данных"""

    @staticmethod
    def activate_new_account_db(email, pass_hash):
        """Вносим изменения в тестовую БД для активации УЗ"""
        time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # Дата для сохранения в БД
        sql = f"UPDATE users SET confirmed_at='{time}', sms_confirmed_at='{time}', " \
              f"encrypted_password=%s, first_password_changed=1 WHERE email=%s"
        connect = DatabaseManager()  # Устанавливаем соединение с БД
        connect.execute_query(sql, (pass_hash, email))  # Выполняем запрос

    @staticmethod
    def delete_new_account_from_db(email):
        """Удаляем запись о созданной УЗ из БД и проверяем, что email не найден"""
        connect = DatabaseManager()
        sql_1 = "DELETE FROM users WHERE email=%s"
        connect.execute_query(sql_1, email)
        connect = DatabaseManager()
        sql_2 = "SELECT email FROM users WHERE email=%s"
        assert not connect.query_fetch_one(sql_2, email)

    # @staticmethod
    # def fake_data_json(path='path', email='email', pass_hash='pass_hash'):
    #     with open(path, 'r', encoding='utf-8') as f:
    #         value = json.loads(f.read())
    #         value.update({
    #             'email': email,
    #             'encrypted_password': pass_hash
    #         })
    #         return value
    #
    # def insert_new_row_into_db(self, fake_json, table):
    #     placeholders = ', '.join(['%s'] * len(fake_json))
    #     columns = ', '.join(fake_json.keys())
    #     values = list(fake_json.values())
    #     sql = f"INSERT INTO {table} ( {columns} ) VALUES ( {placeholders} );"
    #     self.execute_query(sql, values)
