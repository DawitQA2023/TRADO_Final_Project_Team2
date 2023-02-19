import time

import allure
import pytest
from TRADO.QA_WEB.Pages.sideBarQA_page import SideBar_Page
from TRADO.QA_WEB.Utils.utils_QA import Utils
from TRADO.QA_WEB.Locators.locatorsQA_Sidebar import Locators_SideBar
from TRADO.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Sidebar_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        time.sleep(2)
        text = side.Assert_text(Locators_SideBar.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Contact page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(Locators_SideBar.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Shipment Method page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipment_Method_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(Locators_SideBar.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Sidebar_Chrome2(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        time.sleep(2)
        text = side.Assert_text(Locators_SideBar.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Contact page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(Locators_SideBar.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Shipment Method page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipment_Method_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(Locators_SideBar.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)


@pytest.mark.usefixtures('WithOut_login_selectField_none')
class Test_Sidebar_Chrome2(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        time.sleep(2)
        text = side.Assert_text(Locators_SideBar.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Contact page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(Locators_SideBar.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Shipment Method page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipment_Method_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(Locators_SideBar.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)



