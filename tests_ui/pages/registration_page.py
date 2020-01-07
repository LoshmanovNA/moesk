from .base_page import BasePage
from ..locators import RegisterPageLocators, LoginPageLocators


class RegistrationPage(BasePage):
    """Действия на странице регистрации"""
    def fill_registration_form_fl(self, phone='phone', name='name', surname='surname',
                                  patronymic='patronymic', email='email'):
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
        self.click(RegisterPageLocators.NEXT_STEP)

    def should_be_confirm_page(self):
        """Проверяем, что находимся на странице с информацией об отправке email"""
        url = self.get_current_url()  # Получаем текущий url
        expected_text = 'email_sent'
        assert expected_text in url, f"Message: {url} not contains {expected_text}"
