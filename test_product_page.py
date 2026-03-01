from pages.product_page import ProductPage
from pages.routes import Routes

def test_guest_can_add_product_to_basket(browser):
    url = Routes.MAIN_URL+Routes.PRODUCT_HANDBOOK_209.format(getattr(browser, 'user_language', 'en-gb'))+Routes.PARAMETER
    page = ProductPage(browser, url)
    page.open()
    page.should_be_product_page()