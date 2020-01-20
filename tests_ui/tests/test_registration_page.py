from ..pages.registration_page import RegistrationPage
from helpers.user_generator import fake_user

# Для хранения данных о новом пользователе
user_data = {'first_name': '',
             'last_name': '',
             'patronymic': '',
             'phone': '',
             'email': ''}


class TestRegistrationPage(RegistrationPage):
    """Тест создания новой учетной записи"""

    def setUp(self):
        super(TestRegistrationPage, self).setUp()
        fake_user(user_data)

    def test_registration_form(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
        """
        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=user_data['first_name'],
                                       last_name=user_data['last_name'],
                                       patronymic=user_data['patronymic'],
                                       phone=user_data['phone'],
                                       email=user_data['email'])
        self.should_be_confirm_page()
