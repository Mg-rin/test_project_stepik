from pages.main_page import MainPage
from pages.locators import MainPageLocators



def test_guest_can_go_to_login_page(browser):
    url = MainPageLocators.MAIN_URL
    page = MainPage(browser,url)
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина проверяем подстроку


def test_guest_should_see_login_link(browser):
    url = MainPageLocators.MAIN_URL
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()

