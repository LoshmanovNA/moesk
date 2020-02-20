import allure

from .login_page import LoginPage
from ..locators import MainPageLocators


class MainPage(LoginPage):
    _main_page = MainPageLocators()

    @allure.step
    def start_new_tp_claim(self):
        self.click(self._main_page.MAIN_PAGE_BUTTON_CLAIM_TP_XPATH, 'By.XPATH')

    @allure.step
    def start_consolidation_claim(self):
        self.click(self._main_page.MAIN_PAGE_BUTTON_CLAIM_CONSOLIDATION_XPATH, 'By.XPATH')

    @allure.step
    def start_du_claim(self):
        self.click(self._main_page.MAIN_PAGE_BUTTON_CLAIM_DU_XPATH, 'By.XPATH')

    @allure.step
    def start_recovery_claim(self):
        self.click(self._main_page.MAIN_PAGE_BUTTON_CLAIM_RECOVERY_XPATH, 'By.XPATH')

    @allure.step
    def start_redistribution_claim(self):
        self.click(self._main_page.MAIN_PAGE_BUTTON_CLAIM_REDISTRIBUTION_XPATH, 'By.XPATH')
