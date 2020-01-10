import configparser
import logging


from allure_commons._allure import step
from .http_manager import HttpManager
from .json_fixture import JSONFixture


class Api:
    LOGGER = logging.getLogger(__name__)

    config = configparser.ConfigParser()
    config.read('config.ini')

    def __init__(self, environment):
        self.environment = environment
        self.base_url = environment

    @staticmethod
    def login():
        with step("Login"):
            url = Api.USER_AUTH
            user_name = Api.config.get('api', 'login')
            password = Api.config.get('api', 'password')
            data = JSONFixture.authorization(user_name, password)

            result = HttpManager.auth(url, data)
            Api.LOGGER.info(f'TEST: Login with {user_name}, {password} credentials')
            return result


class Config:
    """Хранение и использование переменных окружения"""
    _env = {}

    def __init__(self, path="config.ini"):
        config = configparser.ConfigParser()
        config.read([path])
        for section in config.sections():
            self._env[section] = dict(config.items(section))

    def __getitem__(self, key):
        if key not in self._env:
            raise Exception("'%s' key is not found in env configuration from config.ini" % key)
        return self._env[key]

    def __contains__(self, env):
        return env in self._env