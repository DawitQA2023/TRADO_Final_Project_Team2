import time
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.QA_WEB.Locators.locatoreQA_products import Locators_Products


class Product_page(Locators_Products):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step
    @allure.description('Click drink product catagories')
    def Click_drink_link(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.DRINK_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click snack product catagories')
    def Click_snack_link(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.SNACK_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click snack product catagories')
    def Click_cannabis_link(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.CANABIES_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click + sign to increase and add to cart')
    def Click_plus_button(self, num):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        for x in range(0, int(num)):
            self.driver.find_element(By.XPATH, self.INCRAES_QUAN).click()
            self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click - sign to increase and add to cart')
    def Click_minus_button(self, num):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        for x in range(0, int(num)):
            self.driver.find_element(By.XPATH, self.INCRAES_QUAN).click()
            self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, self.DECRAES_QUAN).click()

    @allure.step
    @allure.description('Click delete icon button to delete product from cart')
    def Click_Delete_product_from_Cart_by_delete_icon(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.DELETE_BUTTON).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click delete link button to delete the product from cart')
    def Click_Delete_product_from_Cart_by_delete_link(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.DELETE_LINK).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click payment button to complete purchase')
    def Click_payment_button(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.PAYMENT_BUTTON).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "GORILLA PRODUCT" in the promotion categories')
    def Click_gorila_product(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.GORILA_GLUE_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "CLICK PROMOTION" in the promotion categories')
    def Click_promotion_categories(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Products.PROMOTION_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "GOAT PRODUCT" in the cannabis categories')
    def Click_goat_product(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.wait.until(EC.url_to_be(self.driver.current_url))
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Products.GOAT_SNACK).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "GOAT mMILK PRODUCT" in the cannabis categories')
    def Click_goat_milk_product(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.GOAT_MILK).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "GORILLA GLUE PRODUCT" in the cannabis categories')
    def Click_Gorilla_glue_product(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.GORILA_GLUE).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "FORMAT CHANGE1" to change the format of products')
    def Click_format_chang1(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.FORMAT_CHANGE1_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "FORMAT CHANGE2" to change the format of products')
    def Click_format_chang2(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.FORMAT_CHANGE2_XPATH).click()
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "FORMAT CHANGE1" to change the format of products')
    def Click_format_chang1(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.FORMAT_CHANGE1_XPATH).click()
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "FORMAT CHANGE1" to change the format of products')
    def click_all_products_and_add_cart(self, num):
        NUMS = 0
        for num in range(0, num):
            self.driver.execute_script("window.scrollBy(0, 200);")
            self.driver.implicitly_wait(5)
            time.sleep(2)
            self.driver.find_element(By.XPATH,
                                     f"/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[{NUMS + 1}]/div/div[2]").click()
            self.driver.find_element(By.XPATH,Locators_Products.ALL_XPATH).click()
            time.sleep(2)
            self.driver.back()
            NUMS += 1

    @allure.step
    @allure.description('Click "POPULARITY" to select products products')
    def Click_popularity(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.POPULARITY_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "POPULARITY" to select products products')
    def Click_lowest_price(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.FROM_LOWEST_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "POPULARITY" to select products products')
    def Click_highest_price(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.FROM_HIGHEST_XPATH).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click "SORTING" to select products products')
    def Click_sorting(self):
        time.sleep(1)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Products.POPULARITY_XPATH).click()
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Check  text message "Please fill out this field." displayed')
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


