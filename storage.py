import ZODB.config


class Database(object):
    def __init__(self, path):
        self.db = ZODB.config.databaseFromURL('./zodb.conf')
        self.connection = self.db.open()
        self.dbroot = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()
