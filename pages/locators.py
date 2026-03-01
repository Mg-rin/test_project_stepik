from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")


class ProductPageLocators:
    H_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    PR_PRODUCT = (By.CSS_SELECTOR,"div.product_main p.price_color")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    CART_NOTIFICATION = (By.CSS_SELECTOR,"#messages div.alert:first-child div.alertinner") # сообщение о добавление "has been added to your basket"
    CART_NOTIFICATION_H_PRODUCT = (By.CSS_SELECTOR,"#messages div.alert:first-child strong") # заголовок продукта h_product
    CART_NOTIFICATION_TOTAL = (By.CSS_SELECTOR,"#messages div.alert:nth-child(3) strong") # итоговая сумма в корзине