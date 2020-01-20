from ..pages.login_page import LoginPage


class TestLoginPage(LoginPage):
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""

    def test_login_user(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """

        self.login_user(self.user_login_fl, self.user_pass)  # Вводим логин и пароль
        self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль
