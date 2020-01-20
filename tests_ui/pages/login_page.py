from .base_page import BasePage
from ..locators import LoginPageLocators


class LoginPage(BasePage):
    """Действия на странице логина"""
    login_page_locators = LoginPageLocators()

    def login_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.get(self.app_url)
        self.update_text(self.login_page_locators.LOGIN_INPUT_EMAIL_CSS, login)
        self.update_text(self.login_page_locators.LOGIN_INPUT_PASS_CSS, password)
        self.click(self.login_page_locators.LOGIN_SUBMIT_BUTTON_CSS)
