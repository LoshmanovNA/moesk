from ..pages.new_tp_claim_pages import FirstStepTP
from ..pages import MainPage, WarningPage, LoginPage


class TestNewConnectionClaimFl(FirstStepTP, MainPage, WarningPage, LoginPage):

    def test_new_connection_claim_fl(self):
        self.login_user(self.config_data.user_login_fl,
                        self.config_data.password)
        self.start_new_tp_claim()
        self.click_accept_warning_button()
        self.click_next_step()
