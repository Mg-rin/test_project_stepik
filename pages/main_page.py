from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators, LoginPageLocators
from pages.routes import Routes


class MainPage(BasePage):

    def should_be_main_page(self):
        self.go_to_login_page()
        self.should_be_login_link_invalid()
        self.should_be_login_link()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.browser.current_url.split("/",4)[4] == f"{Routes.LOGIN_URL}".split('/',1)[1], "Подстрока login в текущем url браузера отсутствует"
        # print(f"{Routes.MAIN_URL}{self.browser.execute_script("return window.navigator.language || window.navigator.userLanguage")}{Routes.LOGIN_URL}") http://selenium1py.pythonanywhere.com/en/accounts/login/

    def should_be_login_link_invalid(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
