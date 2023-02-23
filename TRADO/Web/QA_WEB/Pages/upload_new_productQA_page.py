import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TRADO.Web.QA_WEB.Locators.locatorsQA_upload_product import Locators_Upload_New_Product


class Upload_New_Product_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.Add_Button = Locators_Upload_New_Product.ADD_NEW_PRODUCT_BUTTON
        self.Inputs = Locators_Upload_New_Product.NEW_PRODUCT_FIELDS
        self.Add_Product = Locators_Upload_New_Product.ADD_NEW_PRODUCT_SECTION
        self.No_Store_Error_Message = Locators_Upload_New_Product.STORE_VALIDATION_FAILED
        self.All_field_Error_message = Locators_Upload_New_Product.FILL_THE_FIELD
        self.Add_new_ProductPage = Locators_Upload_New_Product.ADD_PRODUCT_PAGE

    @allure.step
    @allure.description('click_add_new_product_section')
    def click_add_new_product_section(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.Add_Product)))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Add_Product)))
        self.driver.find_element(By.CSS_SELECTOR, self.Add_Product).click()
        div = self.driver.find_element(By.CSS_SELECTOR, self.Add_new_ProductPage)
        wait.until(EC.visibility_of(div))

    @allure.step
    @allure.description("inputs_fields")
    def inputs_fields(self):
        time.sleep(1)
        utils = Utils(self.driver)
        fields = self.driver.find_elements(By.CSS_SELECTOR, self.Inputs)
        utils.assertion(len(fields), 8)
        return fields

    @allure.step
    @allure.description("click_add_new_product_button")
    def click_add_new_product_button(self):
        time.sleep(1)
        utils = Utils(self.driver)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.Add_Button)))
        button = self.driver.find_element(By.CSS_SELECTOR, self.Add_Button)
        utils.assertion(button.get_attribute('defaultValue'), 'הוספה')
        button.click()

    @allure.step
    @allure.description("enter_data_to_inputs")
    def enter_all_inputs_filed(self, data: list):
        WebDriverWait(self.driver, 20)
        utils = Utils(self.driver)
        fields = self.inputs_fields()
        if len(fields) and len(data) == 8:
            for field in range(len(fields)):
                fields[field].clear()
                fields[field].send_keys(data[field])
                utils.assertion(fields[field].get_attribute('value'), data[field])
        else:
            raise ValueError

    """ Error Messages display """

    @allure.step
    @allure.description("messages for all the fields")
    def messages_for_all_the_fields(self, num):
        fields = self.inputs_fields()
        return fields[num].get_attribute('validationMessage')

    @allure.step
    @allure.description("store validation failed message")
    def store_validation_failed_message(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.No_Store_Error_Message)))
        return self.driver.find_element(By.CSS_SELECTOR, self.No_Store_Error_Message).get_attribute('innerText')

    @allure.step
    @allure.description("enter the field message")
    def enter_the_field_message(self, num):
        messages = self.driver.find_elements(By.XPATH, self.All_field_Error_message)
        return messages[num].get_attribute('innerText')

    @allure.step
    @allure.description("")
    def js_email_msg_point(self, text):
        for letter in range(len(text)):
            if text[letter] == '@':
                new = text[letter + 1:]
                return new

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


class Upload_Product_with_Store:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # self.fieldErr  # Error Message for all The Fields
        self.uploadImage = Locators_Upload_New_Product.IMAGE  # Image(need to be with OS)
        self.fillingCheckBox = Locators_Upload_New_Product.CHECKBOX  # Filling The CheckBox
        self.unitsOrWeight = Locators_Upload_New_Product.UNIT_AND_WEIGHT  # Filtering for Upload Product
        self.plusButton = Locators_Upload_New_Product.PLUS_BUTTON  # Click Plus For Business Days
        self.minusButton = Locators_Upload_New_Product.MINUS_BUTTON  # Click Minus For Business Days
        self.amountOfDays = Locators_Upload_New_Product.AMOUNT_OF_DAYS  # The Total Of Business Days
        self.fieldMessages = Locators_Upload_New_Product.ERROR_FIELD_IS_EMPTY

    @allure.step
    @allure.description("")
    def click_add_new_product_section(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 20)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Locators_Upload_New_Product.ADD_NEW_PRODUCT_SECTION)))
        self.driver.find_element(By.CSS_SELECTOR, Locators_Upload_New_Product.ADD_NEW_PRODUCT_SECTION).click()
        div = self.driver.find_element(By.CSS_SELECTOR, Locators_Upload_New_Product.ADD_PRODUCT_PAGE)
        wait.until(EC.visibility_of(div))

    @allure.step
    @allure.description("")
    def inputs_fields(self, length: int):
        time.sleep(1)
        utils = Utils(self.driver)
        fields = self.driver.find_elements(By.XPATH, Locators_Upload_New_Product.NEW_PRODUCT_FIELDS)  # ----------
        utils.assertion(len(fields), length)
        return fields

    @allure.step
    @allure.description("")
    def click_add_new_product_button(self):
        time.sleep(1)
        utils = Utils(self.driver)
        wait = WebDriverWait(self.driver, 20)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Locators_Upload_New_Product.ADD_NEW_PRODUCT_BUTTON)))
        button = self.driver.find_element(By.CSS_SELECTOR, Locators_Upload_New_Product.ADD_NEW_PRODUCT_BUTTON)
        utils.assertion(button.get_attribute('defaultValue'), 'הוספה')
        button.click()

    @allure.step
    @allure.description("")
    def enter_all_inputs_filed(self, length: int, data: list):
        utils = Utils(self.driver)
        fields = self.inputs_fields(length)
        if len(fields) and len(data) == length:
            for field in range(len(fields)):
                fields[field].clear()
                fields[field].send_keys(data[field])
                utils.assertion(fields[field].get_attribute('value'), data[field])
        else:
            raise ValueError

    @allure.step
    @allure.description("")
    def click_on_upload_image(self, path):
        time.sleep(1)
        image = self.driver.find_element(By.XPATH, self.uploadImage)
        image.send_keys(path)

    @allure.step
    @allure.description("")
    def fill_checkbox(self):
        utils = Utils(self.driver)
        checkbox = self.driver.find_element(By.XPATH, self.fillingCheckBox)
        checkbox.click()
        utils.assertion(checkbox.is_selected(), True)

    @allure.step
    @allure.description("")
    def filter_products(self, choice: int):
        utils = Utils(self.driver)
        div = self.driver.find_elements(By.XPATH, self.unitsOrWeight)
        if choice == 0:
            utils.assertion(div[choice].get_attribute('textContent'), 'יחידות')
            div[choice].click()
        elif choice == 1:
            utils.assertion(div[choice].get_attribute('textContent'), 'משקל')
            div[choice].click()
        else:
            raise ValueError

    @allure.step
    @allure.description("")
    def click_plus_button(self, num):
        for i in range(num):
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.element_to_be_clickable((By.XPATH, self.plusButton)))
            button = self.driver.find_element(By.XPATH, self.plusButton)
            button.click()

    @allure.step
    @allure.description("")
    def click_minus_button(self, num):
        for i in range(num):
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.element_to_be_clickable((By.XPATH, self.minusButton)))
            button = self.driver.find_element(By.XPATH, self.minusButton)
            button.click()

    @allure.step
    @allure.description("")
    def amount_of_days(self):
        return self.driver.find_element(By.XPATH, self.amountOfDays).get_attribute('valueAsNumber')

    '''Error Messages display'''

    @allure.step
    @allure.description("")
    def js_messages_for_all_the_fields(self, length, num):
        fields = self.inputs_fields(length)
        return fields[num].get_attribute('validationMessage')

    @allure.step
    @allure.description("")
    def upload_prod_successfully(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators_Upload_New_Product.STORE_VALIDATION_FAILED)))
        return self.driver.find_element(By.CSS_SELECTOR,
                                        Locators_Upload_New_Product.STORE_VALIDATION_FAILED).get_attribute(
            'textContent')

    @allure.step
    @allure.description("")
    def error_message(self, num):
        messages = self.driver.find_elements(By.CSS_SELECTOR, self.fieldMessages)
        return messages[num].get_attribute('innerText')

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
