import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorsQA_Home import Locators_Home
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils


class Home_Page(Locators_Home):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Navigate to Trado logo and click to display Trado QA page')
    def Click_TradoLogo_Button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Home.TRADO_LOGO_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Language_icon and Change language to english')
    def Click_EL_Language_icon(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Home.LANGUAGE_EN_ICON_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to WhatsApp_icon and click to display Trado Support text massage')
    def Click_WhatsApp_icon(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Home.WHATSAPP_ICON_XPATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to WhatsApp_icon and Write text t0 Trado Support')
    def Write_text_to_Trado_Support(self, Message):
        time.sleep(1)
        Message_Input = self.driver.find_element(By.XPATH, Locators_Home.WHATSAPP_TEXT_INPUT_XPATH)
        Message_Input.clear()
        Message_Input.send_keys(Message)
        Utils(self.driver).assertion(Message, Message_Input.get_attribute('value'))

    @allure.step
    @allure.description('Send Message to Trado Support')
    def Click_Send_Button(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Home.SEND_MESSAGE_BUTTON_XPATH).click()
        Utils(self.driver).assertion(Locators_Home.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Check  text message "Please fill out this field." displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text

    @allure.step
    @allure.description('Display next Advertising')
    def Click_Next_Advertising(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        for x in range(0,8):
            self.driver.find_element(By.XPATH, Locators_Home.ADVERT_NEXT_BUTTON_XPATH).click()
            self.driver.implicitly_wait(50)
            self.driver.find_element(By.XPATH, Locators_Home.ADVERT_NEXT_BUTTON_XPATH).click()
            self.driver.find_element(By.XPATH, Locators_Home.ADVERT_PRIVIEW_BUTTON_XPATH).click()
        Utils(self.driver).assertion(Locators_Home.TITLE1, self.driver.title)
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

