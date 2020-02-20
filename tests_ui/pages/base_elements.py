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

    @allure.step
    def fill_address_form(self, clear_button_locator, region_field_locator, city_field_locator, street_field_locator,
                          house_field_locator, index_locator, region=None, city=None):
        """Заполнение формы с адресом"""
        first_value_from_list = self._second_step_locators.SECOND_STEP_FIRST_VALUE_FROM_LIST_CSS
        self.click(clear_button_locator, 'By.XPATH')
        self.update_text(region_field_locator, region if region else ' ')
        self.click(first_value_from_list)
        self.update_text(city_field_locator, city if city else ' ')
        self.click(first_value_from_list)
        self.update_text(street_field_locator, ' ')
        self.click(first_value_from_list)
        self.update_text(house_field_locator, self._claim_model.user_address_house)
        self.update_text(index_locator, self._claim_model.user_address_index)

    @allure.step
    def scroll_into_view(self, locator):
        elem = self.find_element(locator)
        self.driver.execute_script("return arguments[0].scrollTo(0, -250)", elem)

