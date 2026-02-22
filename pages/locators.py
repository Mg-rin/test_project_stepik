from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = '{}/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")

