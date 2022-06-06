from abc import ABC
from typing import Union
from selenium import webdriver

from framework.button import Button


class BasePage(ABC):
    check_element_xpath = ""
    name = ""
    url = ""

    def __init__(self, driver: Union[webdriver.Chrome]) -> None:
        self.driver = driver
        self.check_element = Button(driver, self.check_element_xpath)

    def open_page(self) -> None:
        """Метод переходит на страницу по УРЛ"""
        self.driver.get(self.url)  # переходим на сайт

    def check_open_page(self) -> bool:
        """Метод запускает ф-цию BaseElement.is_displayed -> Bool"""
        return self.check_element.check_visibility()
