from .base_page import BasePage
from ..locators import WarningPageLocators


class WarningPage(BasePage):
    _warning_page = WarningPageLocators

    def click_accept_warning_button(self):
        self.click(self._warning_page.WARNING_WARNED_BUTTON_CSS)

    def click_go_portal_button(self):
        self.click(self._warning_page.WARNING_GO_PORTAL_BUTTON_CSS)
