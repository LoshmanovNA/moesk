
class ClaimsFirstStepLocators:
    """Первый шаг подачи заявки"""

    # Кнопка выпадающего списка для выбор вида заявки
    FIRST_STEP_CLAIM_TYPE_BUTTON_CSS = 'span.selection span[role="presentation"]'

    # Виды заявки в выпадающем списке заявок на Технологическое присоединение
    FIRST_STEP_NEW_CONNECTION_XPATH = '//li[contains(text(), "Новое")]'  # Новое присоединение
    FIRST_STEP_TEMPORARY_CONNECTION_XPATH = '//li[contains(text(), "Временное")]'  # Временное присоединение
    FIRST_STEP_POWER_INCREASE_XPATH = '//li[contains(text(), "Увеличение мощности")]'  # Увеличение мощности
    FIRST_STEP_REASSIGNMENT_XPATH = '//li[contains(text(), "Переуступка")]'  # Переуступка
    FIRST_STEP_NETWORK_ORGANIZATION_XPATH = '//li[contains(text(), "Заявка сетевой организации")]'
    # Чек-бокс "Переуступка по собственному договору"
    FIRST_STEP_REASSIGNMENT_CHECKBOX_CSS = '#is_tu_cession_self_contract'
    # Поле "Номер заявки" при выбранном виде заявки "Переуступка"
    FIRST_STEP_REASSIGNMENT_CLAIM_NUMBER_CSS = '#claim_parent_number_1c'
    # Причина тех. присоединения при заявке сетевой организации от ЮЛ
    FIRST_STEP_NETWORK_ORGANIZATION_REASON_1 = '#claim_claim_reason_id_7'  # Сумма максимальных мощностей...
    FIRST_STEP_NETWORK_ORGANIZATION_REASON_2 = '#claim_claim_reason_id_8'  # Для обеспечения присоединения объектов...

    # Кнопка "Далее"
    FIRST_STEP_NEXT_BUTTON_CSS = '.card-controls button[type="Submit"]'
    FIRST_STEP_CANCEL_CLAIM_CSS = '.card-controls a[href="/"]'








