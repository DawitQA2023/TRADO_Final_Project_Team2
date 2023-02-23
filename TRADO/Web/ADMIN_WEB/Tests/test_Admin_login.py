import allure
import pytest
from TRADO.Web.ADMIN_WEB.Utils.utils_Admin import Utils
from TRADO.Web.ADMIN_WEB.Pages.loginAdmin_page import Login_Page
from TRADO.Web.ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


class Test_Login_Chrome(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Login to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_display_of_Trado_admin_Home_website_by_Chrome_Using_TradoStore(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_dashBord()
        Utils(driver).assertion(self.driver.title, "דשבורד - trado")

    @pytest.mark.sanity
    @allure.description('Successfully Login to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Dani_store')
    def test_Validate_display_of_Trado_admin_Home_website_by_Chrome_Using_daniStore(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_dashBord()
        Utils(driver).assertion(self.driver.title,"דשבורד - trado")

    @pytest.mark.sanity
    @allure.description('Successfully display of Code entering page while using valid phone number')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_UI_PhoneInputPage(self):
        driver = self.driver
        Utils(driver).assertion(self.driver.title,'- trado')


    @pytest.mark.sanity
    @allure.description('Successfully display of Code entering page while using valid phone number')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Trado_Code_input_page_using_valid_Phone_by_Chrome(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_LoginBox()
        login.enter_Phone("1951111111")
        login.click_Send_me_code_Button()
        Utils(driver).assertion(self.driver.title,'- trado')

    @allure.description('Successfully display of Code entering page while using Invalid phone number')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Code_entering_page_while_using_Invalid_phone_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_LoginBox()
        login.enter_Phone('123456789')
        login.click_Send_me_code_Button()
        text = login.Assert_no_such_user_messages()
        Utils(driver).assertion(text, 'no such user')

    @allure.description('Successfully display of Code entering page while using Null phone number')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Code_entering_page_while_using_Null_phone_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_LoginBox()
        login.enter_Phone('')
        login.click_Send_me_code_Button()
        Utils(driver).assertion(self.driver.title, '- trado')

    @pytest.mark.sanity
    @allure.description('Successfully display STORE MANAGEMENT page while using Valid Code number')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Store_management_while_using_Valid_code_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_LoginBox()
        login.enter_Phone("1951111111")
        login.click_Send_me_code_Button()
        login.enter_loginCode("1234")
        login.click_RememberMe_Button()
        login.click_Login_Button()
        text = login.Assert_Store_text()
        Utils(driver).assertion(text, 'Trado\nהרצל 2, רחובות')

    @allure.description('Successfully display STORE MANAGEMENT page while using Invalid Code number')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Store_management_while_using_Invalid_code_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_LoginBox()
        login.enter_Phone("1951111111")
        login.click_Send_me_code_Button()
        login.enter_loginCode("1111")
        login.click_RememberMe_Button()
        login.click_Login_Button()
        text = login.Assert_faild_to_login_messages()
        Utils(driver).assertion(text, "קוד*\nזכור אותי")

    @allure.description('Successfully display STORE MANAGEMENT page while using null Code number')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Store_management_while_using_Null_code_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_LoginBox()
        login.enter_Phone("1951111111")
        login.click_Send_me_code_Button()
        login.enter_loginCode("")
        login.click_RememberMe_Button()
        login.click_Login_Button()
        text = login.Assert_fill_out_text()
        Utils(driver).assertion('נא למלא שדה זהxxx', text)


# *********************************************************************************************************************
# check Compatibility test using FireFox
class Test_Login_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Login to Admin website using valid data and Firefox')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
    def test_Validate_display_of_Trado_admin_Home_website_by_Firefox(self):
        driver = self.driver
        login = Login_Page(driver)
        login.click_dashBord()
        Utils(driver).assertion(self.driver.title, "דשבורד - trado")



