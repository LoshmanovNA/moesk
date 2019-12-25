from seleniumbase.core.mysql import DatabaseManager
import pytest


@pytest.fixture
def db_connect():
    connect = DatabaseManager()
    return connect

