from ...pages import BasePage
from ...locators.claims import NewTPLocators


class FirstStepTP(BasePage):
    _first_step = NewTPLocators().FirstStep()

    def select_claim_type_new_tp(self):
        self.click(self._first_step.NEW_TP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.NEW_TP_NEW_CONNECTION_CSS)

    def select_claim_type_temporary_connection(self):
        self.click(self._first_step.NEW_TP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.NEW_TP_TEMPORARY_CONNECTION_CSS)

    def select_claim_type_power_increase(self):
        self.click(self._first_step.NEW_TP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.NEW_TP_POWER_INCREASE_CSS)

    def select_claim_type_power_reassignment(self):
        self.click(self._first_step.NEW_TP_CLAIM_TYPE_BUTTON_CSS)
        self.click(self._first_step.NEW_TP_REASSIGNMENT_CSS)
        # Выклчюаем чек-бокс переуступки по собственному договору (на случай, если существующих заявок нет)
        self.js_click(self._first_step.NEW_TP_REASSIGNMENT_CHECKBOX_CSS)
        # Вводим вручную номер заявки
        self.update_text(self._first_step.NEW_TP_REASSIGNMENT_CLAIM_NUMBER_CSS, 'И1600123456102')

    def click_next_step(self):
        self.click(self._first_step.NEW_TP_NEXT_BUTTON_CSS)

    def click_cancel_claim(self):
        self.click(self._first_step.NEW_TP_CANCEL_CLAIM_CSS)

