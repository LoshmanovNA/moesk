from ..pages.registration_page import RegistrationPage
from ..helpers.user_generator import UserGenerator
from ..models.user_model import UserModel
from parameterized import parameterized
import pytest


class TestRegistrationPage(RegistrationPage):
    """Тест создания новой учетной записи"""

    def test_registration_form(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие новой записи в БД, удаляем новую УЗ из БД
        """
        self.user = UserGenerator().fake_user(self.user_data)
        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=self.user.first_name,
                                       last_name=self.user.last_name,
                                       patronymic_name=self.user.patronymic_name,
                                       phone=self.user.phone,
                                       email=self.user.email)
        self.should_be_confirm_page()
        self.connect.should_be_new_record_into_db(self.user.email, 'email', 'users')

    def tearDown(self):
        self.connect.delete_new_account_from_db(self.user.email)
        super(TestRegistrationPage, self).tearDown()


class TestValidationRegistrationPage(RegistrationPage):
    """Проверка валидации полей и чекбоксов формы регистрации"""
    _generator = UserGenerator()

    @parameterized.expand(_generator.fake_invalid_registration_data())
    @pytest.mark.negative
    def test_registration_form_fields_validation(self, *args):
        user = UserModel(*args)
        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=user.first_name,
                                       last_name=user.last_name,
                                       patronymic_name=user.patronymic_name,
                                       phone=user.phone,
                                       email=user.email)
        self.check_fields_validation()

    @parameterized.expand([
        (False, True),
        (True, False),
    ])
    @pytest.mark.negative
    def test_registration_form_checkbox_validation(self, param1, param2):
        user = UserGenerator().fake_user(self.user_data)
        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=user.first_name,
                                       last_name=user.last_name,
                                       patronymic_name=user.patronymic_name,
                                       phone=user.phone,
                                       email=user.email,
                                       check_box_1=param1,
                                       check_box_2=param2)
        self.check_checkboxes_validation()
