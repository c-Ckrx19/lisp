from abc import ABC, abstractmethod
import requests


class RequestsScraper(ABC):
    def __init__(self, user_agent, cookie):
        self.headers = {
            'User-Agent': user_agent,
            'Cookie': cookie}
    
    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def store(self):
        pass
    
    def run(self):
        self.parse()
        self.store()
