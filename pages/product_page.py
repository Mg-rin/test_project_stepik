from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.routes import Routes


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.check_parameter()
        self.get_product_info() # получаем инф о товаре заголовок и стоимость
        self.add_product_basket() # добавляем товар в корзину
        self.solve_quiz_and_get_code()
        self.should_be_get_notification() # получаем уведомление о добавление в корзину
        self.should_be_get_total_card() # в корзине есть добавленый товар


    def check_parameter(self):
        current_url_is = self.browser.current_url
        for parameter in Routes.PARAMETERS:
            if parameter in current_url_is:
                assert parameter in current_url_is, f"{current_url_is=}"
        print(f"Параметр в url есть {self.browser.current_url}")


    def get_product_info(self):
        self.product = self.browser.find_element(*ProductPageLocators.H_PRODUCT).text
        self.price = self.browser.find_element(*ProductPageLocators.PR_PRODUCT).text
        assert self.product, "Название товара не вывелось"
        print(f"Товар:{self.product}")
        assert self.price, "Стоимость товара не вывелась"
        print(f"Цена:{self.price}")


    def add_product_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()


    def should_be_get_notification(self):
        self.notification = self.browser.find_element(*ProductPageLocators.CART_NOTIFICATION_H_PRODUCT).text
        assert self.product == self.notification, \
                f"Название товара не совпадает. Ожидалось: {self.product}, Получено: {self.notification}"
        print(f"Название в уведомление совпадает. Ожидалось: {self.product}, Получено: {self.notification}")


    def should_be_get_total_card(self):
        self.notification_total = self.browser.find_element(*ProductPageLocators.CART_NOTIFICATION_TOTAL).text
        assert self.price in self.notification_total, \
                f"Стоимость корзины не совпадает. Ожидалось: {self.price}, Получено: {self.notification_total}"
        print(f"✓ Стоимость корзины совпадает с ценой товара. Ожидалось: {self.price}, Получено: {self.notification_total}")


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CART_NOTIFICATION), \
       "Success message is presented, but should not be"


    def should_disappeared_success_message(self):
        assert  self.is_disappeared(*ProductPageLocators.CART_NOTIFICATION), \
       "Success message is presented, but should disappeared"