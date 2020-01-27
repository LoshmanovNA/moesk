from faker import Faker


class UserGenerator:

    @staticmethod
    def fake_user(user_data):
        f = Faker('ru_RU')

        user_data.first_name = f.first_name_male()
        user_data.last_name = f.last_name_male()
        user_data.patronymic_name = f.middle_name_male()
        user_data.phone = '99851234567'
        user_data.email = f.email()
        return user_data



