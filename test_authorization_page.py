from seleniumbase import BaseCase


class TestAuthorizationPage(BaseCase):

    def test_authorization(self):
        self.open('https://lk.moesk.ru/users/sign_in')
        self.update_text('#user_email', 'user@user.user')
        self.update_text('#user_password', '!Q2w3e4r5t')
        self.click('button.yellow-btn')
        self.assert_element('a.profile-link')