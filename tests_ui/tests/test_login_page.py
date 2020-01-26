from ..pages.login_page import LoginPage
from ..pages.registration_page import RegistrationPage
from ..helpers.user_generator import UserGenerator

import pytest


@pytest.mark.existing_user
class TestLoginExistingUser(LoginPage):
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""

    def test_login_existing_user(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """
        self.get(self.app_url)
        self.login_user(self.user_data.user_login_fl,
                        self.user_data.password)  # Вводим логин и пароль
        self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль


@pytest.mark.new_user
class TestLoginNewUser(LoginPage, RegistrationPage):

    def setUp(self):
        super(TestLoginNewUser, self).setUp()
        self.new_user = UserGenerator.fake_user(self.user_data)

        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=self.new_user.first_name,
                                       last_name=self.new_user.last_name,
                                       patronymic_name=self.new_user.patronymic_name,
                                       phone=self.new_user.phone,
                                       email=self.new_user.email)
        self.should_be_confirm_page()
        self.connect.activate_new_account_db(self.new_user.email,
                                             self.user_data.pass_hash)

    def test_login_new_user(self):
        login = self.new_user.email  # Сгенерированный в setUp email
        password = self.user_data.password  # Пароль из конфига

        self.get(self.app_url)
        self.login_user(login, password)
        self.should_be_main_page_lk()

    def tearDown(self):
        self.connect.delete_new_account_from_db(self.new_user.email)
        self.connect
        super(TestLoginNewUser, self).tearDown()
