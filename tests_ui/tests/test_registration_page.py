from ..pages.registration_page import RegistrationPage
from ..pages.data_base import DataBase


class TestRegistrationPage(RegistrationPage, DataBase):
    """Тест создания новой учетной записи"""

    def test_registration_form(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
        """
        self.open(self.env)
        self.fill_registration_form_fl(TD.phone, TD.name, TD.surname, TD.patronymic, TD.email)
        self.should_be_confirm_page()
