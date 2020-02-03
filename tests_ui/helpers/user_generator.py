from faker import Faker


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
        valid_data = {
            'valid_first_name': self.fake_ru.first_name_male(),
            'valid_last_name': self.fake_ru.last_name_male(),
            'valid_patronymic_name': self.fake_ru.middle_name_male(),
            'valid_phone': '99851234567',
            'valid_email': self.fake_ru.email()
        }
        return valid_data

    def fake_invalid_data(self):
        """Список с невалидными значениями для формы регистрации"""
        invalid_data = {
            'invalid_first_name': [self.fake_ru.first_name_male().lower(),
                                   self.fake_ru.first_name_male().upper(),
                                   self.fake_en.first_name_male(),
                                   ''],
            'invalid_last_name': [self.fake_ru.last_name_male().lower(),
                                  self.fake_ru.last_name_male().upper(),
                                  self.fake_en.last_name_male(),
                                  ''],
            'invalid_patronymic_name': [self.fake_ru.middle_name_male().lower(),
                                        self.fake_ru.middle_name_male().upper(),
                                        self.fake_en.name_male(),
                                        ''],
            'invalid_phone': ['1234567890', '47224567890', ''],
            'invalid_email': ['plainaddress', 'email.example.com', 'email@example', '']
        }
        return invalid_data

    def fake_invalid_registration_data(self):
        """Генерирует кортежи, в которых поочередно каждый параметр формы регистрации имеет невалидное значение"""
        valid_params_lst = [v for v in self.fake_valid_data().values()]
        invalid_params_lst = [v for v in self.fake_invalid_data().values()]

        for i in range(len(valid_params_lst)):
            result = [item for item in valid_params_lst]
            for j in invalid_params_lst[i]:
                result.pop(i)
                result.insert(i, j)
                yield tuple(result)
