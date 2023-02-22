from time import sleep

import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Server.DataBase.MongoDB import login_code_Generating_query
from QA_WEB.Locators.Pre_Requiremen_Locators.Pre_Requirement_Locators import Pre_Requirement_Locators
from QA_WEB.Base.base_Chrome_QA import Base_Chrome
from QA_WEB.Base.base_FireFoxQA import Base_FireFox
from QA_WEB.Utils.utils_QA import Utils


class Pre_Requirement_Login_Chrome(Base_Chrome):
    @allure.step
    @allure.description('Click restaurant option field')
    def click_restaurants(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.RESTAURANTS)))
        if None:
            self.driver.refresh()
        else:
            self.driver.find_element(By.XPATH, Pre_Requirement_Locators.RESTAURANTS).click()

    @allure.step
    @allure.description('Click cocktails option field')
    def click_cocktails(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.COCKTAILS)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.COCKTAILS).click()

    @allure.step
    @allure.description('Click Save button')
    def click_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.SAVE_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.SAVE_BUTTON).click()

    @allure.step
    @allure.description('Click Login option on login page')
    def click_login_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.LOGIN_SECTION)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.LOGIN_SECTION).click()

    @allure.step
    @allure.description('Enter phone number')
    def enter_phone(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_FIELD)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_FIELD).send_keys(phone_number)

    @allure.step
    @allure.description('Click Connection button')
    def click_connect(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON).click()

    @allure.step
    @allure.description('Enter Sms Login code')
    def enter_Login_code(self, sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.assertion(place.get_attribute('value'), digit)

    @allure.step
    @allure.description('Successfully login using all info(restaurant,cocktails,phone, loginCode, connection button)')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def Valid_Login_With_login_Code(self, set_up_Chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        Phone = '0321321321'
        self.enter_phone(Phone)
        self.click_connect()
        sms = login_code_Generating_query(Phone)
        sleep(5)
        self.enter_Login_code(sms)
        self.click_connect()

    @allure.step
    @allure.description('Successfully Open Trado home page using(restaurant,cocktails) field')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def WithOut_login_selectField_restaurant_and_cocktails(self, set_up_Chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()

    @allure.step
    @allure.description('Successfully Open Trado home page using(restaurant) field')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def WithOut_login_selectField_restaurant(self, set_up_Chrome):
        self.click_restaurants()
        self.click_save_button()

    @allure.step
    @allure.description('Successfully Open Trado home page using(cocktails) field')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def WithOut_login_selectField_cocktails(self, set_up_Chrome):
        self.click_cocktails()
        self.click_save_button()

    @allure.step
    @allure.description('Successfully Open Trado home page using(none)field')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def WithOut_login_selectField_none(self, set_up_Chrome):
        self.click_save_button()


class Pre_Requirement_Login_Firefox(Base_FireFox):

    @allure.step
    @allure.description('Click restaurants option field')
    def click_restaurants(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.RESTAURANTS)))
        if None:
            self.driver.refresh()
        else:
            self.driver.find_element(By.XPATH, Pre_Requirement_Locators.RESTAURANTS).click()

    @allure.step
    @allure.description('Click cocktails option field')
    def click_cocktails(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.COCKTAILS)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.COCKTAILS).click()

    @allure.step
    @allure.description('Click Save button')
    def click_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.SAVE_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.SAVE_BUTTON).click()

    @allure.step
    @allure.description('Click Login option on login page')
    def click_login_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.LOGIN_SECTION)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.LOGIN_SECTION).click()

    @allure.step
    @allure.description('Enter phone number')
    def enter_phone(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_FIELD)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_FIELD).send_keys(phone_number)

    @allure.step
    @allure.description('Click Connection button')
    def click_connect(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON).click()

    @allure.step
    @allure.description('Enter Sms Login code')
    def enter_Login_code(self, sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.assertion(place.get_attribute('value'), digit)

    @allure.step
    @allure.description('Successfully login using all info(restaurant,cocktails,phone, loginCode, connection button)')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def Valid_Login_With_login_Code(self, set_up_Firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        Phone = '0321321321'
        self.enter_phone(Phone)
        self.click_connect()
        sms = login_code_Generating_query(Phone)
        sleep(5)
        self.enter_Login_code(sms)
        self.click_connect()

    @allure.step
    @allure.description('Successfully Open Trado home page using(restaurant,cocktails) field')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def WithOut_login_selectField_restaurant_and_cocktails(self, set_up_Firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()

    @allure.step
    @allure.description('Successfully Open Trado home page using(restaurant) field')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def WithOut_login_selectField_restaurant(self, set_up_Firefox):
        self.click_restaurants()
        self.click_save_button()

    @allure.step
    @allure.description('Successfully Open Trado home page using(cocktails) field')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def WithOut_login_selectField_cocktails(self, set_up_Firefox):
        self.click_cocktails()
        self.click_save_button()

    @allure.step
    @allure.description('Successfully Open Trado home page using(none)field')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def WithOut_login_selectField_none(self, set_up_Firefox):
        self.click_save_button()
