"""
This file organizes connection details to the Testcase Database.
"""

from config import Config

# Environments
env = "test"

config = Config()
creds = config[env.upper()]

class Apps:
    TESTCASE_REPOSITORY = "testcase_repository"


APP_CREDS = {

    Apps.TESTCASE_REPOSITORY: {
        env: (
            creds['db_host'],
            creds['db_username'],
            creds['db_password'],
            creds['db_schema'],
            int(creds['db_port']))
    },

}
print(Apps.TESTCASE_REPOSITORY)
