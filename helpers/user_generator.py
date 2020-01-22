from faker import Faker


class UserGenerator:

    def __init__(self):
        self.first_name = 'first_name'
        self.last_name = 'last_name'
        self.patronymic = 'patronymic'
        self.phone = 'phone'
        self.email = 'email'

    def fake_user(self):
        f = Faker('ru_RU')
        self.first_name = f.first_name()
        self.last_name = f.last_name()
        self.patronymic = f.middle_name()
        self.phone = '89851234567'
        self.email = f.email()
