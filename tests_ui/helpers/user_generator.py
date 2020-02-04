from faker import Faker
from ..models.user_model import UserModel


class UserGenerator:
    """
    Содержит методы генерации валидных и невалидных данных для регистрации пользователя
    """

    def __init__(self):
        self.faker = Faker(['ru_RU', 'en_US'])
        self.fake_ru = self.faker['ru_RU']
        self.fake_en = self.faker['en_US']

    def fake_user(self, user_model):
        valid_data = self.fake_valid_data()
        user_model.first_name = valid_data['valid_first_name']
        user_model.last_name = valid_data['valid_last_name']
        user_model.patronymic_name = valid_data['valid_patronymic_name']
        user_model.phone = valid_data['valid_phone']
        user_model.email = valid_data['valid_email']
        return user_model

    def fake_valid_data(self):
        """Список с валидными значениями для формы регистрации"""
        return {
            'first_name': self.fake_ru.first_name_male(),
            'last_name': self.fake_ru.last_name_male(),
            'patronymic_name': self.fake_ru.middle_name_male(),
            'phone': '99851234567',
            'email': self.fake_ru.email()
        }

    def fake_invalid_data(self):
        return {'first_name': [self.fake_ru.first_name_male().lower(),
                               self.fake_ru.first_name_male().upper(),
                               self.fake_en.first_name_male(),
                               ''],

                'last_name': [self.fake_ru.last_name_male().lower(),
                              self.fake_ru.last_name_male().upper(),
                              self.fake_en.last_name_male(),
                              ''],

                'patronymic_name': [self.fake_ru.middle_name_male().lower(),
                                    self.fake_ru.middle_name_male().upper(),
                                    self.fake_en.name_male(),
                                    ''],

                'phone': ['1234567890', '47224567890', '!#$!%!@', ''],

                'email': ['plainaddress', 'email.example.com', 'email@example', '']}

    def generate_invalid_user_model(self, user_model):
        valid_data = self.fake_valid_data()
        result = valid_data.copy()
        for parameters in self.fake_invalid_data():
            for values in parameters:

