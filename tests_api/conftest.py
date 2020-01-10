import logging
import pytest
import configparser
from . import constants


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="environment",
        type=str.lower,
        choices=(
            constants.Environment.PRODUCTION,
            constants.Environment.TEST
        ),
        default=constants.Environment.TEST,
        help="The environment to run the tests in.")


@pytest.fixture
def environment(request):
    return request.config.getoption("--env")
