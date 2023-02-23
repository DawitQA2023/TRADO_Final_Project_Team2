import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import AttachmentType


class Utils:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step
    @allure.description('This validation method, if the assert failed it will take screenshot')
    def assertion(self, expected, actual):
        driver = self.driver
        try:
            assert expected == actual
            self.driver.implicitly_wait(1000)

        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name='screenShot',attachment_type=AttachmentType.PNG)
            raise AssertionError
