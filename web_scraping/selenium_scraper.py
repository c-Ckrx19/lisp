from abc import ABC, abstractmethod
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from lxml import etree
import time


class SeleniumScraper(ABC):
    def __init__(self):
        self.driver = webdriver.Firefox()

    def __del__(self):
        self.driver.quit()

    def visit_web(self, driver, url):
        driver.get(url)
        time.sleep(5)
        page = Soup(driver.page_source, features="html.parser")
        html_etree = etree.HTML(str(page))
        return html_etree

    def etree_after_click(self, driver):
        time.sleep(5)
        page = Soup(driver.page_source, features="html.parser")
        html_etree = etree.HTML(str(page))
        return html_etree

    @abstractmethod
    def parse(self):
        raise NotImplementedError

    @abstractmethod
    def store(self):
        raise NotImplementedError
    
    def run(self):
        self.parse()
        self.store()
