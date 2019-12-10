from seleniumbase.core.mysql import DatabaseManager
import pytest


@pytest.fixture(scope='function')
def db_connection():
    """Set connect to DataBase"""
    connect = DatabaseManager()
    return connect

