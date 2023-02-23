import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.ADMIN_WEB.Locators.locators_Admin_Order import Locators_Order


class Order_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Click Order Menu Option ')
    def click_User_Menu_Option(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH,Locators_Order.ORDER_MENU_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Kabab button ')
    def click_Kebab_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Order.KEBAB_XPATH).click()
        self.driver.implicitly_wait(20)


    @allure.step
    @allure.description('Click Export button ')
    def click_Export_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Order.EXPORT_BUTTON_XPATH).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Ready_Orders button ')
    def click_Ready_Orders_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Order.ORDER).click()
        self.driver.implicitly_wait(20)
    @allure.step
    @allure.description('Click Finished_Orders button ')
    def click_Finished_Orders_button(self):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.find_element(By.XPATH, Locators_Order.FINISH_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click Delivery_Orders ')
    def click_On_Delivery_Orders_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.DELIVERY_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_NEXT_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.NEXT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_FINISHED_ORDER_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.FINISHED_ORDERS_ADDRESS2).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_FINISHED_NAME2_CLICK_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.FINISHED_ORDERS_ADDRESS2_NAME2_CLICK).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_ON_Delivery_NAME1_CLICK_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.ON_DELIVERY_NAME1_CLICK).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)


    @allure.step
    @allure.description('Click NEXT_button ')
    def click_ON_Delivery_NAME1_CLICK1_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.ON_DELIVERY_NAME1_CLICK1).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_READY_ORDERS_NAME1_CLICK1_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.READY_ORDERS_NAME1_CLICK1).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_READY_ORDERS_NAME1_CLICK2_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.READY_ORDERS_NAME1_CLICK2).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_PHONE_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.CLICK_PRODUCT).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click NEXT_button ')
    def click_READY_ORDERS_NAME1_CLICK3_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.READY_ORDERS_NAME1_CLICK3).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)


    @allure.step
    @allure.description('Click _AMOUNT_Orders')
    def click_PRODUCT_Orders_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Order.PRODUCT_X).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Navigate to Search box and click Box ')
    def Click_SearchBox(self, value):
        time.sleep(2)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        value_input = self.driver.find_element(By.XPATH, Locators_Order.SEARCH_XPATH)
        value_input.clear()
        value_input.send_keys(value)
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Check the text')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH,path)
        return actual.text