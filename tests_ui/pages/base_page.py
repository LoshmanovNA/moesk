import logging

from seleniumbase import BaseCase
from ..helpers.db_actions import DBManager
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
        self.app_url = env['app_url']  # Берем app_url адрес из соответствующего env в config.ini
        self.logger = logging.getLogger(__name__)

        # Создание соединения с БД на тесте
        if self.env == 'test':
            db_credentials = DBModel(env['db_host'],
                                     env['db_username'],
                                     env['db_password'],
                                     env['db_schema'],
                                     int(env['db_port']))
            self.connect = DBManager(db_credentials)
        # Данные тестового пользователя в тестовой среде
            self.config_data = UserModel(user_login_fl=env['existing_user_fl'],
                                         user_login_ul=env['existing_user_ul'],
                                         user_login_ip=env['existing_user_ip'],
                                         user_login_representative=env['existing_user_representative'],
                                         password=env['password'],
                                         pass_hash=env['pass_hash'])
        # Данные тестового пользователя на проде
        elif self.env == 'production':
            self.config_data = UserModel(user_login_fl=env['existing_user_fl'],
                                         user_login_ul=env['existing_user_ul'],
                                         user_login_ip=env['existing_user_ip'],
                                         user_login_representative=env['existing_user_representative'],
                                         password=env['password'])
        # Открываем стартовую страницу
        self.get(self.app_url)

    def tearDown(self):
        """
        Действия после завершения тестов:
        Закрываем соединение с БД
        """
        if self.env == 'test':
            self.connect.close_db()
        super(BasePage, self).tearDown()

    def teardown_method(self, method):
        self.assert_true(self.logger_soft.status, self.logger_soft.message)
