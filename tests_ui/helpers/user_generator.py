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

    def valid_user(self, user_model):
        valid_data = self.fake_valid_data()
        user_model.first_name = valid_data['first_name']
        user_model.last_name = valid_data['last_name']
        user_model.patronymic_name = valid_data['patronymic_name']
        user_model.phone = valid_data['phone']
        user_model.email = valid_data['email']
        return user_model

    def invalid_user(self):
        """Генерация пользователя с одним невалидным параметром"""
        valid_data = self.fake_valid_data()
        invalid_data = self.fake_invalid_data()

        for key in valid_data.keys():  # Проходим по каждому ключу в словаре valid_data. Названия ключей - это названия полей формы регистрации
            user_data = valid_data.copy()  # Создаем чистую копию валидных данных
            if key in invalid_data.keys():  # Если поле из валидных данных присутствует в невалидных данных, то
                user_data['negative_param'] = key  # создаем ключ, в значении которого будет названиее невалидного поля.
                # Название ключа соответствуе атрибуту класса user model
                for value in invalid_data[key]:  # Берем невалидный вариант определенного поля
                    user_data[key] = value   # И перезаписываем валидное значение. Получается словарь с одним невалидным полем среди остальных валидных
                    yield [UserModel(**user_data)]  # распаковываем словарь в модель пользователя, названия ключей соответствуют атрибутам класса,
                    # затем выплевываем модель в декоратор параметризации и переходим к следующему невалидному значению поля, а затем к следующему полю

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
