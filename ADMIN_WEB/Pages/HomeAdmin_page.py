import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from ADMIN_WEB.Locators.locators_Admin_HOME import Locators_HOME


class Home_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Click Login Option')
    def click_Logo(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,Locators_HOME.LOGO_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click main dashboard Option')
    def click_main_dashboard (self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.DASHBORD_XPATH1).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Humburger icon')
    def click_Humburger_icon(self):
        self.driver.find_element(By.XPATH, Locators_HOME.HUMBURGER_ICON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.HUMBURGER_ICON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)
    @allure.step
    @allure.description('Click Product menu')
    def click_Product_menu(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.MAIN_SCREEN_PRODUCT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click User menu')
    def click_User_menu(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.MAIN_SCREEN_USER_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click ORDER menu')
    def click_Order_menu(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.MAIN_SCREEN_ORDER_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Language icon')
    def click_US_Language_icon(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.US_LANGUAGE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Language icon')
    def click_IL_Language_icon(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_HOME.IL_LANGUAGE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

