
class NewTPLocators:
    """Подача заявки на Новое технологическое присоединение"""

    class FirstStep:
        """Первый шаг подачи заявки"""
    # Кнопка выпадающего списка для выбор вида заявки
        NEW_TP_CLAIM_TYPE_BUTTON_CSS = 'span.selection span[role="presentation"]'
    # Виды заявки в выпадающем списке
        NEW_TP_NEW_CONNECTION_CSS = 'span>ul>li:first-child'  # Новое присоединение
        NEW_TP_TEMPORARY_CONNECTION_CSS = 'span>ul>li:nth-child(2)'  # Временное присоединение
        NEW_TP_POWER_INCREASE_CSS = 'span>ul>li:nth-child(3)'  # Увеличение мощности
        NEW_TP_REASSIGNMENT_CSS = 'span>ul>li:nth-child(4)'  # Переуступка
    # Чек-бокс "Переуступка по собственному договору"
        NEW_TP_REASSIGNMENT_CHECKBOX_CSS = '#is_tu_cession_self_contract'
    # Поле "Номер заявки" при выбранном виде заявки "Переуступка"
        NEW_TP_REASSIGNMENT_CLAIM_NUMBER_CSS = '#claim_parent_number_1c'
    # Кнопка "Далее"
        NEW_TP_NEXT_BUTTON_CSS = '.card-controls button[type="Submit"]'
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

    # Блок "Адрес по месту регистрации"
        NEW_TP_CLEAR_REG_ADDRESS_BUTTON_CSS = '#claim_user_reg_clear_address'  # Очистить адрес регистрации
        NEW_TP_REGISTRATION_DROPDOWN_VALUES_CSS = 'ul[style*="display: block"] > li'  # Первое значение из списка (
        # для всех выпадающих списков блока)
        NEW_TP_REGISTRATION_FULL_ADDRESS_CSS = '#claim_user_reg_fias_full_address'  # Поле ввода полного адреса
        NEW_TP_REGISTRATION_REGION_CSS = '#claim_user_reg_region ~ a'  # Раскрыть список значений региона
        NEW_TP_REGISTRATION_AREA_CSS = '#claim_user_reg_area ~ a'  # Раскрыть список значений района
        NEW_TP_REGISTRATION_CITY_CSS = '#claim_user_reg_city ~ a'  # Раскрыть список значений города
        NEW_TP_REGISTRATION_SETTLEMENT_CSS = '#claim_user_reg_settlement ~ a'  # Раскрыть список значений
        # населенных пунктов
        NEW_TP_REGISTRATION_STREET_CSS = '#claim_user_reg_street ~ a'  # Раскрыть список значений улиц
        NEW_TP_REGISTRATION_HOUSE_CSS = '#claim_user_reg_house'  # Поле ввода номера дома
        NEW_TP_REGISTRATION_CORPS_CSS = '#claim_user_reg_corps'  # Поле ввода номера корпуса
        NEW_TP_REGISTRATION_BUILDING_CSS = '#claim_user_reg_building'  # Поле ввода номера строения
        NEW_TP_REGISTRATION_INDEX_CSS = '#claim_user_reg_building'  # Поле ввода номера индекса

    # Блок адреса для направления корреспонденции
        NEW_TP_CLEAR_FACT_ADDRESS_BUTTON_CSS = '#claim_user_fact_clear_address'  # Очистить адрес для корреспонденции
        NEW_TP_ADDRESS_EQUAL_CHECKBOX_CSS = 'label[for="claim_user_is_address_equal"]'  # Чек-бокс "Совпадает с адресом
        # по месту регистрации"
        NEW_TP_FACT_FULL_ADDRESS_CSS = '#claim_user_fact_fias_full_address'  # Поле ввода полного адреса
        NEW_TP_FACT_REGION_CSS = '#claim_user_fact_region ~ a'  # Раскрыть список значений региона
        NEW_TP_FACT_AREA_CSS = '#claim_user_fact_area ~ a'  # Раскрыть список значений района
        NEW_TP_FACT_CITY_CSS = '#claim_user_fact_city ~ a'  # Раскрыть список значений города
        NEW_TP_FACT_SETTLEMENT_CSS = '#claim_user_fact_settlement ~ a'  # Раскрыть список значений
        # населенных пунктов
        NEW_TP_FACT_STREET_CSS = '#claim_user_fact_street ~ a'  # Раскрыть список значений улиц
        NEW_TP_FACT_HOUSE_CSS = '#claim_user_fact_house'  # Поле ввода номера дома
        NEW_TP_FACT_CORPS_CSS = '#claim_user_fact_corps'  # Поле ввода номера корпуса
        NEW_TP_FACT_BUILDING_CSS = '#claim_user_fact_building'  # Поле ввода номера строения
        NEW_TP_FACT_INDEX_CSS = '#claim_user_fact_building'  # Поле ввода номера индекса

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
        NEW_TP_NEXT_STEP_CSS = '#nextStep'

    class ThirdStep:
        """Третий шаг подачи заявки (Новое присоединение)"""
    # Блок "Энергопринимющие устройства"
        NEW_TP_EPU_TYPE_DROPDOWN_CSS = '.epu_epu_type > .custom-combobox > a'  # Наименование ЭПУ (открыть список)
        NEW_TP_EPU_TYPES_LIST_CSS = '.epu_epu_type ul li:nth-child(2)'  # Первое значение в списке
        NEW_TP_CADASTRAL_YES_CSS = '#cadastral_availability_yes'  # Кадастровый номер есть (радиобатон)
        NEW_TP_CADASTRAL_NO_CSS = '#cadastral_availability_no'  # Кадастровый номер отсутствует (радиобатон)
        NEW_TP_INPUT_CADASTRAL_CSS = '#epu_cadastral_number'  # Поле ввода кадастрового номера
        NEW_TP_FIND_CADASTRAL_BUTTON_CSS = '#find-adds'  # Кнопка поиска адреса на Росреестре
        NEW_TP_CUSTOM_ADDRESS_CHECKBOX_CSS = '#epu_custom_address_toggler'  # Чек-бокс "Указать адрес в
        # произвольной форме"
        NEW_TP_EPU_FULL_ADDRESS_CSS = '#epu_fias_full_address'  # Поле ввода полного адреса
        NEW_TP_EPU_REGION_CSS = '#epu_region ~ a'  # Раскрыть список значений региона
        NEW_TP_EPU_AREA_CSS = '#epu_area ~ a'  # Раскрыть список значений района
        NEW_TP_EPU_CITY_CSS = '#epu_city ~ a'  # Раскрыть список значений города
        NEW_TP_EPU_SETTLEMENT_CSS = '#epu_settlement ~ a'  # Раскрыть список значений
        # населенных пунктов
        NEW_TP_EPU_STREET_CSS = '#epu_street ~ a'  # Раскрыть список значений улиц
        NEW_TP_EPU_HOUSE_CSS = '#epu_house'  # Поле ввода номера дома
        NEW_TP_EPU_CORPS_CSS = '#epu_corps'  # Поле ввода номера корпуса
        NEW_TP_EPU_BUILDING_CSS = '#epu_building'  # Поле ввода номера строения
        NEW_TP_EPU_INDEX_CSS = '#epu_postcode'  # Поле ввода номера индекса

    # Блок "Мощность и напряжение"
        NEW_TP_MAX_POWER_CSS = '#epu_max_power'  # Ввод максимальной мощности для присоединения
        NEW_TP_VOLTAGE_LIST_CSS = 'div.epu_voltage_level span  a'  # Раскрыть список классов напряжения
        NEW_TP_VOLTAGE_VALUE_XPATH = '//div[text()="380 вольт"]'  # Выбор значения напряжения
        # Блок категории надежности при мощности до 150 кВт
        NEW_TP_RELIABILITY_LIST_CSS = '.epu_reliability_level span a'  # Раскрыть список категорий надежности
        NEW_TP_RELIABILITY_VALUE_XPATH = '//div[text()="3"]'  # Выбор значения категории надежности
        # Блок категории надежности при мощности свыше 150 кВт
        NEW_TP_RELIABILITY_INPUT_XPATH = '//input[@id="3"]'  # Выбор значения категории надежности

    # Блок "Количество точек присоединения"
        NEW_TP_EPU_POINTS_CSS = '#epu_point_count'  # Ввод количества точек присоединения
        NEW_TP_EPU_POINTS_INFO_CSS = '#point_count_info'  # Инфоблок при количестве точек более 4
        NEW_TP_EPU_POINT1_DESCRIBE_CSS = 'input[name="connection_point[0][name]"]'  # Описание точки 1
        NEW_TP_EPU_POINT2_DESCRIBE_CSS = 'input[name="connection_point[1][name]"]'  # Описание точки 2
        NEW_TP_EPU_POINT1_POWER_CSS = 'input[name="connection_point[0][power]"]'  # Мощность точки 1
        NEW_TP_EPU_POINT2_POWER_CSS = 'input[name="connection_point[1][power]"]'  # Мощность точки 2

    # Блок количества и мощности трансформаторов





