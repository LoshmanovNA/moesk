from ..data import TestData as TD
from ..pages.login_page import LoginPage


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
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
        """
        self.open(self.env)
        self.fill_registration_form_fl(TD.phone, TD.name, TD.surname, TD.patronymic, TD.email)
        self.should_be_confirm_page()
        self.should_be_new_record_at_db(TD.email)
        self.delete_new_record(TD.email)



