from seleniumbase import BaseCase
from ..helpers.db_actions import DBManager
from ..locators import CommonLocators
from ..models.db_model import DBModel
from ..models.user_model import UserModel
from ...config_loader import Config


class BasePage(BaseCase):
    """
    BasePage наследует все методы фреймворка BaseCase.
    Другие страницы (pages) будут наследовать BasePage
    чтобы иметь доступ к методам общих для всех страниц элементов
    и методам фреймворка BaseCase
    """
    common_locators = CommonLocators()

    def setUp(self):
        """
        Действия перед выполнением тестов:
        - парсим config.ini,
        - создаем соединение с БД,
        - создаем класс с пользовательскими тестовыми данными
        """
        super(BasePage, self).setUp()

        config = Config()
        # For global environment use config['GLOBAL']
        env = config[self.env.upper()]  # Берем значение заданного окружения (TEST, PRODUCTION, etc)

        self.app_url = env['app_url']

        # Создание соединения с БД
        db_credentials = DBModel(env['db_host'],
                                 env['db_username'],
                                 env['db_password'],
                                 env['db_schema'],
                                 int(env['db_port']))
        self.connect = DBManager(db_credentials)

        # Данные тестового пользователя
        self.user_data = UserModel(user_login_fl=env['existing_user_fl'],
                                   user_login_ul=env['existing_user_ul'],
                                   user_login_ip=env['existing_user_ip'],
                                   password=env['password'],
                                   pass_hash=env['pass_hash'])

    def tearDown(self):
        """
        Действия после завершения тестов:
        Закрываем соединение с БД
        """
        self.connect.close_db()
        super(BasePage, self).tearDown()
