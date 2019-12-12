from seleniumbase.core.mysql import DatabaseManager
import pytest
import datetime
from . import data

def db_connect() # Cоздать фикстуру коннекта к ДБ и выполнить фикстурами активацию и удаление нового пользователя



def activate_new_account():
    """Вносим изменения в БД для активации УЗ"""
    time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # Дата для сохранения в БД
    password = data.pass_hash  # Хэш пароля для сохранения в БД
    sql = f"UPDATE users SET confirmed_at='{time}', sms_confirmed_at='{time}', " \
          f"encrypted_password='{password}', first_password_changed=1 WHERE email=%s"
    value = data.new_user  # Email учетной записи, которую нужно активировать
    connect = DatabaseManager()  # Устанавливаем соединение с БД
    connect.execute_query(sql, value)  # Выполняем запрос


def delete_new_account():
    """Удаляем запись о созданной УЗ из БД"""
    sql = "DELETE FROM users WHERE email=%s"
    value = data.new_user
    connect = DatabaseManager()
    connect.execute_query(sql, value)



