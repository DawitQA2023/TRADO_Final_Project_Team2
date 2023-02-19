import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from ADMIN_WEB.Locators.locators_Admin_User import Locators_User
from ADMIN_WEB.Utils.utils_Admin import Utils


class User_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Click User Menu Option ')
    def click_User_Menu_Option(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,Locators_User.USER_MENU_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Kabab button ')
    def click_Kebab_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.KEBAB_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Add button ')
    def click_Add_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Export button ')
    def click_Export_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.EXPORT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Add by brand button ')
    def click_Add_by_Brand_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_BY_BRAND_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Import button ')
    def click_Import_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.IMPORT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Import button ')
    def click_Tampet_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.TAMPLET_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to FirstName input')
    def enter_FirstName(self, FirstName):
        FirstName_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.FIRST_NAME_XPATH)))
        FirstName_Input.clear()
        FirstName_Input.send_keys(FirstName)
        Utils(self.driver).assertion(FirstName, FirstName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to LastName input')
    def enter_LastName(self, LastName):
        LastName_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.LAST_NAME_XPATH)))
        LastName_Input.clear()
        LastName_Input.send_keys(LastName)
        Utils(self.driver).assertion(LastName, LastName_Input.get_attribute('value'))
        time.sleep(5)
