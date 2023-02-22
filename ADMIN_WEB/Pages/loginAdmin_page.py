import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.support.wait import WebDriverWait
from ADMIN_WEB.Locators.locators_Admin_Login import Locators_Login,Locators_LogOut
from ADMIN_WEB.Utils.utils_Admin import Utils


class Login_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to Login page and click language option')
    def click_Language_option(self):
        self.driver.find_element(By.XPATH, Locators_Login.LANGUAGE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)
        time.sleep(2)

    @allure.step
    @allure.description('Navigate to Login page and click language option')
    def click_dashBord(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Login.DASHBORD_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)
        time.sleep(2)


    @allure.step
    @allure.description('Navigate to Login page and click Phone entering box')
    def click_LoginBox(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Login.PHONEBOX_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Phone input')
    def enter_Phone(self, Phone):
        Phone_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Login.PHONEBOX_XPATH)))
        Phone_Input.clear()
        Phone_Input.send_keys(Phone)
        Utils(self.driver).assertion(Phone, Phone_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click Send code button')
    def click_Send_me_code_Button(self):
        self.driver.find_element(By.XPATH, Locators_Login.SEND_ME_CODE_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Check the alert text message "no such user" displayed')
    def Assert_no_such_user_messages(self):
        actual = self.driver.find_element(By.XPATH, Locators_Login.NO_SUCH_USER_TEXT_XPATH)
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "faild to login" displayed')
    def Assert_fill_in_messages(self):
        time.sleep(1)
        actual = self.driver.find_element(By.XPATH, Locators_Login.FILL_IN_PATH)
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "faild to login" displayed')
    def Assert_faild_to_login_messages(self):
        actual = self.driver.find_element(By.XPATH, Locators_Login.FAILED_TO_LOGIN)
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Store name" displayed')
    def Assert_Store_text(self):
        actual = self.driver.find_element(By.XPATH, Locators_Login.STORENAME_XPATH)
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_fill_out_text(self):
        actual = self.driver.find_element(By.XPATH, Locators_Login.FILL_OUT_ERROR)
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_Validation_Error_messages(self,Element):
        text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,Element)))
        assert text.get_attribute("validationMessage") == "Please fill out this field."

    @allure.step
    @allure.description('Clear and insert data to LoginCode input')
    def enter_loginCode(self, LoginCode):
        time.sleep(1)
        loginCode_Input = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators_Login.CODE_INPUT_BOX_XPATH)))
        loginCode_Input.clear()
        loginCode_Input.send_keys(LoginCode)
        Utils(self.driver).assertion(LoginCode, loginCode_Input.get_attribute('value'))
        time.sleep(2)

    @allure.step
    @allure.description('Click login button')
    def click_Login_Button(self):
        self.driver.find_element(By.XPATH, Locators_Login.CONNECT_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click login button')
    def click_LogOut_Button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_LogOut.LOGOUT_TEXT_XPATH).click()
        self.driver.implicitly_wait(20)
        time.sleep(2)

    @allure.step
    @allure.description('Click RememberMe button')
    def click_RememberMe_Button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Login.REMEMBER_ME_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click RememberMe button')
    def Select_trado_store_management(self):
        self.driver.find_element(By.XPATH, Locators_Login.TRADO_STORE_MANAGEMENT_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click RememberMe button')
    def Select_Dani_store_management(self):
        self.driver.find_element(By.XPATH, Locators_Login.DANI_MEMETIKIM_STORE_MANAGEMENT_XPATH).click()
        self.driver.implicitly_wait(20)
