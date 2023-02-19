import time
from time import sleep
import random
import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Server.DataBase.MongoDB import login_code_Generating_query
from TRADO.QA_WEB.Locators.Pre_Requiremen_Locators.Pre_Requirement_Locators import Pre_Requirement_Locators
from TRADO.QA_WEB.Base.base_Chrome_QA import Base_Chrome
from TRADO.QA_WEB.Base.base_FireFoxQA import Base_FireFox
from QA_WEB.Utils.utils import Utils


class Pre_Requirement_SignUp_Chrome(Base_Chrome):
    @allure.step
    @allure.description('Click restaurant option field')
    def click_restaurants(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.RESTAURANTS)))
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
    @allure.description('Click Registration option on Signup page')
    def click_Signup_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.REGISTRATION_OPTION_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.REGISTRATION_OPTION_XPATH).click()

    @allure.step
    @allure.description('Enter phone number')
    def enter_phone(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_FIELD)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_FIELD).send_keys(phone_number)

    @allure.step
    @allure.description('Enter Bn number')
    def enter_BnNumber(self, BnNumber):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.BN_NUMBER_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.BN_NUMBER_XPATH).send_keys(BnNumber)

    @allure.step
    @allure.description('Click agree term box')
    def Click_agree_term_box(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.AGREE_TERM_BOX_PATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.AGREE_TERM_BOX_PATH).click()

    @allure.step
    @allure.description('Click Connection button')
    def click_connect(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON).click()

    @allure.step
    @allure.description('Click Trado logo')
    def click_Trado_logo(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.TRADO_LOGO)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.TRADO_LOGO).click()
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Enter Sms Login code')
    def enter_Login_code(self, sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.assertion(place.get_attribute('value'), digit)
        time.sleep(2)

    @allure.step
    @allure.description('Successfully Signup using all info(restaurant,cocktails,phone, loginCode, connection button)')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def Valid_SignUp_With_login_Code(self, set_up_Chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.click_Signup_section()
        newPhone = random.randint(1000000000,10000000000)  # this number need to be chage every time
        PhoneNum = newPhone
        self.enter_phone(PhoneNum)
        self.enter_BnNumber("12345678910")
        self.Click_agree_term_box()
        self.click_connect()
        sms = login_code_Generating_query(PhoneNum)
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


class Pre_Requirement_SignUp_Firefox(Base_FireFox):

    @allure.step
    @allure.description('Click restaurant option field')
    def click_restaurants(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.RESTAURANTS)))
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
    @allure.description('Click Registration option on Signup page')
    def click_Signup_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.REGISTRATION_OPTION_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.REGISTRATION_OPTION_XPATH).click()

    @allure.step
    @allure.description('Enter phone number')
    def enter_phone(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_FIELD)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_FIELD).send_keys(phone_number)

    @allure.step
    @allure.description('Enter Bn number')
    def enter_BnNumber(self, BnNumber):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.BN_NUMBER_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.BN_NUMBER_XPATH).send_keys(BnNumber)

    @allure.step
    @allure.description('Click agree term box')
    def Click_agree_term_box(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.AGREE_TERM_BOX_PATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.AGREE_TERM_BOX_PATH).click()

    @allure.step
    @allure.description('Click Connection button')
    def click_connect(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.CONNECT_BUTTON).click()

    @allure.step
    @allure.description('Click Trado logo')
    def click_Trado_logo(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Pre_Requirement_Locators.TRADO_LOGO)))
        self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.TRADO_LOGO).click()
        self.driver.implicitly_wait(50)
        time.sleep(2)

    @allure.step
    @allure.description('Enter Sms Login code')
    def enter_Login_code(self, sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.assertion(place.get_attribute('value'), digit)
        time.sleep(2)

    @allure.step
    @allure.description('Successfully login using all info(restaurant,cocktails,phone, loginCode, connection button)')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def Valid_SignUp_With_login_Code(self, set_up_Firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.click_Signup_section()
        newPhone = random.randint(1000000000, 10000000000)  # this number need to be chage every time
        PhoneNum = newPhone
        self.enter_phone(PhoneNum)
        self.enter_BnNumber("12345678910")
        self.Click_agree_term_box()
        self.click_connect()
        sms = login_code_Generating_query(PhoneNum)
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
