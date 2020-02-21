import allure

from .warning_page import WarningPage
from ..locators import ClaimsFirstStepLocators
from ..models import ClaimModel


class ClaimsFirstStepPage(WarningPage):
    _first_step = ClaimsFirstStepLocators
    _claim_model = ClaimModel()

    def go_through_first_step_new_connection(self):
        self._select_claim_type_new_tp()
        self._go_to_second_step()

    @allure.step
    def _select_claim_type_new_tp(self):
        select_claim_type = self._first_step.FIRST_STEP_CLAIM_TYPE_BUTTON_CSS
        if self.is_element_visible(select_claim_type):
            self.click(self._first_step.FIRST_STEP_CLAIM_TYPE_BUTTON_CSS)
            self.click(self._first_step.FIRST_STEP_NEW_CONNECTION_XPATH, 'By.XPATH')

    @allure.step
    def _select_claim_type_temporary_connection(self):
        self.click(self._first_step.FIRST_STEP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.FIRST_STEP_TEMPORARY_CONNECTION_XPATH, 'By.XPATH')

    @allure.step
    def _select_claim_type_power_increase(self):
        self.click(self._first_step.FIRST_STEP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.FIRST_STEP_POWER_INCREASE_XPATH, 'By.XPATH')

    @allure.step
    def _select_claim_type_power_reassignment(self):
        self.click(self._first_step.FIRST_STEP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.FIRST_STEP_REASSIGNMENT_XPATH, 'By.XPATH')
        # Выклчюаем чек-бокс переуступки по собственному договору (на случай, если существующих заявок нет)
        self.js_click(self._first_step.FIRST_STEP_REASSIGNMENT_CHECKBOX_CSS)
        # Вводим вручную номер заявки
        self.update_text(self._first_step.FIRST_STEP_REASSIGNMENT_CLAIM_NUMBER_CSS,
                         self._claim_model.reassignment_claim_number)

    @allure.step
    def _go_to_second_step(self):
        self.click(self._first_step.FIRST_STEP_NEXT_BUTTON_CSS)

    @allure.step
    def _click_cancel_claim(self):
        self.click(self._first_step.FIRST_STEP_CANCEL_CLAIM_CSS)

