
class RegistrationFormErrors:

    def __init__(self,
                 first_name,
                 last_name,
                 patronymic_name,
                 phone,
                 email,
                 confirm_1,
                 confirm_2):

        first_name = 'Обязательное поле'
        last_name = 'Обязательное поле'
        patronymic_name = 'Обязательное поле'
        email = 'Некорректный электронный адрес'
        phone = 'Обязательное поле, формат +7 (9xx) xxxxxxx'
        confirm_1 = 'Обязательное поле'
        confirm_2 = 'Обязательное поле'
