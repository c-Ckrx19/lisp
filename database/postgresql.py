from abc import ABC, abstractmethod


class PostgreSQL(ABC):
    def __init__(self):
        pass

    def connect(self):
        pass
    
    @abstractmethod
    def read(self):
        raise NotImplementedError
    
    @abstractmethod
    def write(self):
        raise NotImplementedError
