from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from QA_WEB.Locators.locatorsQA_Sidebar import Locators_SideBar
from QA_WEB.Utils.utils_QA import Utils


class SideBar_Page(Locators_SideBar):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Validates moving to "common question page')
    def Click_Common_Question_sidebar_link(self):

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
    @allure.description('Check  text message displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text