from .pages.login_page import LoginPage
from . import data as d


class TestLoginPage(LoginPage):

    def test_login(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """
        self.open(self.env)  # Выбираем окружение (параметр --env. По умолчанию тест)
        self.login_user(d.fl, d.password)  # Вводим логин и пароль из файла data
        self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль

