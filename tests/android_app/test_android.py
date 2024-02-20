from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_android(mobile_management_android):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
    results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
    results.should(have.size_greater_than(0))
    results.first.should(have.text('Appium'))


def test_open_another_text(mobile_management_android):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("House")
    results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
    results.first.should(have.text("House"))
    results.first.click()
