import time

import allure
import pytest
from TRADO.Web.QA_WEB.Pages.sideBarQA_page import SideBar_Page
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Locators.locatorsQA_Sidebar import Locators_SideBar as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Sidebar_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        text = side.Assert_text(path.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Contact page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(path.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Shipment Method page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipment_Method_page(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(path.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Sidebar_Chrome2(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page_(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        time.sleep(2)
        text = side.Assert_text(path.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Contact page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_page_(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(path.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Shipment Method page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipment_Method_page_(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(path.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)


@pytest.mark.usefixtures('WithOut_login_selectField_none')
class Test_Sidebar_Chrome3(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page_1(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        time.sleep(2)
        text = side.Assert_text(path.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Contact page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_page_1(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(path.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)

    @pytest.mark.sanity
    @allure.description('Validates moving to "Shipment Method page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipment_Method_page_1(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_ContactUs_sidebar_link()
        text = side.Assert_text(path.CONTACT_PAGE_PATH)
        Utils(driver).assertion('נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.', text)


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Sidebar_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Validates moving to "common question page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_common_question_page_(self):
        driver = self.driver
        side = SideBar_Page(driver)
        side.Click_Common_Question_sidebar_link()
        text = side.Assert_text(path.ANY_QUESTION_TEXT)
        Utils(driver).assertion("יש לכם שאלות ?\nהגעתם למקום הנכון", text)



""" Home page GUI """


class Test_sideBar_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for sideBar page using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_sideBar_UI_Using_Login(self):
        driver = self.driver
        sideBar = SideBar_Page(driver)
        font_size = sideBar.Check_font_size(path.SIDEBAR_CSS)
        assert font_size == "16px"
        font_weight = sideBar.Check_font_weight(path.SIDEBAR_CSS)
        assert font_weight == "400"
        text_align = sideBar.Check_text_align(path.SIDEBAR_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for sideBar page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Home_UI_Using_Using_without_Login01(self):
        driver = self.driver
        sideBar = SideBar_Page(driver)
        font_size = sideBar.Check_font_size(path.SIDEBAR_CSS)
        assert font_size == "16px"
        font_weight = sideBar.Check_font_weight(path.SIDEBAR_CSS)
        assert font_weight == "400"
        text_align = sideBar.Check_text_align(path.SIDEBAR_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for sideBar page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant')
    def test_Home_UI_Using_without_Login02(self):
        driver = self.driver
        sideBar = SideBar_Page(driver)
        font_size = sideBar.Check_font_size(path.SIDEBAR_CSS)
        assert font_size == "16px"
        font_weight = sideBar.Check_font_weight(path.SIDEBAR_CSS)
        assert font_weight == "400"
        text_align = sideBar.Check_text_align(path.SIDEBAR_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for sideBar page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_cocktails')
    def test_Home_UI_Using_without_Login03(self):
        driver = self.driver
        sideBar = SideBar_Page(driver)
        font_size = sideBar.Check_font_size(path.SIDEBAR_CSS)
        assert font_size == "16px"
        font_weight = sideBar.Check_font_weight(path.SIDEBAR_CSS)
        assert font_weight == "400"
        text_align = sideBar.Check_text_align(path.SIDEBAR_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for sideBar page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_none')
    def test_Home_UI_Using_without_Login04(self):
        driver = self.driver
        sideBar = SideBar_Page(driver)
        font_size = sideBar.Check_font_size(path.SIDEBAR_CSS)
        assert font_size == "16px"
        font_weight = sideBar.Check_font_weight(path.SIDEBAR_CSS)
        assert font_weight == "400"
        text_align = sideBar.Check_text_align(path.SIDEBAR_CSS)
        assert text_align == 'start'
