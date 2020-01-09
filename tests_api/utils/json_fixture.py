class JSONFixture:

    @staticmethod
    def authorization(login, password):
        json = {
            "login": login,
            "password": password
        }
        return json

    @staticmethod
    def registration_new_fl():
        json = {
            "user_type": "person",
            "name": "Петр",
            "surname": "Петров",
            "patronymic": "Петрович",
            "email": "123@mail.mail",
            "phone": "+79991234567",
            "password": "!Q2w3e4r5t"
        }
        return json
