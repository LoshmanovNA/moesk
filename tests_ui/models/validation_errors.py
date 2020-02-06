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

    def expected_validation_errors(self):
        self.first_name = 'Обязательное поле'
        self.last_name = 'Обязательное поле'
        self.patronymic_name = 'Обязательное поле'
        self.email = 'Некорректный электронный адрес'
        self.phone = 'Обязательное поле, формат +7 (9xx) xxxxxxx'
        self.confirm_1 = 'Обязательное поле'
        self.confirm_2 = 'Обязательное поле'
