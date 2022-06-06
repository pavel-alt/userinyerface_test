from random import choice, randint
from time import sleep

from framework.base_page import BasePage
from framework.browser_factory import BrowserFactory
from framework.button import Button
from framework.text_field import TextField
from urls import URL_HOME


class AuthorizationPage(BasePage):
    check_element_xpath = "//form//div[2]/input"  # Поле ввода пароля' (xpath: str)
    name = "AuthorizationPage"  # (str -> сам придумай)
    path_to_page = "game.html"  # str -> скопируй  ------
    text_field_password_xpath = "//div[2]/input"  # класс TextField
    text_field_mail_xpath = "//div[1]/input"  # класс TextField
    choose_domain_field_xpath = "//div[3]/div[3]/input"  # класс TextField
    dropdown_opener_xpath = ".//div[@class='dropdown__opener']"  # класс Button +/-
    dropdown_list_xpath = './/div[@class="dropdown__list-item"]'
    checkbox_xpath = ".//span[contains(@class, 'checkbox__check')]"  # класс Button
    next_page_xpath = ".//a[text()='Next']"  # класс Button
    url = f'{URL_HOME}{path_to_page}'

    def __init__(self, driver):
        super().__init__(driver)
        self.text_field_password = TextField(driver, self.text_field_password_xpath)
        self.text_field_mail = TextField(driver, self.text_field_mail_xpath)
        self.choose_domain_field = TextField(driver, self.choose_domain_field_xpath)
        self.dropdown_opener = Button(driver, self.dropdown_opener_xpath)
        self.dropdown_list = Button(driver, self.dropdown_list_xpath)
        self.checkbox = Button(driver, self.checkbox_xpath)
        self.next_page = Button(driver, self.next_page_xpath)

    def logining(self, password, mail, domain, target_element=None):
        """Поочередно вызывает Password"""
        self.__send_password(password)
        sleep(2)
        self.__send_mail(mail)
        sleep(2)
        self.__send_domain(domain)
        sleep(2)
        self.__choose_domain_1st_order()

    def __send_password(self, password):
        """Вводит пароль"""
        self.text_field_password.clear_text_field()
        self.text_field_password.send_text(password)

    def __send_mail(self, mail):
        """Вводит @"""
        self.text_field_mail.clear_text_field()
        self.text_field_mail.send_text(mail)

    def __send_domain(self, domain):
        """Вводит домен"""
        self.choose_domain_field.clear_text_field()
        self.choose_domain_field.send_text(domain)

    def __choose_domain_1st_order(self, target_element=None):
        """Выбирает домен первого порядка"""
        self.dropdown_opener.click_on_element()
        if not target_element:
            len_all_elements = len(self.dropdown_list.find_elements_by_xpath())
            target_element_xpath = f'{self.dropdown_list_xpath}[{randint(0, len_all_elements + 1)}]'
            target_element = Button(self.driver, target_element_xpath)
        target_element.click_on_element()

    def accept_conditions(self):
        """ """
        self.checkbox.click_on_element()

    def click_to_the_next_page_button(self):
        """ """
        self.next_page.click_on_element()
