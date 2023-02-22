import time
from keyboard import press
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from QA_WEB.Locators.locatorsQA_Search import Locators_Search
from QA_WEB.Utils.utils_QA import Utils


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
        self.driver.find_element(By.XPATH, Locators_Search.SEARCH_BOX_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to Search Product input')
    def Enter_Search_product(self, ProductName):
        ProductName_input = self.driver.find_element(By.XPATH, Locators_Search.SEARCH_BOX_XPATH)
        ProductName_input.clear()
        ProductName_input.send_keys(ProductName)
        ProductName_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(ProductName, ProductName_input.get_attribute('value'))
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Click DropDown search product list')
    def Click_Product_Empty_space(self):
        self.driver.find_element(By.XPATH, Locators_Search.HEADER_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Click DropDown search product list')
    def Click_Product_Search_DropDown_list(self):
        self.driver.find_element(By.XPATH, Locators_Search.SEARCH_DROPDOWN_LIST_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Verify if signup page display')
    def Assert_Product_DisplayPage_displayed_Search_Item(self):
        text = self.driver.find_element(By.XPATH, Locators_Search.PRODUCT_DISPLAY_PAGE_XPATH).text
        return text





    # @allure.step
    # @allure.description('Navigate to Field Of Interest page and select Cocktail Field Of Interest From The List')
    # def Select_Cocktail_Field(self):
    #     self.wait.until(EC.url_to_be(self.driver.current_url))
    #     self.driver.find_element(By.XPATH, Locators_Search.COCKTAIL_XPATH).click()
    #     self.driver.implicitly_wait(50)
    #
    # @allure.step
    # @allure.description('Navigate to Field Of Interest page and select Restaurant Field Of Interest From The List')
    # def Select_Restaurant_Field(self):
    #     self.wait.until(EC.url_to_be(self.driver.current_url))
    #     self.driver.find_element(By.XPATH, Locators_Search.RESTAURANT_XPATH).click()
    #     self.driver.implicitly_wait(50)

    # @allure.step
    # @allure.description('Navigate to Field Of Interest page and Not select any Field Of Interest From The List')
    # def Click_Save_button(self):
    #     self.wait.until(EC.url_to_be(self.driver.current_url))
    #     self.driver.find_element(By.XPATH, Locators_Search.SAVE_BUTTON_XPATH).click()
    #     Utils(self.driver).assertion(Locators_Search.TITLE1, self.driver.title)
    #     self.driver.implicitly_wait(50)