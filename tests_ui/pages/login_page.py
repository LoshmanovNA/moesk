import allure

from .base_page import BasePage
from ..locators import LoginPageLocators


class LoginPage(BasePage):
    """Действия на странице логина"""
    login_page_locators = LoginPageLocators()

    @allure.step
    def login_user(self, login, password):
        """Авторизация под существующим пользователем"""
        self.update_text(self.login_page_locators.LOGIN_INPUT_EMAIL_CSS, login)
        self.update_text(self.login_page_locators.LOGIN_INPUT_PASS_CSS, password)
        self.click(self.login_page_locators.LOGIN_SUBMIT_BUTTON_CSS)

    @allure.step
    def should_be_main_page_lk(self):
        """Проверка успешной авторизации"""
        if 'assets/sprite.png' in self.get_current_url():
            self.click(self.common_locators.COMMON_MAIN_LOGO_CSS)
            self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)
        else:
            self.assert_element(self.common_locators.COMMON_PROFILE_LINK_CSS)

    @allure.step
    def should_not_login(self):
        """При незаполненным логине или пароле авторизация не должна выполниться"""
        self.assert_element(self.login_page_locators.LOGIN_WRONG_EMAIL_OR_PASS_CSS)
