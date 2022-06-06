from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class BrowserFactory:
    @staticmethod
    def get_driver() -> webdriver.Chrome:
        service = ChromeService(executable_path=ChromeDriverManager().install())  # устанавливаем драйвер
        driver = webdriver.Chrome(service=service)  # и создаем его инстанс
        return driver
