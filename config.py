import configparser


class Config:
    """Хранение и использование переменных окружения"""
    _env = {}

    def __init__(self, path='config.ini'):
        config = configparser.ConfigParser()
        config.read([path])
        for section in config.sections():
            self._env[section] = dict(config.items(section))

    def __getitem__(self, key):
        if key not in self._env:
            raise Exception("'%s' key is not found in env configuration from config.ini" % key)
        return self._env[key]

    def __contains__(self, env):
        return env in self._env

    def get_global_variable(self):
        return self._env['GLOBAL']

a = Config()
print(a['TEST'])
