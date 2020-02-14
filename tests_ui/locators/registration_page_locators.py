
class RegistrationPageLocators:
    """Страница регистрации"""
#  Поля формы регистрации
    # Тип заявителя
    REGISTRATION_USER_TYPE_LIST_CSS = '.ui-autocomplete-input'
    REGISTRATION_USER_TYPE_FL_XPATH = '//li[contains(text(), "Физическое")]'
    REGISTRATION_USER_TYPE_UL_XPATH = '//li[contains(text(), "Юридическое")]'
    REGISTRATION_USER_TYPE_IP_XPATH = '//li[contains(text(), "Индивидуальный")]'
    REGISTRATION_USER_TYPE_PPD_XPATH = '//li[contains(text(), "Представитель")]'

    # ФИО заявителя типа Физическое лицо
    REGISTRATION_FIRST_NAME_CSS = '#user_first_name'
    REGISTRATION_LAST_NAME_CSS = '#user_last_name'
    REGISTRATION_PATRONYMIC_CSS = '#user_patronymic_name'

    # Полное и сокращенное наименование юридического лица
    REGISTRATION_UL_FULL_NAME_CSS = '#user_company_attributes_name'
    REGISTRATION_UL_SHORT_NAME_CSS = '#user_company_attributes_short_name'

    # ФИО Индивидуального предпринимателя и чек-бокс "Есть контактное лицо"
    REGISTRATION_IP_FIRST_NAME_CSS = '.personData #user_first_name'
    REGISTRATION_IP_LAST_NAME_CSS = '.personData #user_last_name'
    REGISTRATION_IP_PATRONYMIC_NAME_CSS = '.personData #user_patronymic_name'
    REGISTRATION_IP_HAS_CONTACT_PERSON_CSS = '#ipHasContactPerson'

    # Контактное лицо у ЮЛ и ИП
    REGISTRATION_CONTACT_FIRST_NAME_CSS = '#companyContact #user_first_name'
    REGISTRATION_CONTACT_LAST_NAME_CSS = '#companyContact #user_last_name'
    REGISTRATION_CONTACT_PATRONYMIC_NAME_CSS = '#companyContact #user_patronymic_name'

    # Телефон и почта регистрируемого пользователя
    REGISTRATION_EMAIL_CSS = '#user_email'
    REGISTRATION_PHONE_CSS = '#phone_input'

    #  Чек-боксы согласия на странице регистрации
    REGISTRATION_CONFIRM1_CSS = '#confirm1'
    REGISTRATION_CONFIRM2_CSS = '#confirm2'
    REGISTRATION_CONFIRM3_CSS = '#confirm3'

#  Кнопки "Продолжить регистрацию" и "Отмена"
    REGISTRATION_NEXT_STEP_CSS = '#nextStep'
    REGISTRATION_CLOSE_WINDOW_XPATH = '//a[contains(text(), "Закрыть")]'

#  Ошибки валидации полей формы регистрации
    REGISTRATION_VALIDATION_ERROR_MESSAGES_XPATH = {
        'first_name': '//input[@id="user_first_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'last_name': '//input[@id="user_last_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'patronymic_name': '//input[@id="user_patronymic_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'phone': '//input[@id="phone_input"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'email': '//input[@id="user_email"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'company_full_name': '//input[@id="user_company_attributes_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'company_short_name': '//input[@id="user_company_attributes_short_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'confirm_1': '//input[@id="confirm1"]/ancestor::label[contains (@class, "invalid")]/following-sibling::span',
        'confirm_2': '//input[@id="confirm2"]/ancestor::label[contains (@class, "invalid")]/following-sibling::span'
    }
