
class ClaimsSecondStepLocators:
    """Второй шаг подачи заявки"""
    # Выбор даты рождения (выпадающий календарь)
    THIRD_STEP_BIRTH_DATE_CSS = '#claim_user_birthday_at'
    # Выбор документа
    THIRD_STEP_DOCUMENT_TYPE_PASSPORT_CSS = '#passport'
    THIRD_STEP_DOCUMENT_TYPE_OTHER_CSS = '#other_doc'
    # Если выбран паспорт
    # Паспортные данные
    THIRD_STEP_PASSPORT_SERIA_CSS = '#claim_user_passport_series_number'
    THIRD_STEP_PASSPORT_CODE_CSS = '#claim_user_passport_code'
    THIRD_STEP_PASSPORT_DATE_CSS = '#claim_user_passport_date'
    THIRD_STEP_PASSPORT_ISSUED_CSS = '#claim_user_passport_issued'
    # СНИЛС Заявителя
    THIRD_STEP_USER_SNILS_CSS = '#claim_user_snils'
    # Если выбран радиобатон "Иной документ":
    # Выпадающий список "Тип документа"
    THIRD_STEP_OTHER_TYPES_LIST_CSS = '.claim_user_doc_type .custom-combobox-toggle'
    THIRD_STEP_PASSPORT_MORIAKA_CSS = '#claim_user_doc_type_id option[value="1"]'
    THIRD_STEP_VOIENNIY_BILET_CSS = '#claim_user_doc_type_id option[value="1"]'
    THIRD_STEP_FOREIGN_PASSPORT_CSS = '#claim_user_doc_type_id option[value="1"]'
    THIRD_STEP_DRIVER_LICENSE_CSS = '#claim_user_doc_type_id option[value="1"]'
    THIRD_STEP_OTHER_DOC_INFO_CSS = '#claim_user_other_document'

    # Блок "Адрес по месту регистрации"
    THIRD_STEP_CLEAR_REG_ADDRESS_BUTTON_CSS = '#claim_user_reg_clear_address'  # Очистить адрес регистрации
    THIRD_STEP_REGISTRATION_DROPDOWN_VALUES_CSS = 'ul[style*="display: block"] > li'  # Первое значение из списка (
    # для всех выпадающих списков блока)
    THIRD_STEP_REGISTRATION_FULL_ADDRESS_CSS = '#claim_user_reg_fias_full_address'  # Поле ввода полного адреса
    THIRD_STEP_REGISTRATION_REGION_CSS = '#claim_user_reg_region ~ a'  # Раскрыть список значений региона
    THIRD_STEP_REGISTRATION_AREA_CSS = '#claim_user_reg_area ~ a'  # Раскрыть список значений района
    THIRD_STEP_REGISTRATION_CITY_CSS = '#claim_user_reg_city ~ a'  # Раскрыть список значений города
    THIRD_STEP_REGISTRATION_SETTLEMENT_CSS = '#claim_user_reg_settlement ~ a'  # Раскрыть список значений
    # населенных пунктов
    THIRD_STEP_REGISTRATION_STREET_CSS = '#claim_user_reg_street ~ a'  # Раскрыть список значений улиц
    THIRD_STEP_REGISTRATION_HOUSE_CSS = '#claim_user_reg_house'  # Поле ввода номера дома
    THIRD_STEP_REGISTRATION_CORPS_CSS = '#claim_user_reg_corps'  # Поле ввода номера корпуса
    THIRD_STEP_REGISTRATION_BUILDING_CSS = '#claim_user_reg_building'  # Поле ввода номера строения
    THIRD_STEP_REGISTRATION_INDEX_CSS = '#claim_user_reg_building'  # Поле ввода номера индекса

    # Блок адреса для направления корреспонденции
    THIRD_STEP_CLEAR_FACT_ADDRESS_BUTTON_CSS = '#claim_user_fact_clear_address'  # Очистить адрес для корреспонденции
    THIRD_STEP_ADDRESS_EQUAL_CHECKBOX_CSS = 'label[for="claim_user_is_address_equal"]'  # Чек-бокс "Совпадает с адресом
    # по месту регистрации"
    THIRD_STEP_FACT_FULL_ADDRESS_CSS = '#claim_user_fact_fias_full_address'  # Поле ввода полного адреса
    THIRD_STEP_FACT_REGION_CSS = '#claim_user_fact_region ~ a'  # Раскрыть список значений региона
    THIRD_STEP_FACT_AREA_CSS = '#claim_user_fact_area ~ a'  # Раскрыть список значений района
    THIRD_STEP_FACT_CITY_CSS = '#claim_user_fact_city ~ a'  # Раскрыть список значений города
    THIRD_STEP_FACT_SETTLEMENT_CSS = '#claim_user_fact_settlement ~ a'  # Раскрыть список значений
    # населенных пунктов
    THIRD_STEP_FACT_STREET_CSS = '#claim_user_fact_street ~ a'  # Раскрыть список значений улиц
    THIRD_STEP_FACT_HOUSE_CSS = '#claim_user_fact_house'  # Поле ввода номера дома
    THIRD_STEP_FACT_CORPS_CSS = '#claim_user_fact_corps'  # Поле ввода номера корпуса
    THIRD_STEP_FACT_BUILDING_CSS = '#claim_user_fact_building'  # Поле ввода номера строения
    THIRD_STEP_FACT_INDEX_CSS = '#claim_user_fact_building'  # Поле ввода номера индекса

    # Блок "Получение кассового чека при онлайн-оплате счета по заявке"
    THIRD_STEP_GET_RECEIPT_BY_EMAIL_CSS = '#is_email_receipt'
    THIRD_STEP_GET_RECEIPT_BY_PHONE_CSS = '#is_phone_receipt'
    THIRD_STEP_REFUSED_OF_RECEIPT_CSS = '#claim_receipt_refused'

    # Блок "Получение уведомлений о рассмотрении заявки"
    THIRD_STEP_EMAIL_NOTICE_CHECKBOX_CSS = '#user_email_notice'
    THIRD_STEP_PHONE_NOTICE_CHECKBOX_CSS = '#user_phone_notice'
    THIRD_STEP_AUTOINFORM_CHECKBOX_CSS = '#user_call_notice'

    # Блок кнопок навигации и сохранения заявки
    THIRD_STEP_BACK_BUTTON_CSS = '.card-controls a[href*="edit"]'
    THIRD_STEP_NEXT_STEP_CSS = '#nextStep'
