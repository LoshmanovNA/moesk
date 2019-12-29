from ..data import TestData as TD
from ..pages.registration_page import RegistrationPage
from ..pages.data_base import DataBase
import pytest


class TestRegistrationPage(RegistrationPage, DataBase):
    """Тест создания новой учетной записи"""

    @pytest.fixture(scope="session", autouse=True)
    def test_registration_form(self, request):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
        """
        self.open(self.env)
        self.fill_registration_form_fl(TD.phone, TD.name, TD.surname, TD.patronymic, TD.email)
        self.should_be_confirm_page()
        self.should_be_new_record_at_db(TD.email)
        self.activate_new_account_at_db()
        request.addfinalizer(self.delete_new_record_from_db(TD.email))
