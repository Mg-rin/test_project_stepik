import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: e.g. en, es, fr, ru, en-gb"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nЗапуск браузера с языком: {user_language}")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.user_language = user_language
    yield browser
    browser.quit()