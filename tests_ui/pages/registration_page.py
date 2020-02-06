from ..models.validation_errors import RegistrationFormErrorsModel
from ..locators import LoginPageLocators, RegistrationPageLocators
from ..pages.base_page import BasePage

import allure


class RegistrationPage(BasePage):
    """Действия на странице регистрации"""
    _login_page_locators = LoginPageLocators()
    _registration_page_locators = RegistrationPageLocators()

    @allure.step
    def click_registration_button(self):
        # Переходим по ссылке для регистрации
        self.click(self._login_page_locators.LOGIN_REGISTER_LINK_CSS)

    @allure.step
    def fill_registration_form_fl(self, user_model):
        """Заполнение формы регистрации заявителя вида ФЛ (Физ. лицо)"""
        # Открываем выпадающий список Тип пользователя
        self.click(self._registration_page_locators.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя ФЛ
        self.click(self._registration_page_locators.REGISTRATION_USER_TYPE_FL_XPATH, 'By.XPATH')
        # Вводим данные пользователя
        self.update_text(self._registration_page_locators.REGISTRATION_NAME_CSS, user_model.first_name)
        self.update_text(self._registration_page_locators.REGISTRATION_SURNAME_CSS, user_model.last_name)
        self.update_text(self._registration_page_locators.REGISTRATION_PATRONYMIC_CSS, user_model.patronymic_name)
        self.update_text(self._registration_page_locators.REGISTRATION_EMAIL_CSS, user_model.email)
        self.update_text(self._registration_page_locators.REGISTRATION_PHONE_CSS, user_model.phone)

    @allure.step
    def actions_with_required_checkboxes(self, check_box_1=True, check_box_2=True):
        # Ставим чек-боксы
        if check_box_1:
            self.js_click(self._registration_page_locators.REGISTRATION_CONFIRM1_CSS)
        if check_box_2:
            self.js_click(self._registration_page_locators.REGISTRATION_CONFIRM2_CSS)

    @allure.step
    def continue_registration(self):
        # Кликаем кнопку продолжения регистрации
        self.click(self._registration_page_locators.REGISTRATION_NEXT_STEP_CSS)

    @allure.step
    def should_be_confirm_page(self):
        """Проверяем, что находимся на странице с информацией об отправке email"""
        url = self.get_current_url()  # Получаем текущий url
        expected_text = 'email_sent'
        assert expected_text in url, f"Message: {url} not contains {expected_text}"

    @allure.step
    def get_actual_validation_errors(self, field):
        """Проверяем наличие ошибки валидации поля"""
        actual_validation_error = RegistrationFormErrorsModel()
        registration_form = self._registration_page_locators.REGISTRATION_VALIDATION_ERROR_MESSAGES_XPATH
        error_message = self.find_element(registration_form[field])
        if error_message:
            actual_validation_error.__dict__[field] = self.get_text(error_message)

        return actual_validation_error

    @allure.step
    def get_expected_validation_errors(self):
        """Доделать"""
        expected_validation_errors = RegistrationFormErrorsModel().expected_validation_errors()
        reg_form_elements = self._registration_page_locators.REGISTRATION_VALIDATION_ERROR_MESSAGES_XPATH.items()

        for field, element in reg_form_elements:
            if not self.find_element(element):
                expected_validation_errors.__dict__[field] = None
        return expected_validation_errors

    @allure.step
    def check_fields_validation(self, expected_errors, actual_errors):
        for field in expected_errors.__dict__.keys():
            if expected_errors.__dict__[field] != actual_errors.__dict__[field]:
                print(f"{expected_errors.__dict__[field]} !== {actual_errors.__dict__[field]}")
                return False

    # @allure.step
    # def check_checkboxes_validation(self):
    #     """Проверяем наличие ошибки валидации чек-бокса"""
    #     self.assert_element(self._registration_page_locators.REGISTRATION_CHECKBOX_VALIDATION_CSS)
