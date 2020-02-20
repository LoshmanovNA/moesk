from ..models import RegistrationFormErrorsModel
from ..locators import LoginPageLocators, RegistrationPageLocators
from .base_page import BasePage
from ..helpers import Mailbox
from selenium.common.exceptions import NoSuchElementException

import allure


class RegistrationPage(BasePage):
    """Действия на странице регистрации"""
    _login_page = LoginPageLocators()
    _reg_page = RegistrationPageLocators()

    @allure.step
    def click_registration_button(self):
        # Переходим по ссылке для регистрации
        self.click(self. _login_page.LOGIN_REGISTER_LINK_CSS)

    @allure.step
    def select_user_type_fl(self):
        # Открываем выпадающий список Тип пользователя
        self.click(self._reg_page.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя ФЛ
        self.click(self._reg_page.REGISTRATION_USER_TYPE_FL_XPATH, 'By.XPATH')

    @allure.step
    def select_user_type_ul(self):
        # Открываем выпадающий список Тип пользователя
        self.click(self._reg_page.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя ЮЛ
        self.click(self._reg_page.REGISTRATION_USER_TYPE_UL_XPATH, 'By.XPATH')

    @allure.step
    def select_user_type_ip(self):
        # Открываем выпадающий список Тип пользователя
        self.click(self._reg_page.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя ИП
        self.click(self._reg_page.REGISTRATION_USER_TYPE_IP_XPATH, 'By.XPATH')

    @allure.step
    def select_user_type_representative(self):
        # Открываем выпадающий список Тип пользователя
        self.click(self._reg_page.REGISTRATION_USER_TYPE_LIST_CSS)
        # Выбираем тип пользователя Представитель по доверенности
        self.click(self._reg_page.REGISTRATION_USER_TYPE_PPD_XPATH, 'By.XPATH')

    @allure.step
    def fill_registration_form(self, user_model):
        """Заполнение формы регистрации"""
        
        # Заполняем поля ФИО в зависимости от типа заявителя
        try:
            # Если тип пользователя Физическое лицо или Представитель по доверенности
            if self.is_text_visible('Физическое лицо') or self.is_text_visible('Представитель по доверенности'):
                self.update_text(self._reg_page.REGISTRATION_FIRST_NAME_CSS, user_model.first_name)
                self.update_text(self._reg_page.REGISTRATION_LAST_NAME_CSS, user_model.last_name)
                self.update_text(self._reg_page.REGISTRATION_PATRONYMIC_CSS, user_model.patronymic_name)
                
            # Если тип пользователя Юридическое лицо
            elif self.is_text_visible('Юридическое лицо'):
                self.update_text(self._reg_page.REGISTRATION_UL_FULL_NAME_CSS, user_model.company_full_name)
                self.update_text(self._reg_page.REGISTRATION_UL_SHORT_NAME_CSS, user_model.company_short_name)
                self.update_text(self._reg_page.REGISTRATION_CONTACT_FIRST_NAME_CSS, user_model.first_name)
                self.update_text(self._reg_page.REGISTRATION_CONTACT_LAST_NAME_CSS, user_model.last_name)
                self.update_text(self._reg_page.REGISTRATION_CONTACT_PATRONYMIC_NAME_CSS, user_model.patronymic_name)

            # Если тип пользователя ИП
            elif self.is_text_visible('Индивидуальный предприниматель'):
                self.update_text(self._reg_page.REGISTRATION_IP_FIRST_NAME_CSS, user_model.first_name)
                self.update_text(self._reg_page.REGISTRATION_IP_LAST_NAME_CSS, user_model.last_name)
                self.update_text(self._reg_page.REGISTRATION_IP_PATRONYMIC_NAME_CSS, user_model.patronymic_name)
                self.update_text(self._reg_page.REGISTRATION_CONTACT_FIRST_NAME_CSS, user_model.first_name)
                self.update_text(self._reg_page.REGISTRATION_CONTACT_LAST_NAME_CSS, user_model.last_name)
                self.update_text(self._reg_page.REGISTRATION_CONTACT_PATRONYMIC_NAME_CSS, user_model.patronymic_name)
        except:
            raise NoSuchElementException('Наименование типа заявителя не найдено на странице '
                                         'или некорректные локаторы полей ФИО')
        
        # Заполняем поле телефона
        self.update_text(self._reg_page.REGISTRATION_PHONE_CSS, user_model.phone)
        
        # Заполняем поле адреса электронной почты
        if self.env == 'production':
            # Если проверка на проде, то отправляем письмо на временную почту
            self.temp_mail = Mailbox('')  # Временная почта: <random value>@1secmail.com
            self.update_text(self._reg_page.REGISTRATION_EMAIL_CSS, self.temp_mail.email())
            self.logger.info(self.temp_mail.email())
        else:
            # Если на тесте, то генерируем фейковый валидный email
            self.update_text(self._reg_page.REGISTRATION_EMAIL_CSS, user_model.email)

    @allure.step
    def actions_with_required_checkboxes(self, check_box_1=True, check_box_2=True):
        # Ставим чек-боксы
        if check_box_1:
            self.js_click(self._reg_page.REGISTRATION_CONFIRM1_CSS)
        if check_box_2:
            self.js_click(self._reg_page.REGISTRATION_CONFIRM2_CSS)

    @allure.step
    def continue_registration(self):
        # Кликаем кнопку продолжения регистрации
        self.click(self._reg_page.REGISTRATION_NEXT_STEP_CSS)

    @allure.step
    def should_be_confirm_page(self):
        """Проверяем, что находимся на странице с информацией об отправке email"""
        url = self.get_current_url()  # Получаем текущий url
        expected_text = 'email_sent'
        assert expected_text in url, f"Ссылка {url} не содержит текст '{expected_text}'"

    @allure.step
    def should_be_confirmation_email(self):
        confirmation_link = self.temp_mail.get_link('utp.moesk.ru', 'Подтверждение e-mail')
        self.logger.info(confirmation_link)
        assert 'confirmation_token' in confirmation_link, f"Ссылка {confirmation_link} не содержит токен "

    @allure.step
    def get_actual_validation_errors(self, error_model):
        """Проверяем наличие ошибки валидации поля"""
        registration_form_elements = self._reg_page.REGISTRATION_VALIDATION_ERROR_MESSAGES_XPATH.items()
        actual_error_model = error_model()
        for field_name, element_with_error_message in registration_form_elements:
            if self.is_element_present(element_with_error_message, 'By.XPATH'):
                actual_error_model.__dict__[field_name] = self.get_text(element_with_error_message, 'By.XPATH')
        # self.logger.info(actual_error_model.__dict__.items())
        return actual_error_model

    @allure.step
    def get_expected_validation_errors(self, field, validation_type):
        expected_error_model = RegistrationFormErrorsModel()
        all_expected_validation_errors_dict = RegistrationFormErrorsModel.expected_validation_errors().__dict__
        if validation_type:
            expected_error_message = all_expected_validation_errors_dict[field][validation_type]
            expected_error_model.__dict__[field] = expected_error_message
        else:
            expected_error_message = all_expected_validation_errors_dict[field]
            expected_error_model.__dict__[field] = expected_error_message
            # self.logger.info(expected_error_model.__dict__.items())
        return expected_error_model

    @allure.step
    def compare_actual_and_expected_input_validation_errors(self, actual_errors, expected_errors):
        for field in expected_errors.__dict__.keys():
            if expected_errors.__dict__[field] != actual_errors.__dict__[field]:
                self.logger.info(f"ОЖИДАЛОСЬ: {expected_errors.__dict__[field]}, ПОЛУЧЕНО: {actual_errors.__dict__[field]}")
                return False
        return True
