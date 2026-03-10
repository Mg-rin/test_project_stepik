from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Сообщение о пустой корзине отсутствует!"
        print("Сообщение отображается")

#Негативные тесты
    def is_message_total_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.HEADER_TOTAL_BASKET), "Заголовок блока с общей суммой и информацией отсутствует"
        print("Заголовок с конечной стоймостью отображается")
