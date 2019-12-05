from seleniumbase import BaseCase
from .pages import login_page
from . import data


class TestAuthorizationPage(BaseCase):

    def test_authorization(self):
        self.open(data.lk_prod)
        self.assert_element('a.profile-link')
