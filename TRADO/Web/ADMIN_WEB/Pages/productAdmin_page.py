import allure
import time
from TRADO.Web.ADMIN_WEB.Locators.locators_Admin_Product import Locators_Admin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TRADO.Web.ADMIN_WEB.Utils.utils_Admin import Utils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Product_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Navigate to Login page and click "PRODUCT" moduls')
    def click_on_product_sidebar(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCTS_XPAT).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(50)

    @allure.step
    @allure.description('Click the product and click on "KEBAR" options')
    def click_kebab_buttons(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.KEBAB_ICON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('From the product moduls  "PLUS PRODUCT" files to .Database...')
    def click_plusProduct_buttons(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PLUS_ADD_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click  "language US" files to .Database...')
    def click_languageUS_buttons(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.LANGUAGE_US_PRODUCT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click  "language US" files to .Database...')
    def click_languageIL_buttons(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.LANGUAGE_IL_PRODUCT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click the back button ..')
    def click_back_button(self):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators_Admin.BACK_BUTTON).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    #  ------------------------------------------  product pages -------------------------------------------
    @allure.step
    @allure.description('Enter the "BARCODE".for products..')
    def enter_barcode_fields(self, Barcode):
        time.sleep(2)
        Barcode_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators_Admin.PRODUCT_BARCODE_XPATH)))
        Barcode_input.clear()
        Barcode_input.send_keys(Barcode)
        Utils(self.driver).assertion(Barcode, Barcode_input.get_attribute('value'))

    @allure.step
    @allure.description('Enter the Product in the  "SEARCH" box.for products..')
    def enter_search_box(self, search):
        time.sleep(2)
        Search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.PRODUCT_SEARCH_BOX)))
        Search_input.clear()
        Search_input.send_keys(search)
        Utils(self.driver).assertion(search, Search_input.get_attribute('value'))

    @allure.step
    @allure.description('Enter the "PRICE".for products..')
    def enter_price_fields(self, Price):
        time.sleep(2)
        Price_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.PRICE_PRODUC_XPATH)))
        Price_input.clear()
        Price_input.send_keys(Price)
        Utils(self.driver).assertion(Price, Price_input.get_attribute('value'))

    @allure.step
    @allure.description('Enter the "NAME".for products..')
    def enter_name_fields(self, Name):
        time.sleep(2)
        Name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.NAME_PRODUCT_XPATH)))
        Name_input.clear()
        Name_input.send_keys(Name)
        Utils(self.driver).assertion(Name, Name_input.get_attribute('value'))

    @allure.step
    @allure.description('Click the next button products...')
    def click_next_product_buttons(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCT_NEXT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    # ---------------------------------------- second product info page -----------------------------------------
    @allure.step
    @allure.description('Click the drop down section button....')
    def click_drope_down_section_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.SECTION_ID_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Select products section categories')
    def select_sections_from_given(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.NURIT_CATAGORIES_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click the section in in store fields')
    def click_department_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.DEPARTMENT_ID_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click the section in in product tag fields')
    def click_drope_down_productTag_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCT_TAG_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Select products tag in given categories')
    def select_product_tag_given(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCT_TAG_NURIT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click the section in in store fields')
    def click_drope_down_store_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCT_STOREID_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Select products store categories')
    def select_store_from_given(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRO_STORE_VALUE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click the next button to...')
    def click_next_productInfo_buttons(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCT_INFO_NEXT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    # ------------------------------------product unit pages ----------------------------------------------------
    @allure.step
    @allure.description('Enter the "Amount".for products..in the unit pages')
    def enter_amount_fields(self, Amount):
        time.sleep(1)
        Amount_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.AMOUNT_PRODUCT_XPATH)))
        Amount_input.clear()
        Amount_input.send_keys(Amount)
        Utils(self.driver).assertion(Amount, Amount_input.get_attribute('value'))

    @allure.step
    @allure.description('Enter the "unit in carton".for products..in the unit pages')
    def enter_unitCarton_fields(self, unit_inCarton):
        time.sleep(1)
        unit_inCarton_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.UNIT_IN_CARTON_XPATH)))
        unit_inCarton_input.clear()
        unit_inCarton_input.send_keys(unit_inCarton)
        Utils(self.driver).assertion(unit_inCarton, unit_inCarton_input.get_attribute('value'))

    @allure.step
    @allure.description('Enter the "minimum ordered".for products..in the unit pages')
    def enter_minOrder_fields(self, min_order):
        time.sleep(1)
        min_order_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.MIN_ORDER_XPATH)))
        min_order_input.clear()
        min_order_input.send_keys(min_order)
        Utils(self.driver).assertion(min_order, min_order_input.get_attribute('value'))

    @allure.step
    @allure.description('Click the next button to...')
    def click_next_productUnit_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.UNITS_NEXT_BUUTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    # ----------------------------------------- Delivery product page ------------------------------------
    @allure.step
    @allure.description('Enter the "CITY".for products.Delivery page.')
    def enter_city_fields(self, city):
        time.sleep(1)
        City_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.DELIVERY_CITY_XPATH)))
        City_input.clear()
        City_input.send_keys(city)

    @allure.step
    @allure.description('Enter the "STREET".for products M..Delivery pages.')
    def enter_street_fields(self, street):
        time.sleep(1)
        Street_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_Admin.DELIVERY_STREET_XPATH)))
        Street_input.clear()
        Street_input.send_keys(street)

    @allure.step
    @allure.description('Click the next products  to...')
    def click_next_product_Delivery_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.DELIVERY_NEXT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click the end button to. finsh the process..')
    def click_end_process_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.END_PROCESS_NEXT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click on "DROP ICON" Product page')
    def click_drop_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.DROP_ICON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click on "DROP ICON" Product page')
    def click_list_number(self):
        self.driver.find_element(By.XPATH, Locators_Admin.AMOUNTS_PRODUCT_INLIST_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click on "PAGE2" Product page')
    def click_page3_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.PEODUCT_PAGE3_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click on "EXPORT" Product page')
    def click_Export_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.PORDUCT_EXPORT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click on "ADD BY BRANDS" Product page')
    def click_IMPORT_buttons(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_Admin.PRODUCT_IMPORT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Check the alert text')
    def Assert_text(self, path):
        actual = self.driver.find_element(By.XPATH,path)
        return actual.text
