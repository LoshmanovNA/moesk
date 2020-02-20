import allure

from .main_page import MainPage
from ..locators import WarningPageLocators


class WarningPage(MainPage):
    _warning_page = WarningPageLocators

    @allure.step
    def click_accept_warning_button(self):
        self.click(self._warning_page.WARNING_WARNED_BUTTON_CSS)

    @allure.step
    def click_go_portal_button(self):
        self.click(self._warning_page.WARNING_GO_PORTAL_BUTTON_CSS)
