from ..pages.login_page import LoginPage


class TestLoginPage(LoginPage):
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""
    # Пример изменения действия перед и после тестов
    def setUp(self, masterqa_mode=False):
        super(TestLoginPage, self).setUp()
        print('\nStart tests')

    def tearDown(self):
        super(TestLoginPage, self).tearDown()
        print('\nFinish tests')

    def test_login_user(self):
        """
        Авторизация под существующим пользователем и
        и проверка нахождения на главной странице ЛК
        """
        self.login_user(self.user_email, self.user_pass)  # Вводим логин и пароль из файла data
        self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль
