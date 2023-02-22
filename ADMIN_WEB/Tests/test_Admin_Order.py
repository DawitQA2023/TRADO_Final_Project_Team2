import allure
import pytest
from selenium.webdriver.common.by import By

from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.order_Admin_page  import Order_Page
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox
from ADMIN_WEB.Locators.locators_Admin_Order import Locators_Order

@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
class Test_User_Chrome(Pre_Requirement_Login_Chrome):


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Click_Ready_Orders_from_Order_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        assert self.driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Export_user_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        assert self.driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Click_Ready_Orders_from_Order_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        assert self.driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Delivery_Orders_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_On_Delivery_Orders_button()
        assert self.driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders__from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        assert self.driver.title == "הזמנות - trado"

    # @pytest.mark.sanity
    # @allure.description('Successfully ')
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_AMOUNT_Orders_from_admin(self):
    #     driver = self.driver
    #     user = Order_Page(driver)
    #     user.click_User_Menu_Option()
    #     user.click_AMOUNT_Orders_button()
    #     assert self.driver.title == "הזמנות - trado"


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_templet_user_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_NEXT_button()
        assert self.driver.title == "הזמנות - trado"


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Phone_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("0545603636")
        assert self.driver.title == "הזמנות - trado"


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Last_Name_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("אלהן")
        Text =driver.find_element(By.XPATH,Locators_Order.SEARCH_BY_NAME).text
        assert Text == "אלהן"


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Price_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("Gush Etzion 45, Beer Sheba")
        Text =driver.find_element(By.XPATH, Locators_Order.SEARCH_BY_Address).text
        assert Text != "Gush Etzion 45, Beer Sheba"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Delivery_Time_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("34 3, city")
        Text =driver.find_element(By.XPATH, Locators_Order.SEARCH_BY_DELIVERY_Status).text
        assert Text == "34 3, city"
    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_PAYMENT_TYPE_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("bankTransfer")
        Text =driver.find_element(By.XPATH,Locators_Order.SEACH_BY_PAYMENT_TYPE).text
        assert Text == "bankTransfer"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_PRODUCTION_DATE_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("b2b")
        Text =driver.find_element(By.XPATH, Locators_Order.SEARCH_BY_PAYMENT_DATE).text
        assert Text == "b2b"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_ADDRESS_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("פתח תקווה 10, נתניה")
        Text =driver.find_element(By.XPATH,Locators_Order.SEARCH_BY_ADDRESS).text
        assert Text != "פתח תקווה 10, נתניה"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_ORDER_NUMBER_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("177")
        Text =driver.find_element(By.XPATH,Locators_Order.SEARCH_BY_NUMBER).text
        assert Text != "177"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME1_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = driver.find_element(By.XPATH, Locators_Order.READY_PRODUCTS_NAME1).text
        assert Text != "dddddsa"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME2_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = driver.find_element(By.XPATH, Locators_Order.READY_PRODUCTS_NAME2).text
        assert Text != "אלי "

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME3_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = driver.find_element(By.XPATH, Locators_Order.READY_PRODUCTS_NAME3).text
        assert Text != "ישראל"


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME4_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = driver.find_element(By.XPATH, Locators_Order.READY_PRODUCTS_NAME4).text
        assert Text == 'Robert'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address1__from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        Text = driver.find_element(By.XPATH, Locators_Order.FINISHED_ORDERS_ADDRESS1).text
        assert Text == 'Gush Etzion 45, Beer Sheba'


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address2__from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        user.click_FINISHED_ORDER_button()
        Text = driver.find_element(By.XPATH, Locators_Order.FINISHED_ORDERS_ADDRESS2_NAME).text
        assert Text != 'האש פלאנט (Hashplant)'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address2_Name1_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        user.click_FINISHED_ORDER_button()
        Text = driver.find_element(By.XPATH, Locators_Order.FINISHED_ORDERS_ADDRESS2_NAME1).text
        assert Text != 'OG Kush'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address2_Name3_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        user.click_FINISHED_NAME2_CLICK_button()
        Text = driver.find_element(By.XPATH, Locators_Order.FINISHED_ORDERS_ADDRESS2_NAME2).text
        assert Text != 'מעבד מזון ובלנדר Ninja דגם BN800'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_ON_Delivery_NAME1_CLICK1_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_On_Delivery_Orders_button()
        user.click_ON_Delivery_NAME1_CLICK_button()
        Text = driver.find_element(By.XPATH, Locators_Order.ON_DELIVERY_NAME1).text
        assert Text != 'בדיקה 2'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_ON_Delivery_NAME1_CLICK2_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_On_Delivery_Orders_button()
        user.click_ON_Delivery_NAME1_CLICK1_button()
        Text = driver.find_element(By.XPATH, Locators_Order.ON_DELIVERY_NAME2).text
        assert Text != 'נוטלה'


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ON_Delivery_NAME1_CLICK3_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        user.click_READY_ORDERS_NAME1_CLICK1_button()
        Text = driver.find_element(By.XPATH, Locators_Order.READY_ORDERS_NAME1).text
        assert Text != 'קויארר'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ON_Delivery_NAME1_CLICK3_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        user.click_READY_ORDERS_NAME1_CLICK2_button()
        Text = driver.find_element(By.XPATH, Locators_Order.READY_ORDERS_NAME2).text
        assert Text != 'קויארר'


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ON_Delivery_NAME1_CLICK4_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        user.click_READY_ORDERS_NAME1_CLICK3_button()

        Text = driver.find_element(By.XPATH, Locators_Order.READY_ORDERS_NAME3).text
        assert Text != 'קויארר'


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ON_Delivery_NAME1_CLICK4_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        user.click_READY_ORDERS_NAME1_CLICK3_button()
        Text = driver.find_element(By.XPATH, Locators_Order._ORDERS_NAME_).text
        assert Text == 'שמן למון קוש'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ON_Delivery_NAME1_CLICK4_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        user.click_PRODUCT_Orders_button()
        Text = driver.find_element(By.XPATH, Locators_Order._ORDERS_NAME_).text
        assert Text == ''