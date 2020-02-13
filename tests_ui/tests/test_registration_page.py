from ..pages.registration_page import RegistrationPage
from ..helpers.user_generator import UserGenerator
from ..models.user_model import UserModel
from ..models.validation_errors import RegistrationFormErrorsModel
from parameterized import parameterized
import pytest


@pytest.mark.test_env
@pytest.mark.production_env
class TestRegistrationPage(RegistrationPage):
    """Тест создания новой учетной записи"""

    def test_registration_form(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие новой записи в БД, удаляем новую УЗ из БД
        """
        self.new_user_data = UserGenerator().valid_user(UserModel)
        self.click_registration_button()
        self.fill_registration_form_fl(self.new_user_data)
        self.actions_with_required_checkboxes()
        self.continue_registration()
        self.should_be_confirm_page()
        if self.env == 'production':
            self.should_be_confirmation_email()
        if self.env == 'test':
            self.connect.should_be_new_record_into_db(self.new_user_data.email, 'email', 'users')

    def tearDown(self):
        if self.env == 'test':
            self.connect.delete_new_account_from_db(self.new_user_data.email)
        super(TestRegistrationPage, self).tearDown()


@pytest.mark.test_env
@pytest.mark.production_env
class TestValidationRegistrationPage(RegistrationPage):
    """Проверка валидации полей и чекбоксов формы регистрации"""
    _generator = UserGenerator()

    @parameterized.expand(_generator.generate_negative_params())
    @pytest.mark.negative
    def test_registration_form_validation(self, user):
        # self.logger.info(user.__dict__.items())
        self.click_registration_button()
        self.fill_registration_form_fl(user)
        self.actions_with_required_checkboxes(check_box_1=user.confirm_1,
                                              check_box_2=user.confirm_2)
        self.continue_registration()

        if not self.compare_actual_and_expected_input_validation_errors(
                self.get_actual_validation_errors(error_model=RegistrationFormErrorsModel),
                self.get_expected_validation_errors(field=user.invalid_field,
                                                    validation_type=user.validation_type)):
            self.soft_assert(status=False, log_message=f"Сообщение об ошибке валидации в поле {user.invalid_field} некорректно")
