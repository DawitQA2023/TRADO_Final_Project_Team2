import time

from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatorsQA_Footer import Locators_Footer
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils



class Fotter_Page(Locators_Footer):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Navigate to Facebook footer link and click and display facebook page')
    def Click_Facebook_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.FACEBOOK_LINK_PATH).click()
        Utils(self.driver).assertion(Locators_Footer.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Instagram footer link and click and display facebook page')
    def Click_Instagram_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.INSTAGRAM_LINK_PATH).click()
        Utils(self.driver).assertion(Locators_Footer.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Twitter footer link and click and display facebook page')
    def Click_Twitter_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.TWITTER_LINK_PATH).click()
        Utils(self.driver).assertion(Locators_Footer.TITLE1, self.driver.title)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Common questions footer link and click and display facebook page')
    def Click_Question_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.QUESTION_PAGE_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Shipment footer link and click and display facebook page')
    def Click_Shipment_link(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.SHIPMENT_PAGE_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Shipment footer link and click and display facebook page')
    def Click_Payment_Solution_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.PAYMENT_SOLUTIONS_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Shipment footer link and click and display facebook page')
    def Click_Max_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.MAX_PAGE_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Who we are footer link and click and display facebook page')
    def Click_Who_We_are_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.WHO_WE_ARE_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to My account footer link and click and display facebook page')
    def Click_My_Account_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.MY_ACCOUNT_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to eTrado footer link and click and display facebook page')
    def Click_Etrado_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.ETRADO_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Contact Us footer link and click and display facebook page')
    def Click_Contact_Us_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.CONTACT_US_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Business interface footer link and click and display facebook page')
    def Click_Business_interface_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.BUSINESS_INTERFACE_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Accessibility_statement footer link and display Accessibility statement page')
    def Click_Accessibility_statement_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.ACCESSIBILITY_STATEMENT_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to PRIVACY POLICY footer link and display PRIVACY POLICY page')
    def Click_Privacy_policy_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.PRIVACY_POLICY_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Read agree term footer link and display Term page')
    def Click_Read_agree_term_link(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.READ_AND_AGREE_TO_THE_TERMS_LINK_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Check  text message Displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text

    # Who we are page

    @allure.step
    @allure.description('Navigate to Business interface footer link and click and display QA-Trado page')
    def Click_To_treading_area_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.TO_TREADING_AREA_PATH).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Business interface footer link and click New order button and display QA-Trado page')
    def Click_To_NewOrder_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.NEW_ORDER_BTN).click()
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Navigate to Business interface footer link and click Contact button and display contact page page')
    def Click_Contact_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Footer.CONTACT_BTN).click()
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
