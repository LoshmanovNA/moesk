from faker import Faker


class UserGenerator:

    def __init__(self):
        self.first_name = 'first_name'
        self.last_name = 'last_name'
        self.patronymic_name = 'patronymic_name'
        self.phone = 'phone'
        self.email = 'email'
        self.authentication_token = 'token'

    def fake_user(self):
        f = Faker('ru_RU')
        self.first_name = f.first_name()
        self.last_name = f.last_name()
        self.patronymic_name = f.middle_name()
        self.phone = '89851234567'
        self.email = f.email()
