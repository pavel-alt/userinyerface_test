from framework.base_page import BasePage
from framework.button import Button
from urls import URL_HOME


class HomePage(BasePage):
    check_element_xpath = '//div[3]/button'  # Кнопка 'NO' (xpath: str)
    name = 'HomePage'  # (str -> сам придумай)
    url = URL_HOME   # str -> скопируй
    next_page_xpath = '//div[4]/p/a'  # класс Button

    def __init__(self, driver):
        super().__init__(driver)
        self.next_page = Button(driver, self.next_page_xpath)

    def click_to_the_next_page_button(self):
        self.next_page.click_on_element()
