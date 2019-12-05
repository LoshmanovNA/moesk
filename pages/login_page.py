from seleniumbase import BaseCase
from .locators import LoginPageLocators as LPL, RemindPasswordLocators as RPL


class LoginPage(BaseCase):
    """Действия на странице логина"""
    def login_existing_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.update_text(LPL.LOGIN_INPUT, login)
        self.update_text(LPL.PASS_INPUT, password)
        self.click(LPL.SUBMIT_BUTTON)

    def restore_password(self):
        """Восстановление пароля"""
        # Делаем запрос на восстановление пароля
        self.click(LPL.REMIND_PASS_BUTTON)
        self.update_text(RPL.USER_EMAIL)
        self.click(RPL.SEND_BUTTON)
        # Идем в почтовый ящик, проверяем что письмо пришло и переходим по ссылке




