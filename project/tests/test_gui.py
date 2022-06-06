from time import sleep

from project.pages.authorization_page import AuthorizationPage
from project.pages.home_page import HomePage
from project.pages.introduction_page import IntroductionPage


def test_fill_the_form(driver):
    """ 1. Перейти на сайт по ссылке https://userinyerface.com/game.html%20target=   => Welcome page открыта
        2. Перейти по ссылке к следующей странице (Please click HERE to GO to the next page)  =>
                                                                        Открыта 1 карточка для заполнения информации
        3. Ввести случайный корректный пароль, email, принять условия использования, нажать кнопку Next   =>
                                                                        Открыта 2 карточка для заполнения информации
        4. Выбрать 3 случайных интереса, загрузить любое изображение, нажать кнопку Next     =>
                                                                        Открыта 3 карточка для заполнения информации
    """

    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.check_open_page(), 'welcome page is not open'

    home_page.click_to_the_next_page_button()
    authorization_page = AuthorizationPage(driver)
    assert authorization_page.check_open_page(), 'authorization page is not open'
    sleep(2)
    authorization_page.logining('Aд34567890', 'Aaa', 'gmail')  # TODO Автоматизировать генерацию данных
    authorization_page.accept_conditions()
    authorization_page.click_to_the_next_page_button()
    introduction_page = IntroductionPage(driver)
    assert introduction_page.check_open_page(), 'introduction page is not open'
