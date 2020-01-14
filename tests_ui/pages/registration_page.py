from .base_page import BasePage
from ..locators import LoginPageLocators, RegistrationPageLocators


class RegistrationPage(BasePage):
    """Действия на странице регистрации"""
    login_page_locators = LoginPageLocators()
    registration_page_locators = RegistrationPageLocators()

    def fill_registration_form_fl(self, phone='phone', name='name', surname='surname',
                                  patronymic='patronymic', email='email'):
        """Проверка регистрации заявителя вида ФЛ (Физ. лицо)"""
        # Переходим по ссылке для регистрации
        self.click(self.login_page_locators.LOGIN_REGISTER_LINK_CSS)
        # Открываем выпадающий список Тип пользователя
        self.click(self.registration_page_locators.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя ФЛ
        self.click(self.registration_page_locators.REGISTRATION_USER_TYPE_FL_XPATH, 'By.XPATH')
        # Вводим данные пользователя
        self.update_text(self.registration_page_locators.REGISTRATION_PHONE_CSS, phone)
        self.update_text(self.registration_page_locators.REGISTRATION_NAME_CSS, name)
        self.update_text(self.registration_page_locators.REGISTRATION_SURNAME_CSS, surname)
        self.update_text(self.registration_page_locators.REGISTRATION_PATRONYMIC_CSS, patronymic)
        self.update_text(self.registration_page_locators.REGISTRATION_EMAIL_CSS, email)
        # Ставим чек-боксы
        self.js_click(self.registration_page_locators.REGISTRATION_CONFIRM1_CSS)
        self.js_click(self.registration_page_locators.REGISTRATION_CONFIRM2_CSS)
        # Кликаем кнопку продолжения регистрации
        self.click(self.registration_page_locators.REGISTRATION_NEXT_STEP_CSS)

    def should_be_confirm_page(self):
        """Проверяем, что находимся на странице с информацией об отправке email"""
        url = self.get_current_url()  # Получаем текущий url
        expected_text = 'email_sent'
        assert expected_text in url, f"Message: {url} not contains {expected_text}"
