from ..locators import LoginPageLocators, RegistrationPageLocators
from ..pages.base_page import BasePage

import allure


class RegistrationPage(BasePage):
    """Действия на странице регистрации"""
    _login_page_locators = LoginPageLocators()
    _registration_page_locators = RegistrationPageLocators()

    @allure.step
    def fill_registration_form_fl(self, first_name='name', last_name='surname',
                                  patronymic_name='patronymic', email='email', phone='phone',
                                  check_box_1=True, check_box_2=True):
        """Проверка регистрации заявителя вида ФЛ (Физ. лицо)"""
        # Переходим по ссылке для регистрации
        self.click(self._login_page_locators.LOGIN_REGISTER_LINK_CSS)
        # Открываем выпадающий список Тип пользователя
        self.click(self._registration_page_locators.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя ФЛ
        self.click(self._registration_page_locators.REGISTRATION_USER_TYPE_FL_XPATH, 'By.XPATH')
        # Вводим данные пользователя
        self.update_text(self._registration_page_locators.REGISTRATION_NAME_CSS, first_name)
        self.update_text(self._registration_page_locators.REGISTRATION_SURNAME_CSS, last_name)
        self.update_text(self._registration_page_locators.REGISTRATION_PATRONYMIC_CSS, patronymic_name)
        self.update_text(self._registration_page_locators.REGISTRATION_EMAIL_CSS, email)
        self.update_text(self._registration_page_locators.REGISTRATION_PHONE_CSS, phone)
        # Ставим чек-боксы
        if check_box_1:
            self.js_click(self._registration_page_locators.REGISTRATION_CONFIRM1_CSS)
        if check_box_2:
            self.js_click(self._registration_page_locators.REGISTRATION_CONFIRM2_CSS)
        # Кликаем кнопку продолжения регистрации
        self.click(self._registration_page_locators.REGISTRATION_NEXT_STEP_CSS)

    @allure.step
    def should_be_confirm_page(self):
        """Проверяем, что находимся на странице с информацией об отправке email"""
        url = self.get_current_url()  # Получаем текущий url
        expected_text = 'email_sent'
        assert expected_text in url, f"Message: {url} not contains {expected_text}"

    # @allure.step
    # def check_fields_validation(self):
    #     """Проверяем наличие ошибки валидации поля"""
    #     self.find_element(self._registration_page_locators.REGISTRATION_FIELD_VALIDATION_CSS)
    #
    # @allure.step
    # def check_checkboxes_validation(self):
    #     """Проверяем наличие ошибки валидации чек-бокса"""
    #     self.assert_element(self._registration_page_locators.REGISTRATION_CHECKBOX_VALIDATION_CSS)
