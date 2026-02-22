import os
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators, LoginPageLocators


class MainPage(BasePage):

    def should_be_main_page(self):
        self.go_to_login_page()
        self.should_be_login_link_invalid()
        self.should_be_login_link()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.browser.current_url.split("/",4)[4] == f"{LoginPageLocators.LOGIN_URL}", "Подстрока login в текущем url браузера отсутствует"
        # print(f"{MainPageLocators.RESOURSE_URL}{self.browser.execute_script("return window.navigator.language || window.navigator.userLanguage")}{LoginPageLocators.LOGIN_URL}") http://selenium1py.pythonanywhere.com/en/accounts/login/

    def should_be_login_link_invalid(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
