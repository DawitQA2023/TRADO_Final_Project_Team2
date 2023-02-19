import allure
import pytest
from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.loginAdmin_page import Login_Page
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


class Test_LogOut_Chrome(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Logout_admin_Home_website_by_Chrome(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_dashBord()
        assert self.driver.title == "דשבורד - trado"
        login.click_LogOut_Button()


class Test_LogOut_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Login to Admin website using valid data and Firefox')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
    def test_Validate_Logout_admin_Home_website_by_Firefox(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_dashBord()
        assert self.driver.title == "דשבורד - trado"
        login.click_LogOut_Button()


