class RegistrationFormErrorsModel:

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 patronymic_name=None,
                 phone=None,
                 email=None,
                 company_full_name=None,
                 company_short_name=None,
                 confirm_1=None,
                 confirm_2=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
        self.email = email
        self.phone = phone
        self.company_full_name = company_full_name
        self.company_short_name = company_short_name
        self.confirm_1 = confirm_1
        self.confirm_2 = confirm_2

    @staticmethod
    def expected_validation_errors():
        validation_types = {
                'invalid': 'С заглавной буквы, только кириллица',
                'empty': 'Обязательное поле'
            }
        return RegistrationFormErrorsModel(
            first_name=validation_types,
            last_name=validation_types,
            patronymic_name=validation_types,
            company_full_name='Обязательное поле',
            company_short_name='Обязательное поле',
            email='Некорректный электронный адрес',
            phone='Обязательное поле, формат +7 (9xx) xxxxxxx',
            confirm_1='Обязательное поле',
            confirm_2='Обязательное поле')
