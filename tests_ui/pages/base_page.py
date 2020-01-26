from config import Config
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
        print(env)
        self.app_url = env['app_url']
        self.user_login_fl = env['existing_user_fl']
        self.user_login_ul = env['existing_user_ul']
        self.user_login_ip = env['existing_user_ip']
        self.user_pass = env['password']
        self.user_pass_hash = env['pass_hash']

    def should_be_main_page_lk(self):
        """Проверка успешной авторизации"""
        if 'assets/sprite.png' in self.get_current_url():
            self.click(self.common_locators.COMMON_MAIN_LOGO_CSS)
            self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)
        else:
            self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)


