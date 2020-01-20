from faker import Faker


def fake_user(arr):
    f = Faker('ru_RU')
    arr.update({'first_name': f.first_name(),
                'last_name': f.last_name(),
                'patronymic': f.middle_name(),
                'phone': '9851234567',
                'email': f.email()})
    return arr



