from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorQA_Contact_Us import Locators_Contact_Us
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils


class ContactUS_Page(Locators_Contact_Us):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step
    @allure.description('Navigate to CONTACT_US and click to display Contact_us page')
    def Click_Contact_Button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Contact_Us.CONTACT_US_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Check  text message displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text

    @allure.step
    @allure.description('Clear and insert data to FirstName input')
    def Insert_FirstName(self, First_Name):
        FirstName_Input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_Contact_Us.FIRST_NAME_XPATH)))
        FirstName_Input.clear()
        FirstName_Input.send_keys(First_Name)
        Utils(self.driver).assertion(First_Name, FirstName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to LastName input')
    def Insert_LastName(self, Last_Name):
        LastName_Input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_Contact_Us.LAST_NAME_XPATH)))
        LastName_Input.clear()
        LastName_Input.send_keys(Last_Name)
        Utils(self.driver).assertion(Last_Name, LastName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Email input')
    def Insert_Email(self, Email):
        Email_Input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_Contact_Us.EMAIL_XPATH)))
        Email_Input.clear()
        Email_Input.send_keys(Email)
        Utils(self.driver).assertion(Email, Email_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Phone_Number input')
    def Insert_Phone_number(self, Phone_Number):
        Phone_Number_Input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_Contact_Us.PHONE_NUMBER_XPATH)))
        Phone_Number_Input.clear()
        Phone_Number_Input.send_keys(Phone_Number)
        Utils(self.driver).assertion(Phone_Number, Phone_Number_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to Content Referral input')
    def Insert_Content_Referral(self, Text):
        Content_Referral_Input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_Contact_Us.CONTENT_REFERRAL_XPATH)))
        Content_Referral_Input.clear()
        Content_Referral_Input.send_keys(Text)
        Utils(self.driver).assertion(Text, Content_Referral_Input.get_attribute('value'))

    @allure.step
    @allure.description('Navigate to CONTACT_US and click to display Contact_us page')
    def Click_Send_Button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Contact_Us.SEND_XPATH).click()
        self.driver.implicitly_wait(50)

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
