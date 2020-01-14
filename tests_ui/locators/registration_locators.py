
class RegistrationPageLocators:
    """Страница регистрации"""
    REGISTRATION_USER_TYPE_LIST_CSS = '.ui-autocomplete-input'
    REGISTRATION_USER_TYPE_FL_XPATH = '//li[contains(text(), "Физическое")]'
    REGISTRATION_USER_TYPE_UL_XPATH = '//li[contains(text(), "Юридическое")]'
    REGISTRATION_USER_TYPE_IP_XPATH = '//li[contains(text(), "Индивидуальный")]'
    REGISTRATION_USER_TYPE_PPD_XPATH = '//li[contains(text(), "Представитель")]'
    REGISTRATION_SURNAME_CSS = '#user_last_name'
    REGISTRATION_NAME_CSS = '#user_first_name'
    REGISTRATION_PATRONYMIC_CSS = '#user_patronymic_name'
    REGISTRATION_EMAIL_CSS = '#user_email'
    REGISTRATION_PHONE_CSS = '#phone_input'
    REGISTRATION_CONFIRM1_CSS = '#confirm1'
    REGISTRATION_CONFIRM2_CSS = '#confirm2'
    REGISTRATION_NEXT_STEP_CSS = '#nextStep'
    REGISTRATION_CLOSE_WINDOW_XPATH = '//a[contains(text(), "Закрыть")]'
