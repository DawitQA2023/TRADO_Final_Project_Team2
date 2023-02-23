import allure
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.ADMIN_WEB.Locators.Pre_Requiremen_Locators.Pre_Requirement_Locators import Pre_Requirement_Locators
from TRADO.Web.ADMIN_WEB.Base.base_Chrome_Admin import Base_Chrome
from TRADO.Web.ADMIN_WEB.Base.base_FireFox_Admin import Base_FireFox


class Pre_Requirement_Login_Chrome(Base_Chrome):

    @allure.step
    @allure.description('Enter phone number')
    def enter_phone(self, phone_number):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH).send_keys(phone_number)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Send code button')
    def click_connect_send_main_code(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Enter phone number')
    def enter_Code(self, phone_number):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH).send_keys(phone_number)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Send code button')
    def click_connect_send_main_code(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Remember Me button')
    def click_RememberMe_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.REMEMEBER_ME_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.REMEMEBER_ME_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Connect button')
    def click_Connect_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.CONNECT_BUTTON_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.CONNECT_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click TRADO STORE MANAGEMENT button')
    def click_Trado_store_management_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.TRADO_STORE_MANAGEMENT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.TRADO_STORE_MANAGEMENT_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Dani Memetikim STORE MANAGEMENT button')
    def click_Dani_store_management_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.DANI_MEMETIKIM_STORE_MANAGEMENT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.DANI_MEMETIKIM_STORE_MANAGEMENT_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Dani Memetikim STORE MANAGEMENT button')
    def click_Language_button2(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.LANGUAGE_XPATH2)))
        self.driver.find_element(By.XPATH,Pre_Requirement_Locators.LANGUAGE_XPATH2).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click login button')
    def click_LogOut_Button(self):
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.LOGOUT_BUTTON_ICON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click login button')
    def click_LogOut_text_link(self):
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.LOGOUT_TEXT_LINK_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Navigate to ti dashboard and click dashboard')
    def click_dashBord(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.DASHBORD_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.LANGUAGE_XPATH2).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Successfully login using all info(Phone, code and Trado store manager, Chrome)')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store(self, set_up_Chrome):
        self.enter_phone("1951111111")
        self.click_connect_send_main_code()
        self.enter_Code("1234")
        self.click_RememberMe_button()
        self.click_Connect_button()
        self.click_Trado_store_management_button()

# **********************************************************for Daniel store manager **************************
    @allure.step
    @allure.description('Successfully login using all info(Phone, code and Dani store manager, Chrome)')
    @pytest.mark.usefixtures('set_up_Chrome')
    @pytest.fixture
    def Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Dani_store(self, set_up_Chrome):
        self.enter_phone("1951111111")
        self.click_connect_send_main_code()
        self.enter_Code("1234")
        self.click_RememberMe_button()
        self.click_Connect_button()
        self.click_Dani_store_management_button()


class Pre_Requirement_Login_Firefox(Base_FireFox):

    @allure.step
    @allure.description('Enter phone number')
    def enter_phone(self, phone_number):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH).send_keys(phone_number)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Send code button')
    def click_connect_send_main_code(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Enter phone number')
    def enter_Code(self, phone_number):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.PHONE_NUMBER_INPUT_XPATH).send_keys(phone_number)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Send code button')
    def click_connect_send_main_code(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.SEND_ME_CODE_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Remember Me button')
    def click_RememberMe_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.REMEMEBER_ME_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.REMEMEBER_ME_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Connect button')
    def click_Connect_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.CONNECT_BUTTON_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.CONNECT_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click TRADO STORE MANAGEMENT button')
    def click_Trado_store_management_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.TRADO_STORE_MANAGEMENT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.TRADO_STORE_MANAGEMENT_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Dani Memetikim STORE MANAGEMENT button')
    def click_Dani_store_management_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.DANI_MEMETIKIM_STORE_MANAGEMENT_XPATH)))
        self.driver.find_element(By.XPATH, Pre_Requirement_Locators.DANI_MEMETIKIM_STORE_MANAGEMENT_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Dani Memetikim STORE MANAGEMENT button')
    def click_Language_button2(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Pre_Requirement_Locators.LANGUAGE_XPATH2)))
        self.driver.find_element(By.XPATH,Pre_Requirement_Locators.LANGUAGE_XPATH2).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Successfully login using all info(Phone, code and Trado store manager, Firefox)')
    @pytest.mark.usefixtures('set_up_Firefox')
    @pytest.fixture
    def Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store(self, set_up_Firefox):
        self.enter_phone("1951111111")
        self.click_connect_send_main_code()
        self.enter_Code("1234")
        self.click_RememberMe_button()
        self.click_Connect_button()
        self.click_Trado_store_management_button()

