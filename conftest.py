from seleniumbase.core.mysql import DatabaseManager
import pytest


@pytest.fixture(scope='function')
def db_query():
    """Select query to DataBase"""
    sql = "Select first_name, last_name from users where id=%s "
    user_id = 1872
    query = DatabaseManager()
    res = query.query_fetch_one(query=sql, values=user_id)
    return res

