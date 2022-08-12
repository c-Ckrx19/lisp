from abc import ABC, abstractmethod
import psycopg2


class PostgreSQL(ABC):
    def __init__(self, db, host, user, pwd, port):
        self.db = db
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(database=self.db,
                                     host=self.host,
                                     user=self.user,
                                     password=self.pwd,
                                     port=self.port)

    def create_database(self):
        pass
    
    @abstractmethod
    def read(self):
        raise NotImplementedError
    
    @abstractmethod
    def write(self):
        raise NotImplementedError
