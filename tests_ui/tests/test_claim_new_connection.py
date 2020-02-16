from ..pages import ClaimsFirstStepPage
from ..pages import MainPage, WarningPage, LoginPage


class TestNewConnectionClaim(ClaimsFirstStepPage, MainPage, WarningPage, LoginPage):

    def test_claim_new_connection_fl(self):
        self.login_user(self.config_data.user_login_fl,
                        self.config_data.password)
        self.start_new_tp_claim()
        self.click_accept_warning_button()
        self.click_next_step()

    # def test_claim_new_connection_ul(self):
    #     self.login_user(self.config_data.user_login_ul,
    #                     self.config_data.password)
    #     self.start_new_tp_claim()
    #     self.click_accept_warning_button()
    #     self.click_next_step()
    #
    # def test_claim_new_connection_ip(self):
    #     self.login_user(self.config_data.user_login_ip,
    #                     self.config_data.password)
    #     self.start_new_tp_claim()
    #     self.click_accept_warning_button()
    #     self.click_next_step()
    #

# class TestTemporaryConnectionClaim(ClaimsFirstStepPage, MainPage, WarningPage, LoginPage):
#
#     def test_claim_temp_connection_fl(self):
#         self.login_user(self.config_data.user_login_fl,
#                         self.config_data.password)
#         self.start_new_tp_claim()
#         self.click_accept_warning_button()
#         self.select_claim_type_temporary_connection()
#         self.click_next_step()
#
#     def test_claim_new_connection_ul(self):
#         self.login_user(self.config_data.user_login_ul,
#                         self.config_data.password)
#         self.start_new_tp_claim()
#         self.click_accept_warning_button()
#         self.select_claim_type_temporary_connection()
#         self.click_next_step()
#
#     def test_claim_new_connection_ip(self):
#         self.login_user(self.config_data.user_login_ip,
#                         self.config_data.password)
#         self.start_new_tp_claim()
#         self.click_accept_warning_button()
#         self.select_claim_type_temporary_connection()
#         self.click_next_step()
