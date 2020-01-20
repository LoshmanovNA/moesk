import configparser

from seleniumbase import BaseCase
from ..locators import CommonLocators


class BasePage(BaseCase):
    """
    CommonPage наследует все методы фреймворка BaseCase.
    Другие страницы (pages) будут наследовать CommonPage
    чтобы иметь доступ к методам общих для всех страниц элементов
    и методам фреймворка BaseCase
    """
    common_locators = CommonLocators()

    def setUp(self):
        super(BasePage, self).setUp()
        config = Config()
        # For global environment use config['GLOBAL']
        env = config[self.env.upper()]  # Берем значение заданного окружения (TEST, PRODUCTION, etc)
        self.app_url = env['app_url']
        self.user_login_fl = env['existing_user_fl']
        self.user_login_ul = env['existing_user_ul']
        self.user_login_ip = env['existing_user_ip']
        self.user_pass = env['password']

    def should_be_main_page_lk(self):
        """Проверка успешной авторизации"""
        self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)


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

    def get_global_variable(self):
        return self._env['GLOBAL']
