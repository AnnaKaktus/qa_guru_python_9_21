from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search_ios(mobile_management_ios):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("Wiki" + "\n")
    text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(be.clickable)
    text_output.should(have.text("Wiki"))
