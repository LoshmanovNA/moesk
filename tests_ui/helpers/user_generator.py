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

    def valid_user(self, model):
        return model(first_name=self.fake_ru.first_name_male(),
                     last_name=self.fake_ru.last_name_male(),
                     patronymic_name=self.fake_ru.middle_name_male(),
                     phone='99851234567',
                     email=self.fake_ru.email(),
                     confirm_1=True,
                     confirm_2=True)

    def invalid_user(self, model):
        return model(first_name={'invalid': [self.fake_ru.first_name_male().lower(),
                                             self.fake_ru.first_name_male().upper(),
                                             self.fake_en.first_name_male()],
                                 'empty': ''
                                 },
                     last_name={'invalid': [self.fake_ru.last_name_male().lower(),
                                            self.fake_ru.last_name_male().upper(),
                                            self.fake_en.last_name_male()],
                                'empty': ''
                                },
                     patronymic_name={'invalid': [self.fake_ru.middle_name_male().lower(),
                                                  self.fake_ru.middle_name_male().upper(),
                                                  self.fake_en.name_male()],
                                      'empty': ''
                                      },
                     phone=['1234567890', '47224567890', '!#$!%!@', ''],
                     email=['plainaddress', 'email.example.com', 'email@example', ''],
                     confirm_1=False,
                     confirm_2=False)

    def generate_negative_params(self):
        """Генерация пользователя с одним невалидным параметром"""
        valid_data = self.valid_user(UserModel).__dict__
        invalid_data = self.invalid_user(UserModel).__dict__

        def negative_user_model(field_name, field_value, valid_type=None):
            """
            Создает модель пользователя с валидными данными,
            заменяет валидное значение для указанного поля (field_name) невалидным значением (field_value)
            При наличии, записывает в модель тип валидации validation_type
            """
            model = self.valid_user(UserModel)
            model.invalid_field = field_name
            model.__dict__[field_name] = field_value
            if valid_type:
                model.validation_type = valid_type
            # self.logger.info(model.__dict__.items())
            return [model]

        for field in invalid_data.keys():  # Проходим по каждому ключу в модели invalid_data, приведенной к словарю.
            # Названия ключей - это названия полей формы регистрации
            if field in valid_data.keys() and invalid_data[field] is not None:  # Если поле из модели невалидных данных
                # присутствует в модели валидных данных, то
                if not isinstance(invalid_data[field], dict):  # Если проверяемое поле не предусматривает разделения на
                    # типы возможных ошибок валидации (не содержит в value словарь с типами ошибок)
                    if not isinstance(invalid_data[field], str) and isinstance(invalid_data[field], Iterable):  # Если в
                        # value итерируемый объект, но не строка
                        for invalid_value in invalid_data[field]:  # Перебираем значения итерируемого объекта
                            yield negative_user_model(field_name=field,
                                                      field_value=invalid_value)
                    else:  # Если строка или неитерируемый тип
                        yield negative_user_model(field_name=field,
                                                  field_value=invalid_data[field])
                else:  # Если проверяемое поле предусматривает разделения на типы ошибок валидации
                    for validation_type, invalid_value in invalid_data[field].items():  # Перебираем каждый тип
                        # валидации

                        if not isinstance(invalid_value, str) and isinstance(invalid_value, Iterable):  # Если в
                            # значении у ключа итерируемый объект, но не строка
                            for value in invalid_value:  # Перебираем значения в value у типа валидации
                                yield negative_user_model(field_name=field,
                                                          field_value=value,
                                                          valid_type=validation_type)
                        else:  # Если в значении ключа строка или неитерируемый объект
                            yield negative_user_model(field_name=field,
                                                      field_value=invalid_value,
                                                      valid_type=validation_type)
