from ..pages.registration_page import RegistrationPage


class TestRegistrationPage(RegistrationPage):
    """Тест создания новой учетной записи"""

    def test_registration_form(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
        """
        self.open(self.env)
        self.fill_registration_form_fl(self.reg_phone, self.reg_name, self.reg_surname,
                                       self.reg_patronymic, self.reg_email)
        self.should_be_confirm_page()
