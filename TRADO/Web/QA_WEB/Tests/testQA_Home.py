import allure
import pytest
from TRADO.Web.QA_WEB.Pages.homeQA_page import Home_Page
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Locators.locatorsQA_Home import Locators_Home as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Home_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE_1(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change language to english to hebrew')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_Language_change_1(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_EL_Language_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_display_Whatsapp_Trado_Support_1(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and close using WhatsApp icon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Close_Whatsapp_Trado_Support_1(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and send message')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Send_message_to_support_using_Whatsapp_Trado_Support_1(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Write_text_to_Trado_Support("test qa trado send support")
        home.Click_Send_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change advertisement')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Change_of_advertisement_1(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_Next_Advertising()
        Utils(driver).assertion("trado", self.driver.title)


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Home_Chrome2(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE_2(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change language to english to hebrew')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_Language_change_2(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_EL_Language_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_display_Whatsapp_Trado_Support_2(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and close using WhatsApp icon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Close_Whatsapp_Trado_Support_2(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and send message')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Send_message_to_support_using_Whatsapp_Trado_Support_2(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Write_text_to_Trado_Support("test qa trado send support")
        home.Click_Send_Button()
        Utils(driver).assertion("trado", self.driver.title)


@pytest.mark.usefixtures('WithOut_login_selectField_none')
class Test_Home_Chrome3(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE_3(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change language to english to hebrew')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_Language_change_3(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_EL_Language_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_display_Whatsapp_Trado_Support_3(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and close using WhatsApp icon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Close_Whatsapp_Trado_Support_3(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and send message')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Send_message_to_support_using_Whatsapp_Trado_Support_3(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Write_text_to_Trado_Support("test qa trado send support")
        home.Click_Send_Button()
        Utils(driver).assertion("trado", self.driver.title)


# Compatibility testing using fireFox

# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('WithOut_login_selectField_none')
class Test_Home_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and send message')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Send_message_to_support_using_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Write_text_to_Trado_Support("test qa trado send support")
        home.Click_Send_Button()
        Utils(driver).assertion("trado", self.driver.title)


""" Home page GUI """


class Test_Home_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for Home page using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Home_UI_Using_Home(self):
        driver = self.driver
        home = Home_Page(driver)
        font_size = home.Check_font_size(path.HOME_CSS)
        assert font_size == "16px"
        font_weight = home.Check_font_weight(path.HOME_CSS)
        assert font_weight == "400"
        text_align = home.Check_text_align(path.HOME_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Home page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Home_UI_Using_Home2(self):
        driver = self.driver
        home = Home_Page(driver)
        font_size = home.Check_font_size(path.HOME_CSS)
        assert font_size == "16px"
        font_weight = home.Check_font_weight(path.HOME_CSS)
        assert font_weight == "400"
        text_align = home.Check_text_align(path.HOME_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Home page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant')
    def test_Home_UI_Using_Home3(self):
        driver = self.driver
        home = Home_Page(driver)
        font_size = home.Check_font_size(path.HOME_CSS)
        assert font_size == "16px"
        font_weight = home.Check_font_weight(path.HOME_CSS)
        assert font_weight == "400"
        text_align = home.Check_text_align(path.HOME_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Home page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_cocktails')
    def test_Home_UI_Using_Home4(self):
        driver = self.driver
        home = Home_Page(driver)
        font_size = home.Check_font_size(path.HOME_CSS)
        assert font_size == "16px"
        font_weight = home.Check_font_weight(path.HOME_CSS)
        assert font_weight == "400"
        text_align = home.Check_text_align(path.HOME_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Home page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_none')
    def test_Home_UI_Using_Home4(self):
        driver = self.driver
        home = Home_Page(driver)
        font_size = home.Check_font_size(path.HOME_CSS)
        assert font_size == "16px"
        font_weight = home.Check_font_weight(path.HOME_CSS)
        assert font_weight == "400"
        text_align = home.Check_text_align(path.HOME_CSS)
        assert text_align == 'start'
