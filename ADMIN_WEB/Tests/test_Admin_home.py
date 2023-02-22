import allure
import pytest
from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.HomeAdmin_page import Home_Page
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


class Test_Home_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Display Admin Home page using Logo ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Display_Admin_Home_page_using_Logo(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_Logo()
        Utils(driver).assertion(self.driver.title, "Dashboard - trado")

    @pytest.mark.sanity
    @allure.description('Successfully change language using language icon')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_change_language_using_language_icon(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_main_dashboard()
        home.click_US_Language_icon()
        Utils(driver).assertion(self.driver.title, 'דשבורד - trado')
        home.click_IL_Language_icon()
        Utils(driver).assertion(self.driver.title, 'Dashboard - trado')

    @pytest.mark.sanity
    @allure.description('Successfully Minimize the side bar while clicking hamburger icon')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Minimize_the_side_bar_while_clicking_hamburger_icon(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_Humburger_icon()
        Utils(driver).assertion(self.driver.title, "דשבורד - trado")

    @pytest.mark.sanity
    @allure.description('Successfully Open Product page from main screen')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Open_Product_page_from_main_screen(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_main_dashboard()
        home.click_US_Language_icon()
        home.click_Product_menu()
        Utils(driver).assertion(self.driver.title, 'Products - trado')

    @pytest.mark.sanity
    @allure.description('Successfully Open user page from main screen')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Open_user_page_from_main_screen(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_main_dashboard()
        home.click_US_Language_icon()
        home.click_User_menu()
        Utils(driver).assertion(self.driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Successfully Open order page from main screen')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Open_order_page_from_main_screen(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_main_dashboard()
        home.click_US_Language_icon()
        home.click_Order_menu()
        Utils(driver).assertion(self.driver.title, 'Orders - trado')


# this is for firefox

class Test_home_Firefox(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
    def test_Validate_change_language_using_language_icon(self):
        driver = self.driver
        home = Home_Page(driver)
        home.click_main_dashboard()
        home.click_US_Language_icon()
        Utils(driver).assertion(self.driver.title, 'Dashboard - trado')

