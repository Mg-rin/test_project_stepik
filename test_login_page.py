from pages.login_page import LoginPage
from pages.routes import Routes


def test_guest_see_form_login(browser):
    url = Routes.MAIN_URL+Routes.LOGIN_URL.format(getattr(browser, 'user_language', 'en-gb'))
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()

def test_guest_see_form_register(browser):
    url = Routes.MAIN_URL+Routes.LOGIN_URL.format(getattr(browser, 'user_language', 'en-gb'))
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()