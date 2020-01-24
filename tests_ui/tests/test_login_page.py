import pytest

from ..pages.login_page import LoginPage
from ..pages.registration_page import RegistrationPage
from ...helpers.db_actions import DataBase
from ...helpers.user_generator import UserGenerator


@pytest.mark.existing_user
class TestLoginExistingUser(LoginPage):
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""

    def test_login_existing_user(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """
        self.login_user(self.user_login_fl, self.user_pass)  # Вводим логин и пароль
        self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль


@pytest.mark.new_user
class TestLoginNewUser(LoginPage, RegistrationPage):

    def setUp(self):
        super(TestLoginNewUser, self).setUp()
        #selef.user_data =
        self.user = UserGenerator()
        self.user.fake_user()

        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=self.user.first_name,
                                       last_name=self.user.last_name,
                                       patronymic_name=self.user.patronymic_name,
                                       phone=self.user.phone,
                                       email=self.user.email)
        self.should_be_confirm_page()

        self.db = DataBase()
        self.db.activate_new_account_db(self.user.email, self.user_pass_hash)

    def test_login_new_user(self):
        login = self.user.email  # Сгенерированный в setUp email
        password = self.user_pass  # Пароль из конфига
        self.get(self.app_url)
        self.login_user(login, password)
        self.should_be_main_page_lk()

    def tearDown(self):
        self.db.delete_new_account_from_db(self.user.email)
        super(TestLoginNewUser, self).tearDown()
