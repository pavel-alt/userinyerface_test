from random import sample

from framework.base_os_integration import BaseOsIntegration
from framework.base_page import BasePage
from framework.button import Button
from framework.text import Text


class IntroductionPage(BasePage):
    check_element_xpath = './/a[@class="avatar-and-interests__upload-button"]'  # Кнопка/ссыль 'upload' (xpath: str)
    name = "IntroductionPage"  # (str -> сам придумай)
    url = "/game.html"  # str -> скопируй
    upload_link_xpath = './/a[@class="avatar-and-interests__upload-button"]'  # класс Button
    checkboxes_xpath = './/span[contains(@class, "checkbox__box")]'  # класс Button
    next_page_button_xpath = './/button[text()="Next"]'  # класс Button
    unwanted_xpath_list = ['.//label[@for="interest_unselectall" ]/span', './/label[@for="interest_selectall" ]/span']
    unselect_all_xpath = './/label[@for="interest_unselectall" ]/span'
    number_of_interests_xpath = '//div[3]/h2'

    def __init__(self, driver):
        super().__init__(driver)
        self.check_element = Button(driver, self.check_element_xpath)
        self.upload_link = Button(driver, self.upload_link_xpath)
        self.checkboxes = Button(driver, self.checkboxes_xpath)
        self.next_page_button = Button(driver, self.next_page_button_xpath)
        self.unselect_all = Button(driver, self.unselect_all_xpath)
        self.number_of_interests = Text(driver, self.number_of_interests_xpath)

    def upload_photo(self, path_2_photo):
        """
        1.Нажимает кнопку 'upload'
        2. Вводит путь к фото
        3. Нажимает 'enter'
        """
        self.upload_link.click_on_element()
        BaseOsIntegration.type_write(path_2_photo)
        BaseOsIntegration.press_kw_button('enter')

    def __get_number_interests(self):
        return [int(s) for s in str.split(self.number_of_interests.read_text()) if s.isdigit()][0]  # TODO Сделать лучше

    def choose_interests(self):     # TODO оптимизировать, мб разделить на методы
        """
        1. Нажимает кнопку 'Unselect All'
        2. Создает список вариантов, исключая 'Unselect All' и 'Select All'
        3. Выбирает рандомно 3 элемента из списка
        4. Кликает их
        """
        self.unselect_all.click_on_element()

        all_interests = self.checkboxes.find_elements_by_xpath()
        for xpath in self.unwanted_xpath_list:
            web_el = Button(self.driver, xpath).find_element_by_xpath()
            all_interests.remove(web_el)

        for el in sample(all_interests, self.__get_number_interests()):
            el.click()

    def click_to_the_next_page_button(self):
        """Нажимает кнопку 'Next' """
        self.next_page_button.click_on_element()
