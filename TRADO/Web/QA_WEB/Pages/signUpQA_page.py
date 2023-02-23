import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorsQA_signUp import Locators_SignUp
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Locators.Pre_Requiremen_Locators.Pre_Requirement_Locators import Pre_Requirement_Locators


class SignUp_Page(Locators_SignUp):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Navigate to Main page ')
    def open_Main_page(self):
        super().__init__()

    @allure.step
    @allure.description('Navigate to Field Of Interest page and select Cocktail Field Of Interest From The List')
    def Select_Cocktail_Field(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SignUp.COCKTAIL_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Field Of Interest page and select Restaurant Field Of Interest From The List')
    def Select_Restaurant_Field(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SignUp.RESTAURANT_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Field Of Interest page and Not select any Field Of Interest From The List')
    def Click_Save_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_SignUp.SAVE_BUTTON_XPATH).click()
        Utils(self.driver).assertion(Locators_SignUp.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to SignUp page from Personal area text link')
    def Click_Personal_area_Text_Link(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.PERSONAL_AREA_TEXT_LINK_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to SignUp page from Hello Guest text link')
    def Click_Hello_Text_Link(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.HELLO_GUEST_TEXT_LINK_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to SignUp page from Person Image link')
    def Click_Person_Image_Link(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.PERSON_IMAGE_LINK_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to SignUp page from left open icon arrow link')
    def Click_Left_open_icon_arrow(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.LEFT_OPEN_ICON_ARROW_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Verify if signup page display')
    def Assert_SignUp_page_screen_displayed(self):
        text = self.driver.find_element(By.XPATH, Locators_SignUp.SCREEN_TEXT_XPATH).text
        return text

    @allure.step
    @allure.description('Select registration option')
    def Click_Registration_option(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.REGISTRATION_OPTION_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click on Agree to the terms')
    def Click_Agree_terms_box(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.AGREE_TERM_BOX_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert data to UserName input')
    def Enter_Phone_number(self, PhoneNumber):
        UserName_Input = self.driver.find_element(By.XPATH, Locators_SignUp.PHONE_BOX_XPATH)
        UserName_Input.clear()
        UserName_Input.send_keys(PhoneNumber)
        # Utils(self.driver).assertion(PhoneNumber, UserName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to UserName input')
    def Enter_BN_number(self, BnNumber):
        UserName_Input = self.driver.find_element(By.XPATH, Locators_SignUp.BN_NUMBER_XPATH)
        UserName_Input.clear()
        UserName_Input.send_keys(BnNumber)
        Utils(self.driver).assertion(BnNumber, UserName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click Connect button')
    def Click_Connect_Button(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.CONNECT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Verify if signup page display')
    def Assert_LoginCode_screen_displayed(self):
        text = self.driver.find_element(By.XPATH, Locators_SignUp.LOGINCODE_SCREEN_TEXT_XPATH).text
        return text

    @allure.step
    @allure.description('Click form_loginCode input box')
    def Click_loginCode_Box(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.LOGIN_CODE_INPUT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Clear and insert data to LoginCode input')
    def Enter_LoginCode(self,sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, Pre_Requirement_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.assertion(place.get_attribute('value'), digit)

    @allure.step
    @allure.description('Click Perform verification button ')
    def Click_Perform_Verification_Button(self):
        self.driver.find_element(By.XPATH, Locators_SignUp.PERFORM_VERIFICATION_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click Facebook Logo')
    def Click_Facebook_logo(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_SignUp.FACEBOOK_LOGO_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click Twitter Logo')
    def Click_Twitter_logo(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_SignUp.TWITTER_LOGO_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click GOOGLE Logo')
    def Click_Google_logo(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_SignUp.GOOGLE_LOGO_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click X BUTTON')
    def Click_X_BUTTON(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_SignUp.X_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)
        time.sleep(2)

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
