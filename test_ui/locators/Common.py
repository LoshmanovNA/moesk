class CommonLocators:
    """Общие локаторы для каждой страницы ЛК"""
    # Ссылка на профиль заявителя
    PROFILE_LINK = 'a.profile-link'
    # Ссылка для логаута
    LOGOUT_BUTTON = '#bs-header-menu a[href="/users/sign_out"]'
    # Кнопки подачи заявок
    BUTTON_CLAIM_TP = '//div[@class="claim-types"]/a[contains(@href, "new?operation_type_id=1")]'  # XPATH
    BUTTON_CLAIM_CONSOLIDATION = '//div[@class="claim-types"]/a[contains(@href, "new?operation_type_id=6")]'  # XPATH
    BUTTON_CLAIM_DU = '//div[@class="claim-types"]/a[contains(@href, "new?operation_type_id=5")]'  # XPATH
    BUTTON_CLAIM_RECOVERY = '//div[@class="claim-types"]/a[contains(@href, "new?operation_type_id=3")]'  # XPATH
    BUTTON_CLAIM_REDISTRIBUTION = '//div[@class="claim-types"]/a[contains(@href, "new?operation_type_id=2")]'  # XPATH
    # Разделы главного меню
    MENU_CLAIM = '#bs-header-menu a[href="/claims"]'
    MENU_MESSAGES = '#bs-header-menu a[href="/cabinet/messages"]'
    MENU_ELECTRICITY_METERS = '#bs-header-menu a[href="/electricity_meter_readouts"]'

    class WarningPageLocators:
        """Страница с предупреждением о мошенниках"""
        # Кнопка "Ознакомлен" на странице предупреждения о мошенниках
        WARNED_BUTTON = '.login-block a[href*="/claims"]'
        # Кнопка "Вернуться на портал"
        GO_PORTAL_BUTTON = '.login-block a[href*="/claims"]'
