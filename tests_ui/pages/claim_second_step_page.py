import allure

from .claim_first_step_page import ClaimsFirstStepPage
from ..locators import ClaimsSecondStepLocators
from ..models import ClaimModel
from .base_elements import BaseElements


class ClaimsSecondStepPage(ClaimsFirstStepPage, BaseElements):
    _second_step = ClaimsSecondStepLocators()
    _claim_model = ClaimModel()

    @allure.step
    def fill_date_of_birth(self):
        self.update_text(self._second_step.SECOND_STEP_BIRTH_DATE_CSS, self._claim_model.user_date_birth)
        self.click(self._second_step.SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS)

    @allure.step
    def choose_document_type(self, passport=True):
        if passport:
            self.click(self._second_step.SECOND_STEP_DOCUMENT_TYPE_PASSPORT_XPATH, 'By.XPATH')
        else:
            self.click(self._second_step.SECOND_STEP_DOCUMENT_TYPE_OTHER_XPATH)
            self.select_option_by_value(self._second_step.SECOND_STEP_DOC_TYPES_DROPDOWN_CSS,
                                        self._second_step.SECOND_STEP_FOREIGN_PASSPORT_VALUE)
            self.update_text(self._second_step.SECOND_STEP_OTHER_DOC_INFO_CSS, self._claim_model.user_other_document)

    @allure.step
    def fill_passport_data_and_snils(self):
        passport_seria_locator = self._second_step.SECOND_STEP_PASSPORT_SERIA_CSS
        passport_code_locator = self._second_step.SECOND_STEP_PASSPORT_CODE_CSS
        passport_date_locator = self._second_step.SECOND_STEP_PASSPORT_DATE_CSS
        passport_issued = self._second_step.SECOND_STEP_PASSPORT_ISSUED_CSS
        snils_locator = self._second_step.SECOND_STEP_USER_SNILS_CSS
        dropdown_calendar_locator = self._second_step.SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS
        if self.is_element_visible(passport_seria_locator):
            self.update_text(passport_seria_locator,
                             self._claim_model.user_passport_number)
            self.update_text(passport_code_locator,
                             self._claim_model.user_passport_code)
            self.update_text(passport_date_locator,
                             self._claim_model.user_passport_date)
            self.click(dropdown_calendar_locator)
            self.update_text(passport_issued,
                             self._claim_model.user_passport_issued)
        if self.is_element_visible(snils_locator):
            self.update_text(snils_locator,
                             self._claim_model.user_fl_snils)

    @allure.step
    def fill_requisites_form(self):
        egrip_field = self._second_step.SECOND_STEP_EGRIP_CSS
        egrul_field = self._second_step.SECOND_STEP_EGRUL_CSS
        kpp_field = self._second_step.SECOND_STEP_KPP_CSS
        if self.is_element_present(egrip_field):
            self.update_text(egrip_field, self._claim_model.user_ip_egrip)
        if self.is_element_present(egrul_field):
            self.update_text(egrul_field, self._claim_model.user_ul_egrul_num)
        if self.is_element_present(kpp_field):
            self.update_text(kpp_field, self._claim_model.user_ul_kpp)
        self.update_text(self._second_step.SECOND_STEP_REESTR_DATE_CSS, self._claim_model.user_reestr_date)
        self.update_text(self._second_step.SECOND_STEP_INN_CSS, self._claim_model.user_inn)
        self.update_text(self._second_step.SECOND_STEP_RS_CSS, self._claim_model.user_rs)
        self.update_text(self._second_step.SECOND_STEP_BIK_CSS, self._claim_model.user_bik)
        self.update_text(self._second_step.SECOND_STEP_BANK_CSS, self._claim_model.user_bank)

    @allure.step
    def fill_registration_address_form(self, region=None, city=None):
        self.fill_address_form(clear_button_locator=self._second_step.SECOND_STEP_CLEAR_REG_ADDRESS_BUTTON_XPATH,
                               region_field_locator=self._second_step.SECOND_STEP_REGISTRATION_REGION_FIELD_XPATH,
                               city_field_locator=self._second_step.SECOND_STEP_REGISTRATION_CITY_FIELD_XPATH,
                               street_field_locator=self._second_step.SECOND_STEP_REGISTRATION_STREET_FIELD_XPATH,
                               house_field_locator=self._second_step.SECOND_STEP_REGISTRATION_HOUSE_XPATH,
                               index_locator=self._second_step.SECOND_STEP_REGISTRATION_INDEX_XPATH,
                               region=region,
                               city=city)

    @allure.step
    def fact_and_reg_addresses_are_equal(self, equal=True):
        enabled_checkbox = self._second_step.SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_ENABLED_XPATH
        click_target = self._second_step.SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_TARGET_XPATH
        self.switch_checkbox(enabled_checkbox_locator=enabled_checkbox,
                             target=click_target,
                             enabled=True if equal else False)

    @allure.step
    def fill_fact_address_form(self, region=None, city=None):
        if not self.is_element_present(self._second_step.SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_ENABLED_XPATH):
            self.fill_address_form(clear_button_locator=self._second_step.SECOND_STEP_CLEAR_FACT_ADDRESS_BUTTON_XPATH,
                                   region_field_locator=self._second_step.SECOND_STEP_FACT_REGION_FIELD_XPATH,
                                   city_field_locator=self._second_step.SECOND_STEP_FACT_CITY_FIELD_XPATH,
                                   street_field_locator=self._second_step.SECOND_STEP_FACT_STREET_FIELD_XPATH,
                                   house_field_locator=self._second_step.SECOND_STEP_FACT_HOUSE_XPATH,
                                   index_locator=self._second_step.SECOND_STEP_FACT_INDEX_XPATH,
                                   region=region,
                                   city=city)

    @allure.step
    def deactivate_sms_notification_checkbox(self):
        enabled_sms_notification = self._second_step.SECOND_STEP_ENABLED_PHONE_NOTICE_CHECKBOX_XPATH
        click_target = self._second_step.SECOND_STEP_PHONE_NOTICE_CHECKBOX_TARGET_XPATH
        self.switch_checkbox(enabled_checkbox_locator=enabled_sms_notification,
                             target=click_target,
                             enabled=False)

    @allure.step
    def proxy_checkbox(self, state=False, phone_notice=False):
        enabled_proxy_checkbox = self._second_step.SECOND_STEP_IS_PROXY_CHECKBOX_ENABLED_XPATH
        click_target = self._second_step.SECOND_STEP_PROXY_CHECKBOX_TARGET_XPATH
        self.switch_checkbox(enabled_checkbox_locator=enabled_proxy_checkbox,
                             target=click_target,
                             enabled=True if state else False)
        if self.is_element_present(enabled_proxy_checkbox):
            self.update_text(self._second_step.SECOND_STEP_PROXY_NUMBER_CSS, self._claim_model.proxy_number)
            self.update_text(self._second_step.SECOND_STEP_PROXY_DATE_CSS, self._claim_model.proxy_date)
            self.click(self._second_step.SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS)
            self.update_text(self._second_step.SECOND_STEP_PROXY_FIO_CSS, self._claim_model.proxy_fio)
            self.update_text(self._second_step.SECOND_STEP_TRUSTEE_EMAIL_CSS,
                             self._claim_model.trustee_notice_email)
            self.update_text(self._second_step.SECOND_STEP_TRUSTEE_PHONE_CSS,
                             self._claim_model.trustee_notice_phone)
            self.switch_checkbox(enabled_checkbox_locator=self._second_step.SECOND_STEP_ENABLED_TRUSTEE_PHONE_CHECKBOX_XPATH,
                                 target=self._second_step.SECOND_STEP_TRUSTEE_PHONE_CHECKBOX_TARGET_XPATH,
                                 enabled=True if phone_notice else False)

    @allure.step
    def go_to_third_step(self):
        self.click(self._second_step.SECOND_STEP_NEXT_STEP_CSS)
