class CommonLocators:
    """Общие локаторы для каждой страницы ЛК"""
    COMMON_MAIN_LOGO_CSS = '.header-main_logo a'
    # Ссылка на профиль заявителя
    COMMON_PROFILE_LINK_CSS = 'a.profile-link'
    # Ссылка для логаута
    COMMON_LOGOUT_BUTTON_CSS = '#bs-header-menu a[href="/users/sign_out"]'

    # Разделы главного меню
    COMMON_MENU_CLAIM_CSS = '#bs-header-menu a[href="/claims"]'
    COMMON_MENU_MESSAGES_CSS = '#bs-header-menu a[href="/cabinet/messages"]'
    COMMON_MENU_ELECTRICITY_METERS_CSS = '#bs-header-menu a[href="/electricity_meter_readouts"]'

