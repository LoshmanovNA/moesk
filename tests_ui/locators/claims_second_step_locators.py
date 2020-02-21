
class ClaimsSecondStepLocators:
    """Второй шаг подачи заявки"""
    # Выбор даты рождения (выпадающий календарь)
    SECOND_STEP_BIRTH_DATE_CSS = '#claim_user_birthday_at'
    SECOND_STEP_CALENDAR_ACTIVE_DATE_CSS = 'a.ui-state-active'
    # Выбор документа
    SECOND_STEP_DOCUMENT_TYPE_PASSPORT_XPATH = '//input[@id="passport"]/parent::label'
    SECOND_STEP_DOCUMENT_TYPE_OTHER_XPATH = '//input[@id="other_doc"]/parent::label'
    # Если выбран паспорт
    # Паспортные данные
    SECOND_STEP_PASSPORT_SERIA_CSS = '#claim_user_passport_series_number'
    SECOND_STEP_PASSPORT_CODE_CSS = '#claim_user_passport_code'
    SECOND_STEP_PASSPORT_DATE_CSS = '#claim_user_passport_date'
    SECOND_STEP_PASSPORT_ISSUED_CSS = '#claim_user_passport_issued'
    # СНИЛС Заявителя
    SECOND_STEP_USER_SNILS_CSS = '#claim_user_snils'
    # Если выбран радиобатон "Иной документ":
    # Выпадающий список "Тип документа"
    SECOND_STEP_DOC_TYPES_DROPDOWN_CSS = '#claim_user_doc_type_id'
    SECOND_STEP_PASSPORT_MORIAKA_VALUE = '1'
    SECOND_STEP_VOIENNIY_BILET_VALUE = '2'
    SECOND_STEP_FOREIGN_PASSPORT_VALUE = '4'
    SECOND_STEP_DRIVER_LICENSE_VALUE = '5'
    # Реквизиты иного документа (текстовое поле)
    SECOND_STEP_OTHER_DOC_INFO_CSS = '#claim_user_other_document'

    # Реквизиты заявителей вида Юр. лицо и ИП
    SECOND_STEP_KPP_CSS = '#claim_company_kpp'
    SECOND_STEP_EGRUL_CSS = '#claim_ur_egrul_number'
    SECOND_STEP_EGRIP_CSS = '#claim_ip_egrip_number'
    SECOND_STEP_REESTR_DATE_CSS = '#claim_reestr_date'
    SECOND_STEP_INN_CSS = '#claim_company_inn'
    SECOND_STEP_RS_CSS = '#claim_company_rs'
    SECOND_STEP_BIK_CSS = '#claim_company_bik'
    SECOND_STEP_BANK_CSS = '#claim_company_bank'

    # Блок "Адрес по месту регистрации"
    # Очистить адрес регистрации
    SECOND_STEP_CLEAR_REG_ADDRESS_BUTTON_XPATH = '//input[contains(@id, "reg_clear_address")]'

    # Выбор первого значения из активного выпадающего списка
    SECOND_STEP_FIRST_VALUE_FROM_LIST_CSS = 'ul[style*="display: block"] > li'

    # Поля адреса по месту регистрации
    # Поле ввода полного адреса
    SECOND_STEP_REGISTRATION_FULL_ADDRESS_XPATH = '//span/input[contains(@id, "full_address")]'
    # Поле ввода значения региона
    SECOND_STEP_REGISTRATION_REGION_FIELD_XPATH = '//span/input[contains(@id, "reg_region")]'
    # Поле ввода значения района
    SECOND_STEP_REGISTRATION_AREA_FIELD_XPATH = '//span/input[contains(@id, "reg_area")]'
    # Поле ввода значения города
    SECOND_STEP_REGISTRATION_CITY_FIELD_XPATH = '//span/input[contains(@id, "reg_city")]'
    # Поле ввода значения населенного пункта
    SECOND_STEP_REGISTRATION_SETTLEMENT_FIELD_XPATH = '//span/input[contains(@id, "reg_settlement")]'
    # Поле ввода значения улицы
    SECOND_STEP_REGISTRATION_STREET_FIELD_XPATH = '//span/input[contains(@id, "reg_street")]'
    # Поле ввода номера дома
    SECOND_STEP_REGISTRATION_HOUSE_XPATH = '//input[contains(@id, "reg_house")]'
    # Поле ввода номера корпуса
    SECOND_STEP_REGISTRATION_CORPS_XPATH = '//input[contains(@id, "reg_corps")]'
    # Поле ввода номера строения
    SECOND_STEP_REGISTRATION_BUILDING_XPATH = '//input[contains(@id, "reg_building")]'
    # Поле ввода номера квартиры
    SECOND_STEP_REGISTRATION_FLAT_XPATH = '//input[contains(@id, "reg_flat")]'
    # Поле ввода номера владения
    SECOND_STEP_REGISTRATION_DOMAIN_XPATH = '//input[contains(@id, "reg_domain")]'
    # Поле ввода номера индекса
    SECOND_STEP_REGISTRATION_INDEX_XPATH = '//input[contains(@id, "reg_postcode")]'

    # Блок адреса для направления корреспонденции (фактического адреса)
    # Очистить адрес для корреспонденции
    SECOND_STEP_CLEAR_FACT_ADDRESS_BUTTON_XPATH = '//input[contains(@id, "fact_clear_address")]'

    # Включенный чек-бокс "Совпадает с адресом по месту регистрации" и локатор для клика
    SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_ENABLED_XPATH = '//input[contains(@id, "is_address_equal")]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_FACT_ADDRESS_IS_MATCH_CHECKBOX_TARGET_CSS = 'label[for="is_address_equal"]'

    # Поля адреса для направления корреспонденции (фактического адреса)
    # Поле ввода полного адреса
    SECOND_STEP_FACT_FULL_ADDRESS_XPATH = '//span/input[contains(@id, "full_address")]'
    # Поле ввода значения региона
    SECOND_STEP_FACT_REGION_FIELD_XPATH = '//span/input[contains(@id, "fact_region")]'
    # Поле ввода значения района
    SECOND_STEP_FACT_AREA_FIELD_XPATH = '//span/input[contains(@id, "fact_area")]'
    # Поле ввода значения города
    SECOND_STEP_FACT_CITY_FIELD_XPATH = '//span/input[contains(@id, "fact_city")]'
    # Поле ввода значения населенного пункта
    SECOND_STEP_FACT_SETTLEMENT_FIELD_XPATH = '//span/input[contains(@id, "fact_settlement")]'
    # Поле ввода значения улицы
    SECOND_STEP_FACT_STREET_FIELD_XPATH = '//span/input[contains(@id, "fact_street")]'
    # Поле ввода номера дома
    SECOND_STEP_FACT_HOUSE_XPATH = '//input[contains(@id, "fact_house")]'
    # Поле ввода номера корпуса
    SECOND_STEP_FACT_CORPS_XPATH = '//input[contains(@id, "fact_corps")]'
    # Поле ввода номера строения
    SECOND_STEP_FACT_BUILDING_XPATH = '//input[contains(@id, "fact_building")]'
    # Поле ввода номера квартиры
    SECOND_STEP_FACT_FLAT_XPATH = '//input[contains(@id, "fact_flat")]'
    # Поле ввода номера владения
    SECOND_STEP_FACT_DOMAIN_XPATH = '//input[contains(@id, "fact_domain")]'
    # Поле ввода номера индекса
    SECOND_STEP_FACT_INDEX_XPATH = '//input[contains(@id, "fact_postcode")]'

    # Блок "Получение кассового чека при онлайн-оплате счета по заявке". Включенный чек бокс и локатор для клика
    SECOND_STEP_ENABLED_GET_RECEIPT_BY_EMAIL_CHECKBOX_XPATH = '//input[@id="is_email_receipt"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_GET_RECEIPT_BY_EMAIL_CHECKBOX_TARGET_CSS = 'label[for="is_email_receipt"]'

    SECOND_STEP_ENABLED_GET_RECEIPT_BY_PHONE_CHECKBOX_XPATH = '//input[@id="is_phone_receipt"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_GET_RECEIPT_BY_PHONE_CHECKBOX_TARGET_CSS = 'label[for="is_phone_receipt"]'

    SECOND_STEP_ENABLED_REFUSED_OF_RECEIPT_CHECKBOX_XPATH = '//input[@id="claim_receipt_refused"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_REFUSED_OF_RECEIPT_CHECKBOX_TARGET_CSS = 'label[for="claim_receipt_refused"]'

    # Блок "Получение уведомлений о рассмотрении заявки". Включенный чек бокс и локатор для клика
    SECOND_STEP_ENABLED_EMAIL_NOTICE_CHECKBOX_XPATH = '//input[@id="user_email_notice"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_EMAIL_NOTICE_CHECKBOX_TARGET_CSS = 'label[for="user_email_notice"]'

    SECOND_STEP_ENABLED_PHONE_NOTICE_CHECKBOX_XPATH = '//input[@id="user_phone_notice"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_PHONE_NOTICE_CHECKBOX_TARGET_CSS = 'label[for="user_phone_notice"]'

    SECOND_STEP_ENABLED_AUTOINFORM_NOTICE_CHECKBOX_XPATH = '//input[@id="user_call_notice"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_AUTOINFORM_NOTICE_CHECKBOX_TARGET_CSS = 'label[for="user_call_notice"]'

    # Блок оформления по доверенности
    SECOND_STEP_IS_PROXY_CHECKBOX_ENABLED_XPATH = '//input[@id="claim_is_proxy"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_PROXY_CHECKBOX_TARGET_CSS = 'label[for="claim_is_proxy"]'
    SECOND_STEP_PROXY_NUMBER_CSS = '#claim_user_proxy_number'
    SECOND_STEP_PROXY_DATE_CSS = '#claim_user_proxy_date'
    SECOND_STEP_PROXY_FIO_CSS = '#claim_user_proxy_fio'
    # Способы получения уведомлений в блоке "По доверенности" (включены по умолчанию). Вкл. чек боксы и локаторы для клика
    SECOND_STEP_ENABLED_TRUSTEE_EMAIL_CHECKBOX_XPATH = '//input[@id="trustee_email_notice"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_TRUSTEE_EMAIL_CHECKBOX_TARGET_CSS = 'label[for="trustee_email_notice"]'

    SECOND_STEP_ENABLED_TRUSTEE_PHONE_CHECKBOX_XPATH = '//input[@id="trustee_phone_notice"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_TRUSTEE_PHONE_CHECKBOX_TARGET_CSS = 'label[for="trustee_phone_notice"]'

    SECOND_STEP_ENABLED_TRUSTEE_CALL_CHECKBOX_XPATH = '//input[@id="trustee_call_notice"]/parent::label[contains(@class, "checked")]'
    SECOND_STEP_TRUSTEE_CALL_CHECKBOX_TARGET_CSS = 'label[for="trustee_call_notice"]'
    # E-mail и телефон для получения уведомлений при активном блоке "По доверенности"
    SECOND_STEP_TRUSTEE_EMAIL_CSS = 'input#claim_trustee_email'
    SECOND_STEP_TRUSTEE_PHONE_CSS = 'input#claim_trustee_phone_input'

    # Блок кнопок навигации и сохранения заявки
    SECOND_STEP_BACK_BUTTON_CSS = '.card-controls a[href*="claims"]'
    SECOND_STEP_NEXT_STEP_CSS = '#nextStep'
    SECOND_STEP_SAVE_DRAFT_CSS = 'a.link[href="/"]'
