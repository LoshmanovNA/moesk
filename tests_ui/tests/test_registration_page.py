from ..pages.registration_page import RegistrationPage
from ..helpers.user_generator import UserGenerator


class TestRegistrationPage(RegistrationPage):
    """Тест создания новой учетной записи"""

    def setUp(self):
        super(TestRegistrationPage, self).setUp()
        self.user = UserGenerator.fake_user(self.user_data)

    def test_registration_form(self):
        """
        Генерируем тестовые данные и регистрируем пользователя типа ФЛ, проверям страницу
        подтверждения регистрации, проверяем наличие нового email в БД, удаляем новую УЗ из БД
        """
        self.get(self.app_url)
        self.fill_registration_form_fl(first_name=self.user.first_name,
                                       last_name=self.user.last_name,
                                       patronymic_name=self.user.patronymic_name,
                                       phone=self.user.phone,
                                       email=self.user.email)
        self.should_be_confirm_page()
