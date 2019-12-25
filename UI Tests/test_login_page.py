from .pages.login_page import LoginPage


class TestLoginPage(LoginPage):

    # def test_login_existed_user(self):
    #     """
    #     Авторизация под существующим пользователем и
    #     и проверка нахождения на главной странице ЛК
    #     """
    #     self.open(self.env)  # Выбираем окружение (параметр --env. По умолчанию тест)
    #     self.login_user(d.fl, d.password)  # Вводим логин и пароль из файла data
    #     self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль

    def test_registration_form_fl(self):
        self.open(self.env)
        self.fill_registration_form_fl()
        self.should_be_confirm_page()


