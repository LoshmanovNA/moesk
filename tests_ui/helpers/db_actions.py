from datetime import datetime
import time


class DBManager:

    def __init__(self, DBModel):
        """
        Gets database information from mysql_conf.py and creates a connection.
        """
        import pymysql

        retry_count = 3
        backoff = 1.2  # Time to wait (in seconds) between retries.
        count = 0
        while count < retry_count:
            try:
                self.conn = pymysql.connect(host=DBModel.db_server,
                                            user=DBModel.db_user,
                                            passwd=DBModel.db_pass,
                                            db=DBModel.db_schema,
                                            port=DBModel.db_port)
                self.conn.autocommit(True)
                self.cursor = self.conn.cursor()
                return
            except Exception:
                time.sleep(backoff)
                count = count + 1
        if retry_count == 3:
            raise Exception("Unable to connect to Database after 3 retries.")

    def query_fetch_all(self, query, values):
        """
        Executes a db query, gets all the values, and closes the connection.
        """
        self.cursor.execute(query, values)
        retval = self.cursor.fetchall()
        self.__close_db()
        return retval

    def query_fetch_one(self, query, values):
        """
        Executes a db query, gets the first value, and closes the connection.
        """
        self.cursor.execute(query, values)
        retval = self.cursor.fetchone()
        self.__close_db()
        return retval

    def execute_query(self, query, values):
        """
        Executes a query to the test_db and closes the connection afterwards.
        """
        retval = self.cursor.execute(query, values)
        self.__close_db()
        return retval

    def __close_db(self):
        self.cursor.close()
        self.conn.close()

    def activate_new_account_db(self, email, pass_hash):
        """Вносим изменения в тестовую БД для активации УЗ"""
        confirmed_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # Дата для сохранения в БД
        sql = f"UPDATE users SET confirmed_at='{confirmed_time}', sms_confirmed_at='{confirmed_time}', " \
              f"encrypted_password=%s, first_password_changed=1 WHERE email=%s"
        self.execute_query(sql, (pass_hash, email))  # Выполняем запрос

    def delete_new_account_from_db(self, email):
        """Удаляем запись о созданной УЗ из БД и проверяем, что email не найден"""
        sql_1 = "DELETE FROM users WHERE email=%s"
        self.execute_query(sql_1, email)
        sql_2 = "SELECT email FROM users WHERE email=%s"
        assert not self.query_fetch_one(sql_2, email)

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
