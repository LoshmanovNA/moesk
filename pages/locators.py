
class BasePageLocators:
    PROFILE_LINK = 'a.profile-link'


class LoginPageLocators:

    LOGIN_INPUT = '#user_email'
    PASS_INPUT = '#user_password'
    SUBMIT_BUTTON = 'button.yellow-btn'
    REGISTER_LINK = 'a[href*="sign_up"]'


class RegisterPageLocators:

    USER_TYPE_LIST = '.ui-autocomplete-input'
    USER_TYPE_FL = '//li[contains(text(), "Физическое")]'
    USER_TYPE_UL = '//li[contains(text(), "Юридическое")]'
    USER_TYPE_IP = '//li[contains(text(), "Индивидуальный")]'
    USER_TYPE_PPD = '//li[contains(text(), "Представитель")]'
    SURNAME = '#user_last_name'
    NAME = '#user_first_name'
    PATRONYMIC = '#user_patronymic_name'
    EMAIL = '#user_email'
    PHONE = '#phone_input'
    CONFIRM1 = '#confirm1'
    CONFIRM2 = '#confirm2'
    NEXT_STEP = '#nextStep'
