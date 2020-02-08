import logging

from collections.abc import Iterable
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
        self.logger = logging.getLogger(__name__)

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

        for field in invalid_data.keys():  # Проходим по каждому ключу в словаре invalid_data. Названия ключей - это названия полей формы регистрации
            user_data = valid_data.copy()  # Создаем чистую копию валидных данных
            if field in valid_data.keys():  # Если поле из невалидных данных присутствует в валидных данных, то
                user_data['invalid_field'] = field  # создаем ключ, в значении которого будет названиее невалидного поля. Название ключа соответствуе атрибуту класса user model

                if not isinstance(invalid_data[field], dict):  # Проверяем есть ли у ключа в значении словарь с типами ошибок
                    if not isinstance(invalid_data[field], str) and isinstance(invalid_data[field], Iterable):  # Если в значении итерируемый объект, но не строка
                        for invalid_value in invalid_data[field]:  # Перебираем значения итерируемого объекта
                            user_data[field] = invalid_value  # И перезаписываем валидное значение невалидным. Получается словарь с одним невалидным полем среди остальных валидных
                            yield [UserModel(**user_data)]  # распаковываем словарь в модель пользователя, названия ключей соответствуют атрибутам класса
                    else:
                        user_data[field] = invalid_data[field]  # Если в значении строка
                        yield [UserModel(**user_data)]
                else:
                    for validation_type, invalid_value in invalid_data[field].items():  # Если ключ содержит в значении словарь с типами валидации
                        user_data['validation_type'] = validation_type  # То создаем в словаре с данными для модели пользователя новый ключ с типом валидации который потом передадим в модель
                        # self.logger.info(invalid_data[field].items())
                        if not isinstance(invalid_value, str) and isinstance(invalid_value, Iterable):

                            for value in invalid_value:  # Перебираем значения в value каждого типа валидации
                                user_data[field] = value  # и замеянем ими валидное значение проверяемого поля
                                # self.logger.info(user_data.items())
                                yield [UserModel(**user_data)]
                        else:
                            user_data[field] = invalid_value
                            # self.logger.info(user_data.items())
                            yield [UserModel(**user_data)]

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
        return {'first_name': {'invalid': [self.fake_ru.first_name_male().lower(),
                                           self.fake_ru.first_name_male().upper(),
                                           self.fake_en.first_name_male()],
                               'empty': ''
                               },

                'last_name': {'invalid': [self.fake_ru.last_name_male().lower(),
                                          self.fake_ru.last_name_male().upper(),
                                          self.fake_en.last_name_male()],
                              'empty': ''
                              },

                'patronymic_name': {'invalid': [self.fake_ru.middle_name_male().lower(),
                                                self.fake_ru.middle_name_male().upper(),
                                                self.fake_en.name_male()],
                                    'empty': ''
                                    },

                'phone': ['1234567890', '47224567890', '!#$!%!@', ''],

                'email': ['plainaddress', 'email.example.com', 'email@example', '']}
