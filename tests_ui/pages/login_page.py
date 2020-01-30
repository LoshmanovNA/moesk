import allure

from .base_page import BasePage
from ..locators import LoginPageLocators, CommonLocators


class LoginPage(BasePage):
    """Действия на странице логина"""
    _login_page_locators = LoginPageLocators()
    _common_locators = CommonLocators()

    @allure.step
    def login_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.update_text(self._login_page_locators.LOGIN_INPUT_EMAIL_CSS, login)
        self.update_text(self._login_page_locators.LOGIN_INPUT_PASS_CSS, password)
        self.click(self._login_page_locators.LOGIN_SUBMIT_BUTTON_CSS)

    @allure.step
    def should_be_main_page_lk(self):
        """Проверка нахождения на главной странице после авторизации"""
        if 'assets/sprite.png' in self.get_current_url():
            self.click(self._common_locators.COMMON_MAIN_LOGO_CSS)
            self.assert_element(self._common_locators.COMMON_PROFILE_LINK_CSS), "Main page hadn't  opened"
        else:
            self.assert_element(self._common_locators.COMMON_PROFILE_LINK_CSS), "Main page hadn't  opened"
