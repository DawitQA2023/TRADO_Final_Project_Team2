import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorsQA_Search import Locators_Search
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils


class Search_Page(Locators_Search):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Navigate to Main page ')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to Search box and click Box ')
    def Click_SearchBox(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Search.SEARCH_BOX_XPATH).click()
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to Search Product input')
    def Enter_Search_product(self, ProductName):
        time.sleep(2)
        ProductName_input = self.driver.find_element(By.XPATH, Locators_Search.SEARCH_BOX_XPATH)
        ProductName_input.clear()
        ProductName_input.send_keys(ProductName)
        ProductName_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(ProductName, ProductName_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click DropDown search product list')
    def Click_Product_Empty_space(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Search.HEADER_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click DropDown search product list')
    def Click_Product_Search_DropDown_list(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Search.SEARCH_DROPDOWN_LIST_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Verify if signup page display')
    def Assert_Product_DisplayPage_displayed_Search_Item(self, path):
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, path).text
        return text

    @allure.step
    @allure.description('Check font size')
    def Check_font_size(self, path):
        return self.driver.find_element(By.CSS_SELECTOR, path).value_of_css_property("font-size")

    @allure.step
    @allure.description('Check font weight')
    def Check_font_weight(self, path):
        return self.driver.find_element(By.CSS_SELECTOR, path).value_of_css_property("font-weight")

    @allure.step
    @allure.description('Check text align')
    def Check_text_align(self, path):
        return self.driver.find_element(By.CSS_SELECTOR, path).value_of_css_property("text-align")


