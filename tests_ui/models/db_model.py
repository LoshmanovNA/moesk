

class DBModel:

    def __init__(self, db_server, db_user,
                 db_pass, db_schema, db_port):
        self.db_server = db_server
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_schema = db_schema
        self.db_port = db_port
