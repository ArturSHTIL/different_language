import time


def test_checking_code_operability_for_different_languages(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
