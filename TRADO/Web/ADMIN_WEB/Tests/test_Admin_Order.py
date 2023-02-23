import allure
import pytest
from TRADO.Web.ADMIN_WEB.Pages.orderAdmin_page import Order_Page
from TRADO.Web.ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.ADMIN_WEB.Locators.locators_Admin_Order import Locators_Order


@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
class Test_User_Chrome(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Click_Ready_Orders_from_Order_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Export_user_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Click_Ready_Orders_from_Order_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Delivery_Orders_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_On_Delivery_Orders_button()
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders__from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_templet_user_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_NEXT_button()
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Phone_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("0545603636")
        assert driver.title == "הזמנות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Last_Name_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("אלהן")
        Text = user.Assert_text(Locators_Order.SEARCH_BY_NAME)
        assert Text == "אלהן"

    @pytest.mark.sanity
    @allure.description('Successfully search')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Price_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("Gush Etzion 45, Beer Sheba")
        Text = user.Assert_text(Locators_Order.SEARCH_BY_Address)
        assert Text == "Gush Etzion 45, Beer Sheba"

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_By_Delivery_Time_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("34 3, city")
        Text = user.Assert_text(Locators_Order.TIME_)
        assert Text == '24/02/23, 03:29'

    @pytest.mark.sanity
    @allure.description('Successfully search')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_PAYMENT_TYPE_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("bankTransfer")
        Text = user.Assert_text(Locators_Order.SEACH_BY_PAYMENT_TYPE)
        assert Text == "bankTransfer"

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_PRODUCTION_DATE_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("b2b")
        Text = user.Assert_text(Locators_Order.SEARCH_BY_PAYMENT_DATE)
        assert Text == 'bankTransfer'

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_ADDRESS_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("פתח תקווה 10, נתניה")
        Text = user.Assert_text(Locators_Order.SEARCH_BY_ADDRESS)
        assert Text == 'Gush Etzion 45, Beer Sheba'

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Search_Order_ORDER_NUMBER_to_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.Click_SearchBox("177")
        Text = user.Assert_text(Locators_Order.SEARCH_BY_ADDRESS)
        assert Text == 'Gush Etzion 45, Beer Sheba'

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME1_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = user.Assert_text(Locators_Order.READY_PRODUCTS_NAME1)
        assert Text != "dddddsa"

    @pytest.mark.sanity
    @allure.description('Successfully search ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME2_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = user.Assert_text(Locators_Order.READY_PRODUCTS_NAME2)
        assert Text != "אלי "

    @pytest.mark.sanity
    @allure.description('Successfully search')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME3_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = user.Assert_text(Locators_Order.READY_PRODUCTS_NAME3)
        assert Text != "ישראל"

    @pytest.mark.sanity
    @allure.description('Successfully search')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Ready_Orders_Clicking_Ready_NAME4_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Ready_Orders_button()
        Text = user.Assert_text(Locators_Order.READY_PRODUCTS_NAME4)
        assert Text == '0501234567'

    @pytest.mark.sanity
    @allure.description('Successfully Finished Orders Address from admin ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address1__from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        Text = user.Assert_text(Locators_Order.FINISHED_ORDERS_ADDRESS1)
        assert Text == 'החלוצים 3, אשדוד'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address2__from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        user.click_FINISHED_ORDER_button()
        Text = user.Assert_text(Locators_Order.FINISHED_ORDERS_ADDRESS1)
        assert Text == 'החלוצים 3, אשדוד'

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Finished_Orders_Address2_Name1_from_admin(self):
        driver = self.driver
        user = Order_Page(driver)
        user.click_User_Menu_Option()
        user.click_Finished_Orders_button()
        user.click_FINISHED_ORDER_button()
        Text = user.Assert_text(Locators_Order.FINISHED_ORDERS_ADDRESS2_NAME1)
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
        Text = user.Assert_text(Locators_Order.FINISHED_ORDERS_ADDRESS2_NAME2)
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
        Text = user.Assert_text(Locators_Order.ON_DELIVERY_NAME1)
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
        Text = user.Assert_text(Locators_Order.ON_DELIVERY_NAME2)
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
        Text = user.Assert_text(Locators_Order.READY_ORDERS_NAME1)
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
        Text = user.Assert_text(Locators_Order.READY_ORDERS_NAME2)
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
        Text = user.Assert_text(Locators_Order.READY_ORDERS_NAME3)
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
        Text = user.Assert_text(Locators_Order._ORDERS_NAME_)
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
        Text = user.Assert_text(Locators_Order._ORDERS_NAME_)
        assert Text == ''

