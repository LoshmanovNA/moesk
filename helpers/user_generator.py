from faker import Faker


class UserGenerator:

    def __init__(self,
                 first_name,
                 last_name,
                 patronymic_name,
                 phone,
                 email):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
        self.phone = phone
        self.email = email

    @classmethod
    def fake_user(cls):
        f = Faker('ru_RU')
        first_name = f.first_name()
        last_name = f.last_name()
        patronymic_name = f.middle_name()
        phone = '99851234567'
        email = f.email()
        return cls(first_name, last_name, patronymic_name, phone, email)
