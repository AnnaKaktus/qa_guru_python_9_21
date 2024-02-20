import allure
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser
from config import creds
from utils import attaches


@pytest.fixture
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3a",
        "app": "bs://sample.app",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": creds.user_name,
            "accessKey": creds.access_key
        }
    })
    browser.config.driver = webdriver.Remote(creds.remote_url, options=options)
    yield
    attaches.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step("Tear down app session"):
        browser.quit()

    attaches.attach_bstack_video(session_id)


@pytest.fixture
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities({
        "app": "bs://sample.app",
        "deviceName": "iPhone 8",
        "platformName": "ios",
        "platformVersion": "13",
        "bstack:options": {
            "userName": creds.user_name,
            "accessKey": creds.access_key,
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test"
        }
    })
    browser.config.driver = webdriver.Remote(creds.remote_url, options=options)
    yield
    attaches.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step("Tear down app session"):
        browser.quit()

    attaches.attach_bstack_video(session_id)
