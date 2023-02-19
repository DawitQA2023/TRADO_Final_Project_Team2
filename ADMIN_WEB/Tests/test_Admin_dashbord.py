import allure
import pytest
from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.dashbord_page import DashBord_Page
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
class Test_DashBord_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Display Admin Home page using Logo ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_DashBord_Display(self):
        driver = self.driver
        dashBord = DashBord_Page(driver)
        dashBord.click_dashboard_From_sideBar()
        Utils(driver).assertion(self.driver.title, 'דשבורד - trado')


# this is for firefox
@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
class Test_home_Firefox(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_DashBord_Display(self):
        driver = self.driver
        dashBord = DashBord_Page(driver)
        dashBord.click_dashboard_From_sideBar()
        Utils(driver).assertion(self.driver.title, 'דשבורד - trado')
