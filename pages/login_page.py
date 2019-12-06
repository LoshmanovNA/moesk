from seleniumbase import BaseCase
from .locators import LoginPageLocators as LPL, RemindPasswordLocators as RPL


class LoginPage(BaseCase):
    """Действия на странице логина"""
    def login_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.update_text(LPL.LOGIN_INPUT, login)
        self.update_text(LPL.PASS_INPUT, password)
        self.click(LPL.SUBMIT_BUTTON)

    def should_be_main_page_lk(self):





