import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorsQA_Business_interface import Locators_BusinessInterface


class Business_Interface_Page(Locators_BusinessInterface):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Navigate business interface and click to business interface')
    def Click_Business_Interface_Box(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_BusinessInterface.BUSINESS_INTERFACE_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the first name in first name field box')
    def Enter_FirstName_box(self, First_Name):
        FirstName_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.FIRST_NAME_XPATH)))
        FirstName_input.clear()
        FirstName_input.send_keys(First_Name)
        Utils(self.driver).assertion(First_Name, FirstName_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the lase name in last name field box')
    def Enter_LastName_Box(self, Last_Name):
        LastName_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.LAST_NAME_XPATH)))
        LastName_input.clear()
        LastName_input.send_keys(Last_Name)
        Utils(self.driver).assertion(Last_Name, LastName_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the BnNumber in BnNumber field box')
    def Enter_BnNumber_box(self, BnNumber):
        BnNumber_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.BN_NUMBER_XPATH)))
        BnNumber_input.clear()
        BnNumber_input.send_keys(BnNumber)
        Utils(self.driver).assertion(BnNumber, BnNumber_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the Business Name in Business Name field box')
    def Enter_BusinessName_box(self, BusinessName):
        BusinessName_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.BUSINESS_NAME)))
        BusinessName_input.clear()
        BusinessName_input.send_keys(BusinessName)
        Utils(self.driver).assertion(BusinessName, BusinessName_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the SelectSection in Select Section field box')
    def Enter_SelectSection_box(self, SelectSection):
        SelectSection_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.SELECT_SECTION_XPATH)))
        SelectSection_input.clear()
        SelectSection_input.send_keys(SelectSection)
        Utils(self.driver).assertion(SelectSection, SelectSection_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the YourPhoneNumber in YourPhoneNumber field box')
    def Enter_YourPhoneNumber_box(self, YourPhoneNumber):
        Your_PhoneNumber_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.YOUR_PHONE_NUMBER_XPATH)))
        Your_PhoneNumber_input.clear()
        Your_PhoneNumber_input.send_keys(YourPhoneNumber)
        Utils(self.driver).assertion(YourPhoneNumber, Your_PhoneNumber_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the Your_PhoneNumber in Your_PhoneNumber field box')
    def Enter_HouseNumber_box(self, HouseNumber):
        HouseNumber_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.HOUSE_NUMBER_XPATH)))
        HouseNumber_input.clear()
        HouseNumber_input.send_keys(HouseNumber)
        Utils(self.driver).assertion(HouseNumber, HouseNumber_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the email in email field box')
    def Enter_Email_box(self, Email):
        Email_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.EMAIL_XPATH)))
        Email_input.clear()
        Email_input.send_keys(Email)
        Utils(self.driver).assertion(Email, Email_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the CityStreet in CityStreet field box')
    def Enter_CityStreet_box(self, Street):
        Street_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.STREET_XPATH)))
        Street_input.clear()
        Street_input.send_keys(Street)
        Utils(self.driver).assertion(Street, Street_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert the City in City field box')
    def Enter_City_box(self, City):
        City_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_BusinessInterface.CITY_XPATH)))
        City_input.clear()
        City_input.send_keys(City)
        Utils(self.driver).assertion(City, City_input.get_attribute('value'))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click send button')
    def Click_send_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_BusinessInterface.SEND_BUTTON_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Check  text message')
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