class CommonLocators:
    """Общие локаторы для каждой страницы ЛК"""
    COMMON_MAIN_LOGO_CSS = '.header-main_logo a'
    # Ссылка на профиль заявителя
    COMMON_PROFILE_LINK_CSS = 'a.profile-link'
    # Ссылка для логаута
    COMMON_LOGOUT_BUTTON_CSS = '#bs-header-menu a[href="/users/sign_out"]'
    # Кнопки подачи заявок
    COMMON_BUTTON_CLAIM_TP_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                   '@href, "new?operation_type_id=1")]'
    COMMON_BUTTON_CLAIM_CONSOLIDATION_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                              '@href, "new?operation_type_id=6")]'
    COMMON_BUTTON_CLAIM_DU_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                   '@href, "new?operation_type_id=5")]'
    COMMON_BUTTON_CLAIM_RECOVERY_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                         '@href, "new?operation_type_id=3")]'
    COMMON_BUTTON_CLAIM_REDISTRIBUTION_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                               '@href, "new?operation_type_id=2")]'
    # Разделы главного меню
    COMMON_MENU_CLAIM_CSS = '#bs-header-menu a[href="/claims"]'
    COMMON_MENU_MESSAGES_CSS = '#bs-header-menu a[href="/cabinet/messages"]'
    COMMON_MENU_ELECTRICITY_METERS_CSS = '#bs-header-menu a[href="/electricity_meter_readouts"]'

    class WarningPageLocators:
        """Страница с предупреждением о мошенниках"""
        # Кнопка "Ознакомлен" на странице предупреждения о мошенниках
        COMMON_WARNED_BUTTON_CSS = '.login-block a[href*="/claims"]'
        # Кнопка "Вернуться на портал"
        COMMON_GO_PORTAL_BUTTON_CSS = '.login-block a[href*="/claims"]'

    class PageNotFound:
        COMMON_404_PAGE_XPATH = '//h1[contains(text(), "Ошибка 404")]'
