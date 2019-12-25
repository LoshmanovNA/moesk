from seleniumbase.core.mysql import DatabaseManager


def db_connect():
    pass  # Cоздать фикстуру коннекта к ДБ и выполнить фикстурами активацию и удаление нового пользователя


def delete_new_account(new_account):
    """Удаляем запись о созданной УЗ из БД"""
    sql = "DELETE FROM users WHERE email=%s"
    value = new_account
    connect = DatabaseManager()
    connect.execute_query(sql, value)



