from ..data import TestData as TD
from ..pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("registration")
class TestLoginPage():
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""

    def test_login_user(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """
        print('\nDo some test')
        # self.open(self.env)  # Выбираем окружение (параметр --env. По умолчанию тест)
        # self.login_user(TD.email, TD.password)  # Вводим логин и пароль из файла data
        # self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль
