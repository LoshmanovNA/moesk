import pytest
from requests import Response
from ..utils.api import Api


def test_login():
    result = Api.login()
    assert 300 == result.status_code

    response_json = result.json()
    assert "sessionId" in response_json
