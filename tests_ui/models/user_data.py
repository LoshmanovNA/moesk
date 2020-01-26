

class UserData:
    def __init__(self,
                 first_name=None,
                 last_name=None,
                 patronymic_name=None,
                 phone=None,
                 email=None,
                 user_login_fl=None,
                 user_login_ul=None,
                 user_login_ip=None,
                 password=None,
                 pass_hash=None):

        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
        self.phone = phone
        self.email = email
        self.user_login_fl = user_login_fl
        self.user_login_ul = user_login_ul
        self.user_login_ip = user_login_ip
        self.password = password
        self.pass_hash = pass_hash
