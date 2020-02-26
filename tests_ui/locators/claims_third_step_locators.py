
class ClaimsThirdStepLocators:
    """Третий шаг подачи заявки (Новое присоединение)"""

    # Первое значение в активном выпадающем списке
    THIRD_STEP_FIRST_VALUE_FROM_LIST_CSS = 'ul[style*="display: block"] > li[tabindex]'

    # Блок "Энергопринимющие устройства"
    THIRD_STEP_EPU_TYPE_FIELD_CSS = 'div.epu_epu_type > span > a'  # Наименование ЭПУ (открыть список)
    THIRD_STEP_CADASTRAL_YES_CSS = 'label[for="cadastral_availability_yes"]'  # Кадастровый номер есть (радиобатон)
    THIRD_STEP_CADASTRAL_NO_CSS = 'label[for="cadastral_availability_no"]'  # Кадастровый номер отсутствует (радиобатон)
    THIRD_STEP_INPUT_CADASTRAL_CSS = 'input#epu_cadastral_number'  # Поле ввода кадастрового номера
    THIRD_STEP_FIND_CADASTRAL_BUTTON_CSS = '#find-adds'  # Кнопка поиска адреса на Росреестре
    THIRD_STEP_CUSTOM_ADDRESS_CHECKBOX_CSS = 'label[for="epu_custom_address_toggler"]'  # Чек-бокс "Указать адрес в произвольной форме"
    THIRD_STEP_CUSTOM_ADDRESS_TEXTAREA_CSS = 'textarea#epu_custom_address'

    # Адрес ЭПУ
    THIRD_STEP_EPU_FULL_ADDRESS_CSS = 'input#epu_fias_full_address'  # Поле ввода полного адреса
    THIRD_STEP_EPU_REGION_FIELD_CSS = 'input#epu_region'  # Поле ввода значений региона
    THIRD_STEP_EPU_AREA_FIELD_CSS = 'input#epu_area'  # Поле ввода значений района
    THIRD_STEP_EPU_CITY_FIELD_CSS = 'input#epu_city'  # Поле ввода значений города
    THIRD_STEP_EPU_SETTLEMENT_FIELD_CSS = 'input#epu_settlement'  # Поле ввода значений населенных пунктов
    THIRD_STEP_EPU_STREET_CSS = 'input#epu_street'  # Поле ввода значений улиц
    THIRD_STEP_EPU_HOUSE_CSS = 'input#epu_house'  # Поле ввода номера дома
    THIRD_STEP_EPU_CORPS_CSS = 'input#epu_corps'  # Поле ввода номера корпуса
    THIRD_STEP_EPU_BUILDING_CSS = 'input#epu_building'  # Поле ввода номера строения
    THIRD_STEP_EPU_INDEX_CSS = 'input#epu_postcode'  # Поле ввода номера индекса
    THIRD_STEP_EPU_CLEAR_BUTTON_CSS = 'input#epu_clear_address'  # Кнопка очистить адрес

    # Блок "Мощность и напряжение"
    THIRD_STEP_MAX_POWER_CSS = 'input#epu_max_power'  # Ввод максимальной мощности для присоединения
    THIRD_STEP_PRE_POWER_CSS = 'input#epu_pre_power'  # Ранее согласованная мощность
    THIRD_STEP_VOLTAGE_LIST_CSS = 'div.epu_voltage_level span'  # Раскрыть список классов напряжения
    THIRD_STEP_VOLTAGE_LEVEL_220V_XPATH = '//li[contains(text(), "220 вольт")]'  # Выбор значения напряжения 220 В
    THIRD_STEP_VOLTAGE_LEVEL_380V_XPATH = '//li[contains(text(), "380 вольт")]'  # Выбор значения напряжения 380 В
    THIRD_STEP_VOLTAGE_LEVEL_6KV_XPATH = '//li[contains(text(), "6 кВ")]'  # Выбор значения напряжения 6 кВ
    THIRD_STEP_VOLTAGE_LEVEL_10KV_XPATH = '//li[contains(text(), "10 кВ")]'  # Выбор значения напряжения 10 кВ
    THIRD_STEP_VOLTAGE_LEVEL_20KV_XPATH = '//li[contains(text(), "20 кВ")]'  # Выбор значения напряжения 20 кВ
    THIRD_STEP_VOLTAGE_LEVEL_35KV_XPATH = '//li[contains(text(), "35 кВ")]'  # Выбор значения напряжения 35 кВ
    THIRD_STEP_VOLTAGE_LEVEL_110KV_XPATH = '//li[contains(text(), "110 кВ")]'  # Выбор значения напряжения 110 кВ
    # Блок категории надежности при мощности до 150 кВт
    THIRD_STEP_RELIABILITY_LIST_CSS = '.epu_reliability_level span'  # Раскрыть список категорий надежности
    THIRD_STEP_DROPDOWN_RELIABILITY_LEVEL_ONE_XPATH = '//li[text()="1"]'  # Выпадающий список. Выбор значения категории надежности 1
    THIRD_STEP_DROPDOWN_RELIABILITY_LEVEL_TWO_XPATH = '//li[text()="2"]'  # Выпадающий список. Выбор значения категории надежности 2
    THIRD_STEP_DROPDOWN_RELIABILITY_LEVEL_THREE_XPATH = '//li[text()="3"]'  # Выпадающий список. Выбор значения категории надежности 3
    # Блок категории надежности при мощности свыше 150 кВт
    THIRD_STEP_INPUT_RELIABILITY_LEVEL_ONE_CSS = 'input[id="1"]'  # Поле значения категории надежности 1
    THIRD_STEP_INPUT_RELIABILITY_LEVEL_TWO_CSS = 'input[id="2"]'  # Поле значения категории надежности 2
    THIRD_STEP_INPUT_RELIABILITY_LEVEL_THREE_CSS = 'input[id="3"]'  # Поле значения категории надежности 3

    # Блок "Количество точек присоединения"
    THIRD_STEP_EPU_POINTS_CSS = 'input#epu_point_count'  # Ввод количества точек присоединения
    THIRD_STEP_EPU_POINTS_INFO_CSS = '#point_count_info'  # Инфоблок при количестве точек более 4
    THIRD_STEP_EPU_POINT1_DESCRIBE_CSS = 'input[name="connection_point[0][name]"]'  # Описание точки 1
    THIRD_STEP_EPU_POINT1_POWER_CSS = 'input[name="connection_point[0][power]"]'  # Мощность точки 1

    # Блок количества и мощности трансформаторов
    THIRD_STEP_EPU_COUNT_TRANS_CSS = 'input#epu_count_trans'  # Количество трансформаторов
    THIRD_STEP_EPU_POWER_TRANS_CSS = 'input#epu_power_trans'  # Мощность трансформаторов
    THIRD_STEP_EPU_COUNT_GENERATOR_CSS = 'input#epu_count_generator'  # Количество генераторов
    THIRD_STEP_EPU_POWER_GENERATOR_CSS = 'input#epu_power_generator'  # Мощность генераторов
    THIRD_STEP_EPU_LOAD_TYPE_CSS = 'input#epu_nature_load'  # Характер нагрузки
    THIRD_STEP_EPU_TECHNOLOGICAL_MINIMUM_CSS = 'input#epu_technological_minimum_values_generators'  # Величина и обоснование технологич. минимума
    THIRD_STEP_EPU_NEED_ARMOR_CSS = 'input#epu_need_technological_armor'  # Необходимость брони
    THIRD_STEP_EPU_REASON_ARMOR_CSS = 'input#epu_value_justification_technological_armor'  # Обоснование брони

    # Блок "Ввод объекта в эксплуатацию"
    THIRD_STEP_EPU_OBJECT_READY_CSS = 'label[for="object_is_ready"]'  # Объект построен
    THIRD_STEP_EPU_OBJECT_NOT_READY_CSS = 'label[for="object_is_not_ready"]'  # Объект строится
    THIRD_STEP_EPU_OBJECTS_STEPS_CSS = 'label[for="objects_steps"]'  # Поэтапный ввод объекта

    # Блок кнопок навигации и сохранения заявки
    THIRD_STEP_BACK_BUTTON_CSS = '.card-controls a[href*="claims"]'
    THIRD_STEP_NEXT_STEP_CSS = '#nextStep'
    THIRD_STEP_SAVE_DRAFT_CSS = 'a.link[href="/"]'
