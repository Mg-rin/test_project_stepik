from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    LOGIN_REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_REGISTER_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")



class ProductPageLocators:
    H_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    PR_PRODUCT = (By.CSS_SELECTOR,"div.product_main p.price_color")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    CART_NOTIFICATION = (By.CSS_SELECTOR,"#messages div.alert:first-child div.alertinner") # сообщение о добавление "has been added to your basket"
    CART_NOTIFICATION_H_PRODUCT = (By.CSS_SELECTOR,"#messages div.alert:first-child strong") # заголовок продукта h_product
    CART_NOTIFICATION_TOTAL = (By.CSS_SELECTOR,"#messages div.alert:nth-child(3) strong") # итоговая сумма в корзине

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



class BasketPageLocators:
    BASKET_LINK_PAGE = (By.CSS_SELECTOR,"span.btn-group a")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR,"#content_inner p")
    HEADER_TOTAL_BASKET = (By.CSS_SELECTOR, "div.sub-header h2" )
