
class UserModel:
    """Параметры для создания нового пользователя"""

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 patronymic_name=None,
                 phone=None,
                 email=None,
                 user_login_fl=None,
                 user_login_ul=None,
                 user_login_ip=None,
                 user_login_representative=None,
                 password=None,
                 pass_hash=None,
                 company_full_name=None,
                 company_short_name=None,
                 invalid_field=None,
                 validation_type=None,
                 confirm_1=None,
                 confirm_2=None):

        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
        self.phone = phone
        self.email = email
        self.user_login_fl = user_login_fl
        self.user_login_ul = user_login_ul
        self.user_login_ip = user_login_ip
        self.user_login_representative = user_login_representative
        self.password = password
        self.pass_hash = pass_hash
        self.company_full_name = company_full_name
        self.company_short_name = company_short_name
        self.invalid_field = invalid_field
        self.validation_type = validation_type
        self.confirm_1 = confirm_1
        self.confirm_2 = confirm_2

