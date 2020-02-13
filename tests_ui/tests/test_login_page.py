from ..pages.login_page import LoginPage
from ..pages.registration_page import RegistrationPage
from ..helpers.user_generator import UserGenerator
from ..models.user_model import UserModel

import pytest


@pytest.mark.existing_user
@pytest.mark.test_env
@pytest.mark.production_env
class TestLoginExistingUser(LoginPage):
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""

    def test_login_existing_user(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """
        self.get(self.app_url)
        self.login_user(self.config_data.user_login_fl,
                        self.config_data.password)  # Вводим логин и пароль
        self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль


@pytest.mark.new_user
@pytest.mark.test_env
class TestLoginNewUser(LoginPage, RegistrationPage):
    """
    Тест логина нового пользователя с предварительной
    регистрацией и удалением записи из БД после теста
    """

    def setUp(self):
        """Генерируем данные для нового пользователя и выполняем регистрацию"""
        super(TestLoginNewUser, self).setUp()
        self.new_user_data = UserGenerator().valid_user(UserModel)  # Генерируем класс с тестовыми данными для регистрации

        self.click_registration_button()
        self.fill_registration_form_fl(self.new_user_data)
        self.actions_with_required_checkboxes()
        self.continue_registration()
        self.should_be_confirm_page()  # Проверяем, что находимся на странице подтверждения успешной регистрации
        self.connect.activate_new_account_db(self.new_user_data.email,
                                             self.config_data.pass_hash)  # Активируем УЗ заполнением нужных полей в БД

    def test_login_new_user(self):
        """Авторизация под новым пользователем и проверка нахождения на главной странице ЛК"""
        login = self.new_user_data.email  # Сгенерированный в setUp email
        password = self.config_data.password  # Пароль из конфига

        self.get(self.app_url)
        self.login_user(login, password)
        self.should_be_main_page_lk()

    def tearDown(self):
        """Удаляем запись с новой УЗ из БД"""
        self.connect.delete_new_account_from_db(self.new_user_data.email)
        super(TestLoginNewUser, self).tearDown()
