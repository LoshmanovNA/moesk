
class NewTPLocators:
    """Подача заявки на технологическое присоединение"""

    class FirstStep:
        """Первый шаг подачи заявки"""
        # Кнопка выпадающего списка для выбор вида заявки
        CLAIM_TYPE_BUTTON = 'span.selection span[role="presentation"]'
        # Виды заявки в выпадающем списке
        NEW_CONNECTION = 'span>ul>li:first-child'
        TEMPORARY_CONNECTION = 'span>ul>li:nth-child(2)'
        POWER_INCREASE = 'span>ul>li:nth-child(3)'
        PEREUSTUPKA = 'span>ul>li:nth-child(4)'
        # Кнопка "Далее"
        NEXT_BUTTON = '.card-controls button[type=submit]'
        CANCEL_CLAIM = '.card-controls a[href="/"]'

    class SecondStep:
        """Второй шаг подачи заявки"""
        # Выбор даты рождения (выпадающий календарь)
        BIRTH_DATE = '#claim_user_birthday_at'
        # Выбор документа
        DOCUMENT_TYPE_PASSPORT = '#passport'
        DOCUMENT_TYPE_OTHER = '#other_doc'
    # Если выбран паспорт
        # Паспортные данные
        PASSPORT_SERIA = '#claim_user_passport_series_number'
        PASSPORT_CODE = '#claim_user_passport_code'
        PASSPORT_DATE = '#claim_user_passport_date'
        PASSPORT_ISSUED = '#claim_user_passport_issued'
        # СНИЛС Заявителя
        USER_SNILS = '#claim_user_snils'
    # Если выбран радиобатон "Иной документ":
        # Выпадающий список "Тип документа"
        OTHER_TYPES_LIST = '.claim_user_doc_type .custom-combobox-toggle'
        PASSPORT_MORIAKA = '#claim_user_doc_type_id option[value="1"]'
        VOIENNIY_BILET = '#claim_user_doc_type_id option[value="1"]'
        FOREIGN_PASSPORT = '#claim_user_doc_type_id option[value="1"]'
        DRIVER_LICENSE = '#claim_user_doc_type_id option[value="1"]'
        OTHER_DOC_INFO = '#claim_user_other_document'
        # Блок адреса по месту регистрации, заполняем поле полный адрес, остальные заполняются автоматически
        FULL_REG_ADDRESS = '#claim_user_reg_fias_full_address'
        CLEAR_REG_ADDRESS_BUTTON = '#claim_user_reg_clear_address'  # Очистить адрес регистрации
        # Блок адреса для направления корреспонденции
        ADDRESS_EQUAL_CHECKBOX = 'label[for="claim_user_is_address_equal"]'  # Совпадает с адресом по месту регистрации
        FULL_FACT_ADDRESS = '#claim_user_fact_fias_full_address'  # Полный адрес
        CLEAR_FACT_ADDRESS_BUTTON = '#claim_user_fact_clear_address'  # Очистить адрес для направления корреспонденции
        # Блок "Получение кассового чека при онлайн-оплате счета по заявке"
        GET_RECEIPT_BY_EMAIL = '#is_email_receipt'
        GET_RECEIPT_BY_PHONE = '#is_phone_receipt'
        REFUSED_OF_RECEIPT = '#claim_receipt_refused'
        # Блок "Получение уведомлений о рассмотрении заявки"
        EMAIL_NOTICE_CHECKBOX = '#user_email_notice'
        PHONE_NOTICE_CHECKBOX = '#user_phone_notice'
        AUTOINFORM_CHECKBOX = '#user_call_notice'
        # Блок кнопок навигации и сохранения заявки
        BACK_BUTTON = '.card-controls a[href*="edit"]'

    class ThirdStep:
        """Третий шаг подачи заявки (Новое присоединение)"""
