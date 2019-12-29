from .base_page import BasePage
from ..locators import LoginPageLocators


class LoginPage(BasePage):
    """Действия на странице логина"""
    def login_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.update_text(LoginPageLocators.LOGIN_INPUT, login)
        self.update_text(LoginPageLocators.PASS_INPUT, password)
        self.click(LoginPageLocators.SUBMIT_BUTTON)
