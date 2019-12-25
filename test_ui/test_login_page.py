from .pages.login_page import LoginPage
from . import data as d
from faker import Faker


class TestLoginPage(LoginPage):
    """Тестируем авторизацию под существующим пользователем и регистрацию нового физ.лица"""

    # def test_login_existed_user(self):
    #     """
    #     Авторизация под существующим пользователем и
    #     и проверка нахождения на главной странице ЛК
    #     """
    #     self.open(self.env)  # Выбираем окружение (параметр --env. По умолчанию тест)
    #     self.login_user(d.fl, d.password)  # Вводим логин и пароль из файла data
    #     self.should_be_main_page_lk()  # Проверям главную страницу путем поиска ссылки на профиль

    def test_registration_form_fl(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ
        """
        f = Faker('ru-RU')
        phone = '89998887766'
        name = f.first_name()
        surname = f.last_name()
        patronymic = f.last_name()
        email = f.email()
        self.open(self.env)
        self.fill_registration_form_fl(phone, name, surname, patronymic, email)
        self.should_be_confirm_page()
        self.should_be_new_record_at_db(email)
        self.delete_new_record(email)



