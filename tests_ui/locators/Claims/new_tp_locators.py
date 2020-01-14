
class NewTPLocators:
    """Подача заявки на технологическое присоединение"""

    class FirstStep:
        """Первый шаг подачи заявки"""
        # Кнопка выпадающего списка для выбор вида заявки
        NEW_TP_CLAIM_TYPE_BUTTON_CSS = 'span.selection span[role="presentation"]'
        # Виды заявки в выпадающем списке
        NEW_TP_NEW_CONNECTION_CSS = 'span>ul>li:first-child'
        NEW_TP_TEMPORARY_CONNECTION_CSS = 'span>ul>li:nth-child(2)'
        NEW_TP_POWER_INCREASE_CSS = 'span>ul>li:nth-child(3)'
        NEW_TP_REASSIGNMENT_CSS = 'span>ul>li:nth-child(4)'
        # Кнопка "Далее"
        NEW_TP_NEXT_BUTTON_CSS = '#nextStep'
        NEW_TP_CANCEL_CLAIM_CSS = '.card-controls a[href="/"]'

    class SecondStep:
        """Второй шаг подачи заявки"""
        # Выбор даты рождения (выпадающий календарь)
        NEW_TP_BIRTH_DATE_CSS = '#claim_user_birthday_at'
        # Выбор документа
        NEW_TP_DOCUMENT_TYPE_PASSPORT_CSS = '#passport'
        NEW_TP_DOCUMENT_TYPE_OTHER_CSS = '#other_doc'
    # Если выбран паспорт
        # Паспортные данные
        NEW_TP_PASSPORT_SERIA_CSS = '#claim_user_passport_series_number'
        NEW_TP_PASSPORT_CODE_CSS = '#claim_user_passport_code'
        NEW_TP_PASSPORT_DATE_CSS = '#claim_user_passport_date'
        NEW_TP_PASSPORT_ISSUED_CSS = '#claim_user_passport_issued'
        # СНИЛС Заявителя
        NEW_TP_USER_SNILS_CSS = '#claim_user_snils'
    # Если выбран радиобатон "Иной документ":
        # Выпадающий список "Тип документа"
        NEW_TP_OTHER_TYPES_LIST_CSS = '.claim_user_doc_type .custom-combobox-toggle'
        NEW_TP_PASSPORT_MORIAKA_CSS = '#claim_user_doc_type_id option[value="1"]'
        NEW_TP_VOIENNIY_BILET_CSS = '#claim_user_doc_type_id option[value="1"]'
        NEW_TP_FOREIGN_PASSPORT_CSS = '#claim_user_doc_type_id option[value="1"]'
        NEW_TP_DRIVER_LICENSE_CSS = '#claim_user_doc_type_id option[value="1"]'
        NEW_TP_OTHER_DOC_INFO_CSS = '#claim_user_other_document'
        # Блок адреса по месту регистрации, заполняем поле полный адрес, остальные заполняются автоматически
        NEW_TP_FULL_REG_ADDRESS_CSS = '#claim_user_reg_fias_full_address'
        NEW_TP_CLEAR_REG_ADDRESS_BUTTON_CSS = '#claim_user_reg_clear_address'  # Очистить адрес регистрации
        # Блок адреса для направления корреспонденции
        NEW_TP_ADDRESS_EQUAL_CHECKBOX_CSS = 'label[for="claim_user_is_address_equal"]'  # Совпадает с адресом по месту регистрации
        NEW_TP_FULL_FACT_ADDRESS_CSS = '#claim_user_fact_fias_full_address'  # Полный адрес
        NEW_TP_CLEAR_FACT_ADDRESS_BUTTON_CSS = '#claim_user_fact_clear_address'  # Очистить адрес для направления корреспонденции
        # Блок "Получение кассового чека при онлайн-оплате счета по заявке"
        NEW_TP_GET_RECEIPT_BY_EMAIL_CSS = '#is_email_receipt'
        NEW_TP_GET_RECEIPT_BY_PHONE_CSS = '#is_phone_receipt'
        NEW_TP_REFUSED_OF_RECEIPT_CSS = '#claim_receipt_refused'
        # Блок "Получение уведомлений о рассмотрении заявки"
        NEW_TP_EMAIL_NOTICE_CHECKBOX_CSS = '#user_email_notice'
        NEW_TP_PHONE_NOTICE_CHECKBOX_CSS = '#user_phone_notice'
        NEW_TP_AUTOINFORM_CHECKBOX_CSS = '#user_call_notice'
        # Блок кнопок навигации и сохранения заявки
        NEW_TP_BACK_BUTTON_CSS = '.card-controls a[href*="edit"]'
        NEW_TP_NEXT_STEP = '#nextStep'

    class ThirdStep:
        """Третий шаг подачи заявки (Новое присоединение)"""
