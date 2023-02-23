import time

from TRADO.Web.QA_WEB.Locators.locatorsQA_personalArea import Locators_PersonalArea
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils


class PageArea_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Click Personal area')
    def Click_Personal_Area(self):
        time.sleep(2)
        self.driver.implicitly_wait(50)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_PersonalArea.PERSONAL_AREA_BUTTON_XPATH).click()

    @allure.step
    @allure.description('Enter First name')
    def enter_first_name(self, first_name1):
        time.sleep(2)
        utils = Utils(self.driver)
        first_name = self.driver.find_element(By.XPATH, Locators_PersonalArea.FIRSTNAME_XPATH)
        first_name.clear()
        first_name.send_keys(first_name1)
        utils.assertion(first_name1, first_name.get_attribute('value'))

    @allure.step
    @allure.description('Enter Last name')
    def enter_last_name(self, last_name1):
        time.sleep(2)
        utils = Utils(self.driver)
        last_name = self.driver.find_element(By.XPATH, Locators_PersonalArea.LASTNAME_XPATH)
        last_name.clear()
        last_name.send_keys(last_name1)
        utils.assertion(last_name1, last_name.get_attribute('value'))

    @allure.step
    @allure.description('Enter Phone')
    def enter_phone(self, phone1):
        time.sleep(2)
        utils = Utils(self.driver)
        phone = self.driver.find_element(By.XPATH, Locators_PersonalArea.PHONE_XPATH)
        phone.clear()
        phone.send_keys(phone1)
        utils.assertion(phone1, phone.get_attribute('value'))

    @allure.step
    @allure.description('Enter Email')
    def enter_email(self, email1):
        time.sleep(2)
        utils = Utils(self.driver)
        email = self.driver.find_element(By.XPATH, Locators_PersonalArea.EMAIL_XPATH)
        email.clear()
        email.send_keys(email1)
        utils.assertion(email1, email.get_attribute('value'))

    @allure.step
    @allure.description('Enter Id')
    def enter_id(self, id1):
        time.sleep(2)
        utils = Utils(self.driver)
        id_num = self.driver.find_element(By.XPATH, Locators_PersonalArea.ID_XPATH)
        id_num.clear()
        id_num.send_keys(id1)
        utils.assertion(id1, id_num.get_attribute('value'))

    @allure.step
    @allure.description('Enter City')
    def enter_city(self, city1):
        time.sleep(2)
        utils = Utils(self.driver)
        city = self.driver.find_element(By.XPATH, Locators_PersonalArea.CITY_XPATH)
        city.clear()
        city.send_keys(city1)

    @allure.step
    @allure.description('Enter Number')
    def enter_number(self, number1):
        time.sleep(2)
        utils = Utils(self.driver)
        number = self.driver.find_element(By.XPATH, Locators_PersonalArea.NUMBER_XPATH)
        number.clear()
        number.send_keys(number1)
        utils.assertion(number.get_attribute('value'), number1)

    @allure.step
    @allure.description('Click Edit Button')
    def click_Edit_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_PersonalArea.EDIT_BUTTON_XPATH).click()

    @allure.step
    @allure.description('Click Save button')
    def click_Save_button(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_PersonalArea.SAVE_BUTTON_XPATH).click()

    @allure.step
    @allure.description('Check text message displayed')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH, path)
        return actual.text

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



