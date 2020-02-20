from ..pages import ClaimsFirstStepPage, ClaimsSecondStepPage, MainPage, WarningPage, LoginPage


class TestNewConnectionClaim(ClaimsSecondStepPage):

    # def test_claim_new_connection_fl(self):
    #     self.login_user(self.config_data.user_login_fl,
    #                     self.config_data.password)
    #     self.start_new_tp_claim()
    #     self.click_accept_warning_button()
    #     self.go_to_second_step()
    #     self.fill_date_of_birth()
    #     self.choose_document_type(passport=True)
    #     self.fill_passport_data_and_snils()
    #     self.fill_registration_address_form(region='Московская', city=None)
    #     self.fact_and_reg_addresses_are_equal(equal=True)
    #     self.fill_fact_address_form(region='Москва', city=None)
    #     self.deactivate_sms_notification_checkbox()
    #     self.proxy_checkbox(state=False)
    #     self.go_to_third_step()

    # def test_claim_new_connection_ul(self):
    #     self.login_user(self.config_data.user_login_ul,
    #                     self.config_data.password)
    #     self.start_new_tp_claim()
    #     self.click_accept_warning_button()
    #     self.go_to_second_step()
    #     self.fill_requisites_form()
    #     self.fill_registration_address_form(region=None, city=None)
    #     self.fact_and_reg_addresses_are_equal(equal=True)
    #     self.fill_fact_address_form(region=None, city=None)
    #     self.deactivate_sms_notification_checkbox()
    #     self.proxy_checkbox(state=True)
    #     self.go_to_third_step()

    def test_claim_new_connection_ip(self):
        self.login_user(self.config_data.user_login_ip,
                        self.config_data.password)
        self.start_new_tp_claim()
        self.click_accept_warning_button()
        self.go_to_second_step()
        self.fill_requisites_form()
        self.fill_registration_address_form(region='Московская', city='Балашиха')
        self.fact_and_reg_addresses_are_equal(equal=False)
        self.fill_fact_address_form(region=None, city=None)
        self.deactivate_sms_notification_checkbox()
        self.proxy_checkbox(state=True)
        self.go_to_third_step()


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
