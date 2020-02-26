from ..pages import *


class TestNewConnectionClaim(ClaimsThirdStepPage):

    def test_claim_new_connection_fl(self):
        self.login_user(self.config_data.user_login_fl,
                        self.config_data.password)
        self.start_new_tp_claim()
        self.click_accept_warning_button()
        self.go_through_first_step_new_connection()
        self.go_through_second_step_new_connection()
        self.go_through_third_step_new_connection()

    def test_claim_new_connection_ul(self):
        self.login_user(self.config_data.user_login_ul,
                        self.config_data.password)
        self.start_new_tp_claim()
        self.click_accept_warning_button()
        self.go_through_first_step_new_connection()
        self.go_through_second_step_new_connection()
        self.go_through_third_step_new_connection()

    def test_claim_new_connection_ip(self):
        self.login_user(self.config_data.user_login_ip,
                        self.config_data.password)
        self.start_new_tp_claim()
        self.click_accept_warning_button()
        self.go_through_first_step_new_connection()
        self.go_through_second_step_new_connection()
        self.go_through_third_step_new_connection()


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
#
#     def test_claim_new_connection_representative(self):
#         self.login_user(self.config_data.user_login_representative,
#                         self.config_data.password)
#         self.start_new_tp_claim()
#         self.click_accept_warning_button()
#         self.select_claim_type_temporary_connection()
#         self.click_next_step()
