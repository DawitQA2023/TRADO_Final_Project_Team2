import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorsQA_Sidebar import Locators_SideBar
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils


class SideBar_Page(Locators_SideBar):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Validates moving to "common question page')
    def Click_Common_Question_sidebar_link(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SideBar.COMMON_QUESTION_XPATH).click()
        Utils(self.driver).assertion(Locators_SideBar.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Validates moving to "Contact Us page')
    def Click_ContactUs_sidebar_link(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SideBar.CONTACT_XPATH).click()
        Utils(self.driver).assertion(Locators_SideBar.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Validates moving to "Shopping method Page')
    def Click_Shopping_method_sidebar_link(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SideBar.SHIPPING_METHOD_XPATH).click()
        Utils(self.driver).assertion(Locators_SideBar.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Add product to cart')
    def Click_Product_to_cart(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SideBar.ADD_PRODUCT_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Check  text message displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text

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