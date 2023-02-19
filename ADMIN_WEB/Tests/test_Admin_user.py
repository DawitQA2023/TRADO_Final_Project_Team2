import allure
import pytest
from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.userAdmin_page import User_Page
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


class Test_User_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Export_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_import_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Import_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_templet_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Tampet_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Add_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Add_button()
        user.enter_FirstName("aaaaa")
        user.enter_LastName("ssdfghhh")




# this is for firefox

class Test_User_Firefox(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
    def test_Validate_Export_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")
