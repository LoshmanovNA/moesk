from seleniumbase import BaseCase
from .locators import LoginPageLocators, RegisterPageLocators, BasePageLocators
from seleniumbase.core.mysql import DatabaseManager


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

    def fill_registration_form_fl(self, phone, name, surname, patronymic, email):
        """Проверка регистрации заявителя вида ФЛ (Физ. лицо)"""
        # Переходим по ссылке для регистрации
        self.click(LoginPageLocators.REGISTER_LINK)
        # Открываем выпадающий список Тип пользователя
        self.click(RegisterPageLocators.USER_TYPE_LIST)
        # Выбираем тип пользователя ФЛ
        self.click(RegisterPageLocators.USER_TYPE_FL, 'By.XPATH')
        # Вводим данные пользователя
        self.update_text(RegisterPageLocators.PHONE, phone)
        self.update_text(RegisterPageLocators.NAME, name)
        self.update_text(RegisterPageLocators.SURNAME, surname)
        self.update_text(RegisterPageLocators.PATRONYMIC, patronymic)
        self.update_text(RegisterPageLocators.EMAIL, email)
        # Ставим чек-боксы
        self.js_click(RegisterPageLocators.CONFIRM1)
        self.js_click(RegisterPageLocators.CONFIRM2)
        # Кликаем кнопку продолжения регистрации
        self.click(RegisterPageLocators.NEXT_STEP, timeout=3)

    def should_be_confirm_page(self):
        """Проверяем, что находимся на странице с информацией об отправке email"""
        url = self.get_current_url()  # Получаем текущий url
        expected_text = 'email_sent'
        assert expected_text in url, f"Message: {url} not contains {expected_text}"

    def should_be_new_record_at_db(self, email):
        connect = DatabaseManager()
        sql = "SELECT email FROM users WHERE email=%s"
        row = connect.query_fetch_one(sql, email)
        assert row[0] == email # Проверка не отрабатывает!!!

    def delete_new_record(self, email):
        """Удаляем запись о созданной УЗ из БД и проверяем, что email не найден"""
        connect = DatabaseManager()
        sql = "DELETE FROM users WHERE email=%s"
        connect.execute_query(sql, email)
        assert not self.should_be_new_record_at_db(email)
