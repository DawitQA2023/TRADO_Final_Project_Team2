import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait



class Product_assertion_functions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_Title_text(self):
        actual = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div/h4/span")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_name_error(self):
        actual = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[4]/div")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_barcode_error(self):
        actual = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Please fill out this field." displayed')
    def Assert_price_error(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[7]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_first_page(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_product_info_page(self):
        actual = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div["
                                                    "3]/div[1]/div[3]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_store_id_page(self):
        actual = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div["
                                                    "5]/div[1]/span[1]/div[2]/div/div[4]")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_section_id_page(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Catagories." displayed')
    def Assert_NULL_page(self):
        actual = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div["
                                                    "2]/div[1]/span[1]/div[2]/div/div[2]")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_unit_page(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[3]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Catagories." displayed')
    def Assert_unitIncarton(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Catagories." displayed')
    def Assert_min_order(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Catagories." displayed')
    def Assert_amount_carton(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_delivery_carton(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_delivery_city_carton(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_delivery_street_carton(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_delivery_null_carton(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_search_valid_products(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_languageUS_(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_languageIL_(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_backTitle_(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/span/form/div[2]/div[4]/label")
        return actual.text

    @allure.step
    @allure.description('Check the alert text message "Categories." displayed')
    def Assert_importTitle_(self):
        actual = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[4]/div/div/div/form/div[1]/div/label")
        return actual.text
