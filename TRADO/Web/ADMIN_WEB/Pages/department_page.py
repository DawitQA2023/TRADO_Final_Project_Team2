import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.ADMIN_WEB.Locators.locators_Admin_Department import Locators_Dep
from TRADO.Web.ADMIN_WEB.Utils.utils_Admin import Utils


class Department_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Click User Menu Option ')
    def click_User_Menu_Option(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.DEPARTMENT_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Choose button ')
    def click_Kebab_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.CHOOSE).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Add button ')
    def click_Add_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.ADD_PRODUCT).click()
        self.driver.find_element(By.XPATH, Locators_Dep.X_BUTTON).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Export button ')
    def click_Export_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.EXPORT_PRODUCT).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Login Option')
    def click_Department(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.TITLE).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Department Option')
    def click_Department_From_sideBar(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.DASHBOARD).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Navigate to Search box and click Box ')
    def Click_SearchBox(self, value):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        value_input = self.driver.find_element(By.XPATH, Locators_Dep.SEARCH_BOX_XPATH)
        value_input.clear()
        value_input.send_keys(value)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Search box and click Box ')
    def Enter_Search_product(self, ProductName):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Dep.SEARCH_BOX_XPATH).click()
        ProductName_input = self.driver.find_element(By.XPATH, Locators_Dep.SEARCH_BOX_XPATH)
        ProductName_input.clear()
        ProductName_input.send_keys(ProductName)
        Utils(self.driver).assertion(ProductName, ProductName_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click Department Option')
    def click_Add_Count_From_Department(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.ADD_COUNT).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Department Option')
    def click_Drop_down_icon(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.DROP_ICON).click()
        self.driver.find_element(By.XPATH, Locators_Dep.LIST_NUM).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Choose button ')
    def click_ON_OFF_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.ADD_PRODUCT).click()
        self.driver.find_element(By.XPATH, Locators_Dep.ON__OFF).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Export button ')
    def click_ADD_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Dep.ON__OFF).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Check the alert text')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text
