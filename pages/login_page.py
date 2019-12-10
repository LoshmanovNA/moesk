from seleniumbase import BaseCase
from .locators import LoginPageLocators, RegisterPageLocators, BasePageLocators
from faker import Faker


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
        fake = Faker()
        email = fake.email()  # Генерируем почту для регистрации пользователя
        print(email, '\n')
        # Переходим по ссылке для регистрации
        self.click(LoginPageLocators.REGISTER_LINK)
        # Открываем выпадающий список Тип пользователя
        self.click(RegisterPageLocators.USER_TYPE_LIST)
        # Выбираем тип пользователя ФЛ
        self.click(RegisterPageLocators.USER_TYPE_FL, 'By.XPATH')
        # Вводим данные пользователя
        self.update_text(RegisterPageLocators.NAME, 'Тест')
        self.update_text(RegisterPageLocators.SURNAME, 'Тест')
        self.update_text(RegisterPageLocators.PATRONYMIC, 'Тест')
        self.update_text(RegisterPageLocators.EMAIL, email)
        self.update_text(RegisterPageLocators.PHONE, '9999999999')
        # Ставим чек-боксы
        self.js_click(RegisterPageLocators.CONFIRM1)
        self.js_click(RegisterPageLocators.CONFIRM2)
        # Кликаем кнопку продолжения регистрации
        self.click(RegisterPageLocators.NEXT_STEP)

    def test_query(self, db_query):
        print(db_query)




