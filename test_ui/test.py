from seleniumbase.core.mysql import DatabaseManager
from . import data as d

print(d.email)

def database():
    connect = DatabaseManager()
    sql = "SELECT email FROM users WHERE email=%s"
    value = d.email
    res = connect.query_fetch_one(sql, value)
    print(res[0])

    # assert row[0] == d.email, f'{row} is no equal {d.email}'
database()