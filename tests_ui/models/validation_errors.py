class RegistrationFormErrorsModel:

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 patronymic_name=None,
                 phone=None,
                 email=None,
                 confirm_1=None,
                 confirm_2=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
        self.email = email
        self.phone = phone
        self.confirm_1 = confirm_1
        self.confirm_2 = confirm_2

    @staticmethod
    def expected_validation_errors():
        return {
            'first_name': {
                'invalid': 'С заглавной буквы, только кириллица',
                'empty': 'Обязательное поле',
            },
            'last_name': {
                'invalid': 'С заглавной буквы, только кириллица',
                'empty': 'Обязательное поле'
            },
            'patronymic_name': {
                'invalid': 'С заглавной буквы, только кириллица',
                'empty': 'Обязательное поле'
            },
            'email': 'Некорректный электронный адрес',
            'phone': 'Обязательное поле, формат +7 (9xx) xxxxxxx',
            'confirm_1': 'Обязательное полее',
            'confirm_2': 'Обязательное поле'
        }
