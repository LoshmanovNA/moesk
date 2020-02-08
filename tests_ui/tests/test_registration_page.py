from ..pages.registration_page import RegistrationPage
from ..helpers.user_generator import UserGenerator
from ..models.user_model import UserModel
from ..models.validation_errors import RegistrationFormErrorsModel
from parameterized import parameterized
import pytest


# class TestRegistrationPage(RegistrationPage):
#     """Тест создания новой учетной записи"""
#
#     def test_registration_form(self):
#         """
#         Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
#         подтверждения регистрации, проверяем наличие новой записи в БД, удаляем новую УЗ из БД
#         """
#         self.user = UserGenerator().valid_user()(self.user_data)
#         self.click_registration_button()
#         self.fill_registration_form_fl(self.user)
#         self.actions_with_required_checkboxes()
#         self.continue_registration()
#         self.should_be_confirm_page()
#         if self.env == 'test':
#             self.connect.should_be_new_record_into_db(self.user.email, 'email', 'users')
#
#     def tearDown(self):
#         if self.env == 'test':
#             self.connect.delete_new_account_from_db(self.user.email)
#         super(TestRegistrationPage, self).tearDown()


class TestValidationRegistrationPage(RegistrationPage):
    """Проверка валидации полей и чекбоксов формы регистрации"""
    _generator = UserGenerator()

    @parameterized.expand(_generator.invalid_user())
    @pytest.mark.negative
    def test_registration_form_fields_validation(self, user):
        # self.logger.info(user.__dict__.items())
        self.click_registration_button()
        self.fill_registration_form_fl(user)
        self.actions_with_required_checkboxes()
        self.continue_registration()
        if not self.compare_actual_and_expected_validation_errors(
                self.get_actual_validation_errors(error_model=RegistrationFormErrorsModel),
                self.get_expected_validation_errors(field=user.invalid_field,
                                                    validation_type=user.validation_type,
                                                    error_model=RegistrationFormErrorsModel)):
            self.soft_assert(status=False, log_message=f"Сообщение об ошибке валидации в поле {user.invalid_field} некорректно")

    # @parameterized.expand([
    #     (False, True),
    #     (True, False),
    # ])
    # @pytest.mark.negative
    # def test_registration_form_checkbox_validation(self, param1, param2):
    #     user = UserGenerator().fake_user(self.user_data)
    #     self.click_registration_button(self)
    #     self.fill_registration_form_fl(user)
    #     self.actions_with_required_checkboxes()
    #     self.continue_registration()
    #     self.check_checkboxes_validation()
