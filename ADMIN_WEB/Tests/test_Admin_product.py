import allure
import pytest
from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Base.base_Chrome_Admin import Base_Chrome
from ADMIN_WEB.Pages.productAdmin_page import Product_Page
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


class Test_product_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_x()








class Test_product_Firefox(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_x()
