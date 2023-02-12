import time

import allure
import pytest
from ADMIN.Utils.utils import Utils
from ADMIN.Base.base_test import Base_Page
from ADMIN.Pages.login_page import Login_Page


class Test_Login(Base_Page):

    @allure.description('Successfully Display Login page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Trado_admin_website_login_page(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_Language_option()
        time.sleep(2)

    @allure.description('Successfully display code entering page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Code_entering_page_while_using_valid_phone_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_LoginBox()
        login.enter_Phone('1951111111')
        login.click_Send_me_code_Button()
        Utils(driver).assertion(login.title1, self.driver.title)

    @allure.description('Successfully display code entering page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Code_entering_page_while_using_Blank_phone_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_LoginBox()
        login.enter_Phone('')
        login.click_Send_me_code_Button()
        Utils(driver).assertion(login.title1, self.driver.title)

    @allure.description('Successfully display code entering page')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_display_of_Code_entering_page_while_using_Invalid_phone_number(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.click_LoginBox()
        login.enter_Phone('123456789')
        login.click_Send_me_code_Button()
        login.Assert_no_such_user_messages()
        time.sleep(5)
        time.sleep(5)