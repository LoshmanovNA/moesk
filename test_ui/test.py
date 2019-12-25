from seleniumbase.core.mysql import DatabaseManager
from faker import Faker
f = Faker('ru-RU')
email = f.email()


def test_db():
    connect = DatabaseManager()
    sql = "SELECT email FROM users WHERE email=%s"
    value = email
    print(value)
    # connect.execute_query(sql, value)
    rows = connect.query_fetch_one(sql, value)
    print(type(rows))
    for row in rows:
        print(row, value)
        assert row == email, f'{row} is no equal {email}'
