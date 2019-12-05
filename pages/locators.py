from seleniumbase import BaseCase as BC


class LoginPageLocators(BC):
    LOGIN_INPUT = BC.find_element('#user_email', by=By.CSS_SELECTOR)
    PASS_INPUT = BC.find_element('#user_password', by=By.CSS_SELECTOR)
    SUBMIT_BUTTON = BC.find_element('button.yellow-btn', by=By.CSS_SELECTOR)
    REMIND_PASS_BUTTON = BC.find_element('a[href*="password"]', by=By.CSS_SELECTOR)


class RemindPasswordLocators(BC):
    USER_EMAIL = BC.find_element('#user_email', by=By.CSS_SELECTOR)
    SEND_BUTTON = BC.find_element('#nextStep', by=By.CSS_SELECTOR)
