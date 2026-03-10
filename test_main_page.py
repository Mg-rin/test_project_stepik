import pytest

from pages.main_page import MainPage
from pages.routes import Routes
from pages.basket_page import BasketPage


@pytest.mark.xfail(reason = "LOGIN LINK INVALID")
def test_guest_can_go_to_login_page(browser):
    url = Routes.MAIN_URL
    page = MainPage(browser,url)
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина проверяем подстроку


def test_guest_should_see_login_link(browser):
    url = Routes.MAIN_URL
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = Routes.MAIN_URL
    page = MainPage(browser, url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.should_be_message_empty_basket()
