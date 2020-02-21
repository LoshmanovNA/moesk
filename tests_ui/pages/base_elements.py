import allure

from ..pages import BasePage
from ..models import ClaimModel
from ..locators import ClaimsSecondStepLocators


class BaseElements(BasePage):
    """Общие действия с элементами, повторяющиеся на разных страницах"""
    _second_step_locators = ClaimsSecondStepLocators()
    _claim_model = ClaimModel()

    @allure.step
    def switch_checkbox(self, enabled_checkbox_locator, target, enabled=True):
        """Включение или отключение чек-бокса"""
        if enabled:
            if self.is_element_present(enabled_checkbox_locator, 'By.XPATH'):
                return True
            else:
                self.click(target)
        else:
            if self.is_element_present(enabled_checkbox_locator):
                self.click(target)
            else:
                return True