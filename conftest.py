import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    '''
    set the option to start the "browser"
    set the option to start the "language"
    '''
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Please choose language name to select")


@pytest.fixture(scope="session")
def browser(request):
    """
    Read language and browser
    """
    browser_name = request.config.getoption("browser_name")
    language_choose = request.config.getoption("language")

    if browser_name == "chrome":
        # initialize the Chrome browser with desired options
        print("\ninitialize Chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_choose})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        # initialize the Firefox browser with desired options
        print("\ninitialize Firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language_choose)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

