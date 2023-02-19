import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from ADMIN_WEB.Locators.locators_Admin_Product import Locators_Product
from ADMIN_WEB.Utils.utils_Admin import Utils


class Product_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Navigate to Login page and click language option')
    def click_x(self):
        print("test")
