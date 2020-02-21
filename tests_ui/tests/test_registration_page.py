from ..pages import RegistrationPage
from ..helpers import UserGenerator
from ..models import RegistrationFormErrorsModel
from parameterized import parameterized
import pytest


@pytest.mark.test_env
@pytest.mark.production_env
@pytest.mark.smoke
class TestRegistrationPage(RegistrationPage):
    """Тест создания новой учетной записи"""

    def common_registration_actions(self, user_data):
        """Общие методы для заполнения формы регистрации заявителя любого вида"""
        self.fill_registration_form(user_data)
        self.actions_with_required_checkboxes()
        self.continue_registration()
        self.should_be_confirm_page()
        if self.env == 'production':
            self.should_be_confirmation_email()
        if self.env == 'test':
            self.connect.should_be_new_record_into_db(user_data.email, 'email', 'users')
            self.connect.delete_new_account_from_db(user_data.email)

    def test_registration_form_fl(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие новой записи в БД, удаляем новую УЗ из БД
        """
        self.new_user_data = UserGenerator().valid_user()
        self.click_registration_button()
        self.select_user_type_fl()
        self.common_registration_actions(self.new_user_data)

    def test_registration_form_ul(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ЮЛ, проверям страницу
        подтверждения регистрации. Если прод - проверяем наличие письма, если тест - проверяем наличие
        новой записи в БД и удаляем ее из БД
        """
        self.new_user_data = UserGenerator().valid_user()
        self.click_registration_button()
        self.select_user_type_ul()
        self.common_registration_actions(self.new_user_data)

    def test_registration_form_ip(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие новой записи в БД, удаляем новую УЗ из БД
        """
        self.new_user_data = UserGenerator().valid_user()
        self.click_registration_button()
        self.select_user_type_ip()
        self.common_registration_actions(self.new_user_data)

    def test_registration_form_representative(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие новой записи в БД, удаляем новую УЗ из БД
        """
        self.new_user_data = UserGenerator().valid_user()
        self.click_registration_button()
        self.select_user_type_representative()
        self.common_registration_actions(self.new_user_data)


@pytest.mark.test_env
@pytest.mark.production_env
@pytest.mark.negative
class TestValidationRegistrationPage(RegistrationPage):
    """Проверка валидации полей и чекбоксов формы регистрации"""

    def common_registration_actions(self, user):
        """Общие методы для заполнения формы регистрации заявителя любого вида"""
        self.fill_registration_form(user)
        self.actions_with_required_checkboxes(check_box_1=user.confirm_1,
                                              check_box_2=user.confirm_2)
        self.continue_registration()

        if not self.compare_actual_and_expected_input_validation_errors(
                self.get_actual_validation_errors(error_model=RegistrationFormErrorsModel),
                self.get_expected_validation_errors(field=user.invalid_field,
                                                    validation_type=user.validation_type)):
            self.soft_assert(status=False, log_message=f"Сообщение об ошибке валидации в "
                                                       f"поле {user.invalid_field} некорректно")

    @parameterized.expand(UserGenerator().generate_negative_params())
    def test_registration_form_validation_fl(self, user):
        """Тест валидации формы регистрации физ. лица"""
        # self.logger.info(user.__dict__.items())
        self.click_registration_button()
        self.select_user_type_fl()
        self.common_registration_actions(user)

    @parameterized.expand(UserGenerator().generate_negative_params(company=True))
    def test_registration_form_validation_ul(self, user):
        """Тест валидации формы регистрации юр. лица"""
        # self.logger.info(user.__dict__.items())
        self.click_registration_button()
        self.select_user_type_ul()
        self.common_registration_actions(user)

    @parameterized.expand(UserGenerator().generate_negative_params())
    def test_registration_form_validation_ip(self, user):
        """Тест валидации формы регистрации ИП"""
        self.logger.debug(user.__dict__.items())
        self.click_registration_button()
        self.select_user_type_ip()
        self.common_registration_actions(user)

    @parameterized.expand(UserGenerator().generate_negative_params())
    def test_registration_form_validation_representative(self, user):
        """Тест валидации формы регистрации представителя по доверенности"""
        self.logger.debug(user.__dict__.items())
        self.click_registration_button()
        self.select_user_type_representative()
        self.common_registration_actions(user)

