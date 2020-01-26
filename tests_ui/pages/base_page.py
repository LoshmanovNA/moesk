from seleniumbase import BaseCase
from ..helpers.db_actions import DBManager
from ..locators import CommonLocators
from ..models.db_model import DBModel
from ..models.user_data import UserData
from ...config_loader import Config


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

        # Создание соединения с БД
        db = DBModel(env['db_host'],
                     env['db_username'],
                     env['db_password'],
                     env['db_schema'],
                     int(env['db_port']))
        self.connect = DBManager(db)
        # Данные тестового пользователя
        self.user_data = UserData(user_login_fl=env['existing_user_fl'],
                                  user_login_ul=env['existing_user_ul'],
                                  user_login_ip=env['existing_user_ip'],
                                  password=env['password'],
                                  pass_hash=env['pass_hash'])

    def tearDown(self):
        self.connect.close_db()
        super(BasePage, self).tearDown()

    def should_be_main_page_lk(self):
        """Проверка успешной авторизации"""
        if 'assets/sprite.png' in self.get_current_url():
            self.click(self.common_locators.COMMON_MAIN_LOGO_CSS)
            self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)
        else:
            self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)


