from abc import ABC, abstractmethod
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from lxml import etree
import time


class SeleniumScraper(ABC):
    """
    A scraper using Selenium library

    Methods
    -------
    visit_web(driver, url)
        Return an etree element of a web page
    etree_after_click(driver)
        Return an etree element of a web page visited via clicks
    parse()
        Abstract method for parse event
    store()
        Abstract method for data storage
    run()
        Run a Selenium scraper
    """
    def __init__(self):
        self.driver = webdriver.Firefox()

    def __del__(self):
        """Delete a driver after having finished using."""
        self.driver.quit()

    def visit_web(self, driver, url):
        """Return an etree element of a web page.

        Parameters
        ----------
        driver : selenium.webdriver
            The web driver performing visit actions
        url : str
            URL of the web page visited
        """
        driver.get(url)
        time.sleep(5)
        page = Soup(driver.page_source, features="html.parser")
        html_etree = etree.HTML(str(page))
        return html_etree

    def etree_after_click(self, driver):
        """Return an etree element of a web page visited via clicks.

        Parameters
        ----------
        driver : selenium.webdriver
              The web driver performing visit actions
        """
        time.sleep(5)
        page = Soup(driver.page_source, features="html.parser")
        html_etree = etree.HTML(str(page))
        return html_etree

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
        "Run a Selenium scraper."
        self.parse()
        self.store()
