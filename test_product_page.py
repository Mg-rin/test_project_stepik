import pytest
from pages.product_page import ProductPage
from pages.routes import Routes

#@pytest.mark.parametrize('product',['the-shellcoders-handbook_209/','coders-at-work_207/'])
#@pytest.mark.parametrize('parameter',['?promo=newYear','?promo=newYear2019'])

@pytest.mark.parametrize('product',['coders-at-work_207/'])
@pytest.mark.parametrize('parameter',[*[f'?promo=offer{i}' for i in range(10) if i!=7], pytest.param('?promo=offer7',marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser,product,parameter):
    url = Routes.CATALOG_PRODUCT.format(product)+parameter
    page = ProductPage(browser, url)
    page.open()
    page.should_be_product_page()



