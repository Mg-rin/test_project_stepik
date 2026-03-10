import pytest
from conftest import browser
from test_data import generate_credentials
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.routes import Routes

@pytest.mark.guest_product
class TestGuestAddToBasketFromProductPage():
    @pytest.mark.parametrize('product',['the-city-and-the-stars_95/'])
    def test_guest_should_see_login_link_on_product_page(self,browser,product):
        url = Routes.CATALOG_PRODUCT.format(product)
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link() # проверка наличия ссылки на форму авторизации

    @pytest.mark.need_review
    @pytest.mark.xfail(reason='Не валидное значение')
    @pytest.mark.parametrize('product',['the-city-and-the-stars_95/'])
    def test_guest_can_go_to_login_page_from_product_page(self, browser, product):
        url = Routes.CATALOG_PRODUCT.format(product)
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page() # переход на форму авторизации

    @pytest.mark.need_review
    @pytest.mark.parametrize('product',['coders-at-work_207/']) #
    @pytest.mark.parametrize('parameter',[*[f'?promo=offer{i}' for i in range(3) if i!=2],
                                          pytest.param('?promo=offer2',marks=pytest.mark.xfail)]) # перечесления параметра через цикл и ислючение с ошибкой (в реальности ?promo=offer7) можно заменить на реальные значения range(10) if i!=7
    def test_guest_can_add_product_to_basket(self, browser,product,parameter):
        url = Routes.CATALOG_PRODUCT.format(product)+parameter # адрес страницы
        page = ProductPage(browser, url) # иницивлизация
        page.open() # открытие страницы
        page.should_be_product_page() # проверка (инф о товаре, добавление в корзину, сообщение)


    @pytest.mark.need_review
    @pytest.mark.parametrize('product',['the-city-and-the-stars_95/'])
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser,product):
        url = Routes.CATALOG_PRODUCT.format(product)
        page = ProductPage(browser, url)
        page.open()
        page.go_to_basket_page() # переход на страницу корзины
        basket_page = BasketPage(browser,browser.current_url) # инициализация
        basket_page.should_be_message_empty_basket() # проверка на наличие сообщения о пустой корзине

    @pytest.mark.parametrize('product', ['the-city-and-the-stars_95/'])
    def test_guest_can_see_total_in_basket(self, browser, product):
        url = Routes.CATALOG_PRODUCT.format(product)
        page = ProductPage(browser, url)
        page.open()
        page.add_product_basket() # добавление товара в корзину
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_message_total_in_basket()  # проверка на наличие блока с инф о карзине (итого)


    @pytest.mark.guest_product_negative
    class NegativeChecks:
        # Отрицательные проверки: Проверяем, что нет сообщения об успехе
        @pytest.mark.xfail(reason='Сообщение появляется после добаления товара в корзину')
        @pytest.mark.parametrize('product', ['coders-at-work_207/'])
        def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser, product):
            url = Routes.CATALOG_PRODUCT.format(product)
            page = ProductPage(browser, url)
            page.open()
            page.add_product_basket() # добавление товара в корзину
            page.should_not_be_success_message() # проверка на отсутствие успешного добавление

        @pytest.mark.parametrize('product', ['coders-at-work_207/'])
        def test_guest_cant_see_success_message(self,browser, product):
            url = Routes.CATALOG_PRODUCT.format(product)
            page = ProductPage(browser, url)
            page.open()
            page.should_not_be_success_message() #проверка на отсутствие успешного добавление

        @pytest.mark.xfail(reason='Сообщение не изчезает через 4с после добаления товара в корзину')
        @pytest.mark.parametrize('product', ['coders-at-work_207/'])
        def test_message_disappeared_after_adding_product_to_basket(self,browser, product):
            url = Routes.CATALOG_PRODUCT.format(product)
            page = ProductPage(browser, url)
            page.open()
            page.add_product_basket()
            page.should_disappeared_success_message()

        @pytest.mark.xfail(reason='Заголовок не отображается в пустой корзине')
        @pytest.mark.parametrize('product', ['the-city-and-the-stars_95/'])
        def test_guest_cant_see_total_in_basket(self,browser, product):
            url = Routes.CATALOG_PRODUCT.format(product)
            page = ProductPage(browser, url)
            page.open()
            page.go_to_basket_page() #
            basket_page = BasketPage(browser, browser.current_url) #
            basket_page.is_message_total_in_basket() # проверка на наличие блока с инф о карзине (итого)


@pytest.mark.user_product
@pytest.mark.parametrize('product', ['coders-at-work_207/'])
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = Routes.LOGIN_URL
        page = LoginPage(browser, url)
        email, password = generate_credentials()
        page.open()
        page.register_new_user(email, password) #регистрация нового пользователя
        page.should_be_authorized_user() #проверка на наличие значка авторизованного пользователя

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, product):
        url = Routes.CATALOG_PRODUCT.format(product) # адрес страницы
        page = ProductPage(browser, url)  # иницивлизация
        page.open()# открытие страницы
        page.get_product_info()  # получаем инф о товаре заголовок и стоимость
        page.add_product_basket()
        page.should_be_get_notification()  # получаем уведомление о добавление в корзину
        page.should_be_get_total_card()  # в корзине есть добавленый товар


    def test_user_cant_see_success_message(self,browser, product):
        url = Routes.CATALOG_PRODUCT.format(product)
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()  # проверка на отсутствие успешного добавление