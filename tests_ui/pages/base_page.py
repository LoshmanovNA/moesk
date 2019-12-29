from ..locators import CommonLocators
from seleniumbase import BaseCase

"""
Класс BaseCase фреймворка SeleniumBase инициализирует 
запуск и закрытие драйвера и содержит множество готовых
вспомогательных методов для работы с локаторами, базой данных,
окружениями и другими полезными удобными и готовыми вещами
которые можно найти в env/lib/python3.7/seleniumbase
"""


class BasePage(BaseCase):
    """
    CommonPage наследует все методы фреймворка BaseCase.
    Другие страницы (pages) будут наследовать CommonPage
    чтобы иметь доступ к методам общих для всех страниц элементов
    и методам фреймворка BaseCase
    """
    def should_be_main_page_lk(self):
        """Проверка успешной авторизации"""
        self.assert_element(CommonLocators.PROFILE_LINK)
