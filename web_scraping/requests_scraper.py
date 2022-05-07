from abc import ABC, abstractmethod
import requests


class RequestsScraper(ABC):
    """
    A scraper using requests library.

    Attributes
    ----------
    user_agent : str
        user agent parameter in header
    cookie : str
        cookie parameter in header

    Methods
    -------
    parse()
        Abstract method for parse event
    store()
        Abstract method for data storage
    run()
        Run a Selenium scraper
    """
    def __init__(self, user_agent, cookie):
        """
        Parameters
        ----------
        user_agent : str
            user agent parameter in header
        cookie : str
            cookie parameter in header
        """
        self.headers = {
            'User-Agent': user_agent,
            'Cookie': cookie}
    
    @abstractmethod
    def parse(self):
        """Customize your parse method.

        Raises
        ------
        NotImplementedError
            If the function is not overwritten.
        """
        raise NotImplementedError

    @abstractmethod
    def store(self):
        """Customize your store method.
        
        Raises
        ------
        NotImplementedError
            If the function is not overwritten.
        """
        raise NotImplementedError
    
    def run(self):
        """Run a requests scraper."""
        self.parse()
        self.store()
