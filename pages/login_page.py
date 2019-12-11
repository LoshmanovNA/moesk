from .locators import LoginPageLocators, RegisterPageLocators, BasePageLocators
from .. import data
from seleniumbase.core.mysql import DatabaseManager
from seleniumbase import BaseCase
import datetime


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

    def fill_registration_form_fl(self):
        """Проверка регистрации заявителя вида ФЛ (Физ. лицо)"""
        # Берем тестовую почту из файла с данными
        test_email = data.test_email
        # Переходим по ссылке для регистрации
        self.click(LoginPageLocators.REGISTER_LINK)
        # Открываем выпадающий список Тип пользователя
        self.click(RegisterPageLocators.USER_TYPE_LIST)
        # Выбираем тип пользователя ФЛ
        self.click(RegisterPageLocators.USER_TYPE_FL, 'By.XPATH')
        # Вводим данные пользователя
        self.update_text(RegisterPageLocators.PHONE, '79999999999')
        self.update_text(RegisterPageLocators.NAME, 'Тест')
        self.update_text(RegisterPageLocators.SURNAME, 'Тест')
        self.update_text(RegisterPageLocators.PATRONYMIC, 'Тест')
        self.update_text(RegisterPageLocators.EMAIL, test_email)
        # Ставим чек-боксы
        self.js_click(RegisterPageLocators.CONFIRM1)
        self.js_click(RegisterPageLocators.CONFIRM2)
        # Кликаем кнопку продолжения регистрации
        self.click(RegisterPageLocators.NEXT_STEP, timeout=3)

    def should_be_confirm_page(self):
        url = self.get_current_url()
        expected_text = 'email_sent'
        assert expected_text in url, f"Message: {url} not contains {expected_text}"

    def activate_new_account(self):
        time = datetime.datetime.isoformat  # пример формата 2014-04-21 06:53:34
        sql = 'UPDATE users ' \
              'SET confirmed_at=time, confirmation_sent_at=time, sms_confirmed_at=dt, first_password_changed=1' \
              'WHERE email=%s'
        value = data.test_email
        connect = DatabaseManager()
        connect.execute_query()








