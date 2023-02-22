import allure
import pytest
from QA_WEB.Pages.homeQA_page import Home_Page
from QA_WEB.Utils.utils_QA import Utils
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Home_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change language to english to hebrew')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_Language_change(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_EL_Language_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_display_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and close using WhatsApp icon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Close_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Click_WhatsApp_icon()
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


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Home_Chrome2(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change language to english to hebrew')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_Language_change(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_EL_Language_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_display_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and close using WhatsApp icon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Close_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Click_WhatsApp_icon()
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

@pytest.mark.usefixtures('WithOut_login_selectField_none')
class Test_Home_Chrome3(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Open trado QA PAGE')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_logo_display_trado_QA_PAGE(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_TradoLogo_Button()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Change language to english to hebrew')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Trado_Language_change(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_EL_Language_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_display_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Whatsapp Trado Support and close using WhatsApp icon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Close_Whatsapp_Trado_Support(self):
        driver = self.driver
        home = Home_Page(driver)
        home.Click_WhatsApp_icon()
        home.Click_WhatsApp_icon()
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

# Compatibility testing using fireFox


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