from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from ADMIN.Locators.locators_Login import Locators_Login
from ADMIN.Utils.utils import Utils


class Login_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.title1 = Locators_Login.TITLE1
        self.title2 = Locators_Login.TITLE2
        self.error_fillText = Locators_Login.ERROR_TEXT
        self.language = Locators_Login.LANGUAGE_XPATH
        self.phoneBox = Locators_Login.PHONEBOX_XPATH
        self.sendCode_button = Locators_Login.SEND_ME_CODE_BUTTON_XPATH

    @allure.step
    @allure.description('Navigate to Main Home page')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to Login page and click language option')
    def click_Language_option(self):
        self.driver.find_element(By.XPATH, self.language).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title1, self.driver.title)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Navigate to Login page and click Phone entering box')
    def click_LoginBox(self):
        self.driver.find_element(By.XPATH, self.phoneBox).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        Utils(self.driver).assertion(self.title1, self.driver.title)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to Phone input')
    def enter_Phone(self, Phone):
        UserName_Input = self.driver.find_element(By.XPATH, self.phoneBox)
        UserName_Input.clear()
        UserName_Input.send_keys(Phone)
        Utils(self.driver).assertion(Phone, UserName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click signUp button to register on the website')
    def click_Send_me_code_Button(self):
        self.driver.find_element(By.XPATH, self.sendCode_button).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_no_such_user_messages(self):
        text = self.driver.find_element(By.XPATH, Locators_Login.NO_SUCH_USER_TEXT).text
        print(text)


    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_Validation_Error_messages(self,Element):
        text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,Element)))
        assert text.get_attribute("validationMessage") == "Please fill out this field."

