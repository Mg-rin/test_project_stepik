from pages.product_page import ProductPage
from pages.routes import Routes

def test_guest_can_add_product_handbook_209_to_basket(browser):
    url = Routes.CATALOG+Routes.PRODUCT_HANDBOOK_209+Routes.PARAMETER_PR_NEWYEAR
    page = ProductPage(browser, url)
    page.open()
    page.should_be_product_page()


def test_guest_can_add_product_work_207_to_basket(browser):
    url = Routes.CATALOG+Routes.PRODUCT_WORK_207+Routes.PARAMETER_PR_NEWYEAR_2019
    page = ProductPage(browser, url)
    page.open()
    page.should_be_product_page()
