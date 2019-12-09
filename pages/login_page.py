from seleniumbase import BaseCase
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BaseCase):
    """Действия на странице логина"""

    def login_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.update_text(LoginPageLocators.LOGIN_INPUT, login)
        self.update_text(LoginPageLocators.PASS_INPUT, password)
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def should_be_main_page_lk(self):
        """Проверка успешной авторизации"""
        self.assert_element(BasePageLocators.PROFILE_LINK)

    def registration_form(self):
        pass




