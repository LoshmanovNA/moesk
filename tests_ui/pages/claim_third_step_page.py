import allure

from .claim_second_step_page import ClaimsSecondStepPage
from ..locators import ClaimsThirdStepLocators
from ..models import ClaimModel
from .base_elements import BaseElements


class ClaimsThirdStepPage(ClaimsSecondStepPage, BaseElements):
    _third_step = ClaimsThirdStepLocators

    @allure.step
    def go_through_third_step_new_connection(self, region=None, city=None, power=None, voltage=None,
                                             reliability=None, number_of_points=None, model=None):
        """Заполнение 3 шага заявки"""
        claim_model = model() if model else ClaimModel()

        self._select_epu_type()
        self._input_cadastral_number(model=claim_model)
        self._fill_epu_address_form(region=region, city=city, model=claim_model)
        self._enter_max_power_value(power=power, model=claim_model)
        self._select_voltage_level(voltage_level=voltage, model=claim_model)
        self._select_reliability_level(reliability_level=reliability, model=claim_model)
        self._enter_connection_points(number_of_points=number_of_points, model=claim_model)
        self._object_readiness_status()

    @allure.step
    def _select_epu_type(self, model):
        if model.epu_type:
            self.click_chain([self._third_step.THIRD_STEP_EPU_TYPE_FIELD_CSS,
                              self._third_step.THIRD_STEP_FIRST_VALUE_FROM_LIST_CSS])

    @allure.step
    def _input_cadastral_number(self, model):
        self.update_text(self._third_step.THIRD_STEP_INPUT_CADASTRAL_CSS, model.cadastral_number)

    @allure.step
    def _fill_epu_address_form(self, model, region=None, city=None):
        """Заполнение формы с адресом"""
        first_value_from_list = self._second_step_locators.SECOND_STEP_FIRST_VALUE_FROM_LIST_CSS
        self.click(self._third_step.THIRD_STEP_EPU_CLEAR_BUTTON, 'By.XPATH')
        self.update_text(self._third_step.THIRD_STEP_EPU_REGION_FIELD_CSS, region if region else model.region)
        self.click(first_value_from_list)
        self.update_text(self._third_step.THIRD_STEP_EPU_CITY_FIELD_CSS, city if city else model.city)
        self.click(first_value_from_list)
        self.update_text(self._third_step.THIRD_STEP_EPU_STREET_CSS, model.street)
        self.click(first_value_from_list)
        self.update_text(self._third_step.THIRD_STEP_EPU_INDEX_CSS, model.post_index)

    @allure.step
    def _select_tp_period_for_temp_connection(self):
        pass

    @allure.step
    def _enter_max_power_value(self, power, model):
        if power:
            self.update_text(self._third_step.THIRD_STEP_MAX_POWER_CSS, power)
        else:
            self.update_text(self._third_step.THIRD_STEP_MAX_POWER_CSS,
                             model.max_power)

    @allure.step
    def _enter_pre_power_value(self, pre_power, model):
        if pre_power:
            self.update_text(self._third_step.THIRD_STEP_PRE_POWER_CSS, pre_power)
        else:
            self.update_text(self._third_step.THIRD_STEP_PRE_POWER_CSS,
                             model.pre_power)

    @allure.step
    def _select_voltage_level(self, voltage_level, model):
        level_locators = {"220": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_220V_XPATH,
                          "380": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_380V_XPATH,
                          "6": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_6KV_XPATH,
                          "10": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_10KV_XPATH,
                          "20": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_20KV_XPATH,
                          "35": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_35KV_XPATH,
                          "110": self._third_step.THIRD_STEP_VOLTAGE_LEVEL_110KV_XPATH}
        voltage_level = str().join([char for char in str(voltage_level) if char.isdigit()])
        if voltage_level:
            self.click_chain([self._third_step.THIRD_STEP_VOLTAGE_LIST_CSS,
                              level_locators[voltage_level]])
        else:
            self.click_chain([self._third_step.THIRD_STEP_VOLTAGE_LIST_CSS,
                              level_locators[model.voltage_level]])

    @allure.step
    def _select_reliability_level(self, reliability_level, model):
        required_level_value = str(reliability_level)

        dropdown_list_locator = self._third_step.THIRD_STEP_RELIABILITY_LIST_CSS
        # Локаторы для указания категории надежности при мощности до 150 кВт
        reliability_level_dropdown_value_locators = {"1": self._third_step.THIRD_STEP_INPUT_RELIABILITY_LEVEL_ONE_CSS,
                                                     "2": self._third_step.THIRD_STEP_INPUT_RELIABILITY_LEVEL_TWO_CSS,
                                                     "3": self._third_step.THIRD_STEP_INPUT_RELIABILITY_LEVEL_THREE_CSS}
        # Локаторы для указания категории надежности при мощности более 150 кВт
        reliability_level_input_value_locators = {"1": self._third_step.THIRD_STEP_INPUT_RELIABILITY_LEVEL_ONE_CSS,
                                                  "2": self._third_step.THIRD_STEP_INPUT_RELIABILITY_LEVEL_TWO_CSS,
                                                  "3": self._third_step.THIRD_STEP_INPUT_RELIABILITY_LEVEL_THREE_CSS}
        if reliability_level:
            if self.is_element_visible(dropdown_list_locator):
                self.click_chain([dropdown_list_locator,
                                  reliability_level_dropdown_value_locators[required_level_value]])
            else:
                self.click(reliability_level_input_value_locators[required_level_value])
        else:
            if self.is_element_visible(dropdown_list_locator):
                self.click_chain([dropdown_list_locator,
                                  reliability_level_dropdown_value_locators[model.reliability_level]])
            else:
                self.click(reliability_level_input_value_locators[model.reliability_level])

    @allure.step
    def _enter_connection_points(self, number_of_points, model):
        if number_of_points:
            self.update_text(self._third_step.THIRD_STEP_EPU_POINTS_CSS, number_of_points)
        else:
            self.update_text(self._third_step.THIRD_STEP_EPU_POINTS_CSS, model.connection_points)

    @allure.step
    def _object_readiness_status(self, model):
        if model:
            self.click(self._third_step.THIRD_STEP_EPU_OBJECT_READY_CSS)

