from tests_ui.data import TestData as TD
from tests_ui.pages.registration_page import RegistrationPage
from tests_ui.pages.data_base import DataBase
import pytest


@pytest.fixture
def registration():

    """
    Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
    подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
    """
    rp = RegistrationPage()
    db = DataBase()
    rp.driver(rp.env)
    # rp.fill_registration_form_fl(TD.phone, TD.name, TD.surname, TD.patronymic, TD.email)
    # rp.should_be_confirm_page()
    # db.should_be_new_record_at_db(TD.email)
    # db.activate_new_account_at_db()
    # yield registration
    # db.delete_new_record_from_db(TD.email)
    print('\nStart')
    yield registration
    print('\nFinish')

