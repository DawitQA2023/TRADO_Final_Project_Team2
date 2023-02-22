
import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from QA_WEB.Locators.locatorsQA_Payment import Locators_Payment
from QA_WEB.Utils.utils_QA import Utils

class Payment_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Check  text message "Please fill out this field." displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text

    @allure.step
    @allure.description("CHENGE LANGUEGE TO ENTER PAYMENT PAGE")
    def Click_change_language_Page(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Payment.PAYMENT_CHANGE_LANGUAGE_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description("SELECT ITEM TO ADD TO CART")
    def Add_products_to_cart(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Payment.SELECT_ITEM_XPATH).click()
        self.driver.implicitly_wait(20)
        # Item = 0
        # for product in range(21):
        #     self.wait.until(EC.url_to_be(self.driver.current_url))
        #     self.driver.find_element(By.XPATH, f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{Item+1}]/div[1]/div[2]/div[1]/img[1]").click()
        #     self.Click_plus_button()
        #     self.driver.implicitly_wait(20)
        #     self.driver.back()
        #     Item += 1

    @allure.step
    @allure.description("ADD SELECTED ITEM TO CART")
    def Click_plus_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Payment.PLUS_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)
        time.sleep(1)

    @allure.step
    @allure.description("Click Payment Button")
    def Click_payment_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Payment.PAYMENT_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description("Click open Payment button payment to display Check out page")
    def Valid_open_payment_page(self):
        self.Add_products_to_cart()
        self.Click_plus_button()
        self.Click_payment_button()

    @allure.step
    @allure.description('Clear and insert data to Business input')
    def Enter_Business_name(self, BusinessName):
        BusinessName_input = self.driver.find_element(By.XPATH, Locators_Payment.BUSINESS_NAME_XPATH)
        BusinessName_input.clear()
        BusinessName_input.send_keys(BusinessName)
        BusinessName_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(BusinessName, BusinessName_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Bn number input')
    def Enter_BN_Number(self, BnNumber):
        BnNumber_input = self.driver.find_element(By.XPATH, Locators_Payment.BN_NUMBER_XPATH)
        BnNumber_input.clear()
        BnNumber_input.send_keys(BnNumber)
        BnNumber_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(BnNumber, BnNumber_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Email input')
    def Enter_Email(self, Email):
        Email_input = self.driver.find_element(By.XPATH, Locators_Payment.EMAIL_XPATH)
        Email_input.clear()
        Email_input.send_keys(Email)
        Email_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Email, Email_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to City input')
    def Enter_City(self, City):
        City_input = self.driver.find_element(By.XPATH, Locators_Payment.CITY_XPATH)
        City_input.clear()
        City_input.send_keys(City)
        City_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(City, City_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Street input')
    def Enter_Street(self, Street):
        Street_input = self.driver.find_element(By.XPATH, Locators_Payment.STREET_XPATH)
        Street_input.clear()
        Street_input.send_keys(Street)
        Street_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Street, Street_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Home Number input')
    def Enter_Home_number(self, Home_Num):
        Home_Num_input = self.driver.find_element(By.XPATH, Locators_Payment.HOUSENUMBER_XPATH)
        Home_Num_input.clear()
        Home_Num_input.send_keys(Home_Num)
        Home_Num_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Home_Num, Home_Num_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Entrance Number input')
    def Enter_Entrance_Number(self, Entrance):
        Entrance_input = self.driver.find_element(By.XPATH, Locators_Payment.ENTRANCE_NUMBER_XPATH)
        Entrance_input.clear()
        Entrance_input.send_keys(Entrance)
        Entrance_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Entrance, Entrance_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Floor Number input')
    def Enter_Floor_Number(self, Floor):
        Floor_input = self.driver.find_element(By.XPATH, Locators_Payment.FLOOR_XPATH)
        Floor_input.clear()
        Floor_input.send_keys(Floor)
        Floor_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Floor, Floor_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description("enter data to All Invoice Detail field")
    def Enter_all_Invoice_detail_filed(self, BusinessName, BnNumber, Email, City, Street, Home_Num, Entrance, Floor):
        self.Enter_Business_name(BusinessName)
        self.Enter_BN_Number(BnNumber)
        self.Enter_Email(Email)
        self.Enter_City(City)
        self.Enter_Street(Street)
        self.Enter_Home_number(Home_Num)
        self.Enter_Entrance_Number(Entrance)
        self.Enter_Floor_Number(Floor)

    # -----------------------------------------------------------------------------------------------------------------

    @allure.step
    @allure.description('Clear and insert data to Shipping City input')
    def Enter_Shipping_city_name(self, Shipping_City):
        Shipping_City_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_CITY_XPATH)
        Shipping_City_input.clear()
        Shipping_City_input.send_keys(Shipping_City)
        Shipping_City_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Shipping_City, Shipping_City_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Shipping Street input')
    def Enter_Shipping_Street(self, Shipping_Street):
        Shipping_Street_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_STREET_XPATH)
        Shipping_Street_input.clear()
        Shipping_Street_input.send_keys(Shipping_Street)
        Shipping_Street_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Shipping_Street, Shipping_Street_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Shipping Home number input')
    def Enter_Shipping_Home_number(self, Shipping_Home_number):
        Shipping_Home_number_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_HOUSENUMBER_XPATH)
        Shipping_Home_number_input.clear()
        Shipping_Home_number_input.send_keys(Shipping_Home_number)
        Shipping_Home_number_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Shipping_Home_number, Shipping_Home_number_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Shipping Entrance input')
    def Enter_Shipping_Entrance(self, Shipping_Entrance):
        Shipping_Entrance_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_ENTRANCE_XPATH)
        Shipping_Entrance_input.clear()
        Shipping_Entrance_input.send_keys(Shipping_Entrance)
        Shipping_Entrance_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Shipping_Entrance, Shipping_Entrance_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Shipping Floor input')
    def Enter_Shipping_Floor(self, Shipping_Floor):
        Shipping_Floor_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_FLOOR_XPATH)
        Shipping_Floor_input.clear()
        Shipping_Floor_input.send_keys(Shipping_Floor)
        Shipping_Floor_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Shipping_Floor, Shipping_Floor_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Contact name input')
    def Enter_Shipping_Contact_name(self, Contact_name):
        Contact_name_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_CONTACT_NAME_XPATH)
        Contact_name_input.clear()
        Contact_name_input.send_keys(Contact_name)
        Contact_name_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(Contact_name, Contact_name_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to First Name input')
    def Enter_Shipping_First_Name(self, FirstName):
        FirstName_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_FIRST_NAME_XPATH)
        FirstName_input.clear()
        FirstName_input.send_keys(FirstName)
        FirstName_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(FirstName, FirstName_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to LastName input')
    def Enter_Shipping_Last_Name(self, LastName):
        LastName_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_LAST_NAME_XPATH)
        LastName_input.clear()
        LastName_input.send_keys(LastName)
        LastName_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(LastName, LastName_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Shipping PhoneNumber input')
    def Enter_Shipping_PhoneNumber(self, PhoneNumber):
        PhoneNumber_input = self.driver.find_element(By.XPATH, Locators_Payment.SHIPPING_PHONE_NUMBER_XPATH)
        PhoneNumber_input.clear()
        PhoneNumber_input.send_keys(PhoneNumber)
        PhoneNumber_input.send_keys(Keys.RETURN)
        Utils(self.driver).assertion(PhoneNumber, PhoneNumber_input.get_attribute('value'))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description("enter data to All Shipping Address field")
    def Enter_all_Shipping_Address_filed(self, Shipping_City, Shipping_Street, Shipping_Home_number, Shipping_Entrance, Shipping_Floor, Contact_name, FirstName, LastName, PhoneNumber):
        self.Enter_Shipping_city_name(Shipping_City)
        self.Enter_Shipping_Street(Shipping_Street)
        self.Enter_Home_number(Shipping_Home_number)
        self.Enter_Entrance_Number(Shipping_Entrance)
        self.Enter_Floor_Number(Shipping_Floor)
        self.Enter_Shipping_Contact_name(Contact_name)
        self.Enter_Shipping_First_Name(FirstName)
        self.Enter_Shipping_Last_Name(LastName)
        self.Enter_Shipping_PhoneNumber(PhoneNumber)

    @allure.step
    @allure.description("Click Complete Purchase Button")
    def Click_Complete_Purchase_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Payment.COMPLETE_PURCHASE_BUTTON).click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
