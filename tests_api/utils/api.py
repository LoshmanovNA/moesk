import configparser
import logging

from allure_commons._allure import step
from .http_manager import HttpManager
from .json_fixture import JSONFixture


class Api:
    LOGGER = logging.getLogger(__name__)
    config = configparser.ConfigParser()
    config.read('config.ini')

    BASE_URL = config.get('api', 'app_url')
    USER_AUTH = BASE_URL + '/user/auth'
    USER_REGISTER = BASE_URL + '/user/register'

    @staticmethod
    def login():
        with step("Login"):
            url = Api.USER_AUTH
            user_name = Api.config.get('api', 'login')
            password = Api.config.get('api', 'password')
            data = JSONFixture.authorization(user_name, password)

            result = HttpManager.auth(url, data)
            Api.LOGGER.info('TEST: Login with {0}, {1} credentials'.format(user_name, password))
            return result
