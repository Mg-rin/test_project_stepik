from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators


def test_guest_see_form_login(browser):
    url = MainPageLocators.MAIN_URL+LoginPageLocators.LOGIN_URL.format(getattr(browser, 'user_language', 'en-gb'))
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()

def test_guest_see_form_register(browser):
    url = MainPageLocators.MAIN_URL+LoginPageLocators.LOGIN_URL.format(getattr(browser, 'user_language', 'en-gb'))
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()