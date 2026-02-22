from selenium.webdriver.common.by import By


class MainPageLocators():
    RESOURSE_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    LOGIN_URL = 'accounts/login/'
