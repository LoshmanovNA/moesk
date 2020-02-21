import allure

from .claim_first_step_page import ClaimsFirstStepPage
from ..locators import ClaimsSecondStepLocators
from ..models import ClaimModel
from .base_elements import BaseElements


class ClaimsSecondStepPage(ClaimsFirstStepPage, BaseElements):
    """Методы для работы с полями на втором шаге подачи заявки"""
    _second_step = ClaimsSecondStepLocators()

    @allure.step
    def go_through_second_step_new_connection(self, passport=True, region=None, city=None, fact_address_equal=True,
                                              sms_notification=False, is_proxy=False, model=None):
        """Объединяет в себе действия по заполнению полей с персональнымид данными для разных видов заявителей"""
        claim_model = model() if model else ClaimModel()

        self._fill_date_of_birth(model=claim_model)
        self._choose_document_type(passport=passport)
        self._fill_passport_data_and_snils(model=claim_model)
        self._fill_requisites_form(model=claim_model)
        self._fill_registration_address_form(model=claim_model, region=region, city=city)
        self._fact_and_reg_addresses_are_equal(equal=fact_address_equal)
        self._fill_fact_address_form(model=claim_model, region=region, city=city)
        self._sms_notification_checkbox(state=sms_notification)
        self._proxy_checkbox(model=claim_model, state=is_proxy)
        self._go_to_third_step()

    @allure.step
    def _fill_date_of_birth(self, model):
        """Заполняет поле даты рождения для ФЛ"""
        birth_date_field = self._second_step.SECOND_STEP_BIRTH_DATE_CSS
        if self.is_element_visible(birth_date_field):
            self.update_text(self._second_step.SECOND_STEP_BIRTH_DATE_CSS, model.user_date_birth)
            self.click(self._second_step.SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS)

    @allure.step
    def _choose_document_type(self, passport):
        """Выбирает тип документа пасспорт РФ или иной документ"""
        document_type = self._second_step.SECOND_STEP_DOCUMENT_TYPE_PASSPORT_XPATH
        if self.is_element_present(document_type):
            if passport:
                self.click(self._second_step.SECOND_STEP_DOCUMENT_TYPE_PASSPORT_XPATH, 'By.XPATH')
            else:
                self.click(self._second_step.SECOND_STEP_DOCUMENT_TYPE_OTHER_XPATH)
                self.select_option_by_value(self._second_step.SECOND_STEP_DOC_TYPES_DROPDOWN_CSS,
                                            self._second_step.SECOND_STEP_FOREIGN_PASSPORT_VALUE)
                self.update_text(self._second_step.SECOND_STEP_OTHER_DOC_INFO_CSS, self._claim_model.user_other_document)
        else:
            return

    @allure.step
    def _fill_passport_data_and_snils(self, model):
        """Заполняет поля паспорта и снилса для ФЛ"""
        passport_seria_locator = self._second_step.SECOND_STEP_PASSPORT_SERIA_CSS
        passport_code_locator = self._second_step.SECOND_STEP_PASSPORT_CODE_CSS
        passport_date_locator = self._second_step.SECOND_STEP_PASSPORT_DATE_CSS
        passport_issued = self._second_step.SECOND_STEP_PASSPORT_ISSUED_CSS
        snils_locator = self._second_step.SECOND_STEP_USER_SNILS_CSS
        dropdown_calendar_locator = self._second_step.SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS

        if self.is_element_visible(passport_seria_locator):
            self.update_text(passport_seria_locator,
                             model.user_passport_number)
            self.update_text(passport_code_locator,
                             model.user_passport_code)
            self.update_text(passport_date_locator,
                             model.user_passport_date)
            self.click(dropdown_calendar_locator)
            self.update_text(passport_issued,
                             model.user_passport_issued)
        if self.is_element_visible(snils_locator):
            self.update_text(snils_locator,
                             model.user_fl_snils)

    @allure.step
    def _fill_requisites_form(self, model):
        """Заполняет поля реквизитов для ЮЛ и ИП"""
        egrip_field = self._second_step.SECOND_STEP_EGRIP_CSS
        egrul_field = self._second_step.SECOND_STEP_EGRUL_CSS
        kpp_field = self._second_step.SECOND_STEP_KPP_CSS

        if self.is_element_present(egrip_field):
            self.update_text(egrip_field, model.user_ip_egrip)
        if self.is_element_present(egrul_field):
            self.update_text(egrul_field, model.user_ul_egrul_num)
        if self.is_element_present(kpp_field):
            self.update_text(kpp_field, model.user_ul_kpp)
        if self.is_element_present(self._second_step.SECOND_STEP_INN_CSS):
            self.update_text(self._second_step.SECOND_STEP_REESTR_DATE_CSS, model.user_reestr_date)
            self.update_text(self._second_step.SECOND_STEP_INN_CSS, model.user_inn)

    @allure.step
    def _fill_registration_address_form(self, model, region=None, city=None):
        """Заполнение формы с адресом регистрации"""
        first_value_from_list = self._second_step_locators.SECOND_STEP_FIRST_VALUE_FROM_LIST_CSS

        self.click(self._second_step.SECOND_STEP_CLEAR_REG_ADDRESS_BUTTON_XPATH, 'By.XPATH')
        self.update_text(self._second_step.SECOND_STEP_REGISTRATION_REGION_FIELD_XPATH,
                         region if region else model.region)
        self.click(first_value_from_list)
        self.update_text(self._second_step.SECOND_STEP_REGISTRATION_CITY_FIELD_XPATH,
                         city if city else model.city)
        self.click(first_value_from_list)
        self.update_text(self._second_step.SECOND_STEP_REGISTRATION_STREET_FIELD_XPATH,
                         model.street)
        self.click(first_value_from_list)
        self.update_text(self._second_step.SECOND_STEP_REGISTRATION_INDEX_XPATH,
                         model.post_index)

    @allure.step
    def _fact_and_reg_addresses_are_equal(self, equal=True):
        """
        Действия с чек-боксом 'Совпадает с адресом по месту регистрации'
        Если equal=true, то чек-бокс включится, иначе выключится
         """
        enabled_checkbox = self._second_step.SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_ENABLED_XPATH
        click_target = self._second_step.SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_TARGET_CSS
        self.switch_checkbox(enabled_checkbox_locator=enabled_checkbox,
                             target=click_target,
                             enabled=True if equal else False)

    @allure.step
    def _fill_fact_address_form(self, model, region=None, city=None):
        """Заполнение формы с адресом для направления корреспонденции"""
        first_value_from_list = self._second_step_locators.SECOND_STEP_FIRST_VALUE_FROM_LIST_CSS

        self.click(self._second_step.SECOND_STEP_CLEAR_FACT_ADDRESS_BUTTON_XPATH, 'By.XPATH')
        self.update_text(self._second_step.SECOND_STEP_FACT_REGION_FIELD_XPATH,
                         region if region else model.region)
        self.click(first_value_from_list)
        self.update_text(self._second_step.SECOND_STEP_FACT_CITY_FIELD_XPATH,
                         city if city else model.city)
        self.click(first_value_from_list)
        self.update_text(self._second_step.SECOND_STEP_FACT_STREET_FIELD_XPATH,
                         model.street)
        self.click(first_value_from_list)
        self.update_text(self._second_step.SECOND_STEP_FACT_INDEX_XPATH,
                         model.post_index)

    @allure.step
    def _sms_notification_checkbox(self, state=False):
        """Отключение получения уведомлений на телефон"""
        enabled_sms_notification = self._second_step.SECOND_STEP_ENABLED_PHONE_NOTICE_CHECKBOX_XPATH
        click_target = self._second_step.SECOND_STEP_PHONE_NOTICE_CHECKBOX_TARGET_CSS
        self.switch_checkbox(enabled_checkbox_locator=enabled_sms_notification,
                             target=click_target,
                             enabled=False if not state else True)

    @allure.step
    def _proxy_checkbox(self, model, state=False, phone_notice=False):
        """
        Действия с чек-боксом подачи заявки по доверенности.
        Если state=false - чек-бокс выключен, иначе включен
        При включенном заполняется форма представителя по доверенности
        При phone_notice=false отключается чекс бокс уведомление на телефон
        """
        enabled_proxy_checkbox = self._second_step.SECOND_STEP_IS_PROXY_CHECKBOX_ENABLED_XPATH
        click_target = self._second_step.SECOND_STEP_PROXY_CHECKBOX_TARGET_CSS
        self.switch_checkbox(enabled_checkbox_locator=enabled_proxy_checkbox,
                             target=click_target,
                             enabled=True if state else False)
        if self.is_element_present(enabled_proxy_checkbox):
            self.update_text(self._second_step.SECOND_STEP_PROXY_NUMBER_CSS,
                             model.proxy_number)
            self.update_text(self._second_step.SECOND_STEP_PROXY_DATE_CSS,
                             model.proxy_date)
            self.click(self._second_step.SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS)
            self.update_text(self._second_step.SECOND_STEP_PROXY_FIO_CSS,
                             model.proxy_fio)
            self.update_text(self._second_step.SECOND_STEP_TRUSTEE_EMAIL_CSS,
                             model.trustee_notice_email)
            self.update_text(self._second_step.SECOND_STEP_TRUSTEE_PHONE_CSS,
                             model.trustee_notice_phone)
            self.switch_checkbox(enabled_checkbox_locator=self._second_step.SECOND_STEP_ENABLED_TRUSTEE_PHONE_CHECKBOX_XPATH,
                                 target=self._second_step.SECOND_STEP_TRUSTEE_PHONE_CHECKBOX_TARGET_CSS,
                                 enabled=True if phone_notice else False)

    @allure.step
    def _go_to_third_step(self):
        """Переход на 3 шаг подачи заявки"""
        self.click(self._second_step.SECOND_STEP_NEXT_STEP_CSS)
