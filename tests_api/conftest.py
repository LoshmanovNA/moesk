import logging
import pytest
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
