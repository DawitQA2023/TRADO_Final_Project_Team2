import allure
import pytest
from TRADO.QA_WEB.Pages.footerQA_page import Fotter_Page
from TRADO.QA_WEB.Utils.utils_QA import Utils
from TRADO.QA_WEB.Locators.locatorsQA_Footer import Locators_Footer
from TRADO.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Footer_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Open Facebook page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_facebook_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Facebook_link()
        Utils(driver).assertion("Facebook – log in or sign up", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Instagram Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Instagram_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Instagram_link()
        Utils(driver).assertion("Instagram", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Twitter Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Twitter_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Twitter_link()
        Utils(driver).assertion("טוויטר \ גילוי", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Question Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Question_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Question_link()
        text = fotter.Assert_text(Locators_Footer.ANY_QUESTION_TEXT)
        Utils(driver).assertion(text, "יש לכם שאלות ?\nהגעתם למקום הנכון")

    @pytest.mark.sanity
    @allure.description('Successfully open shipping Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipping_Method_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Shipment_link()
        text = fotter.Assert_text(Locators_Footer.SHIPMENT_TEXT)
        Utils(driver).assertion(text, 'שיטת השילוח שלנו נורא פשוטה.')

    @pytest.mark.sanity
    @allure.description('Successfully open Payment Solution Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Payment_Method_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Shipment_link()
        text = fotter.Assert_text(Locators_Footer.PAYMENT_SOLUTIONS_LINK_PATH)
        Utils(driver).assertion(text, 'פתרונות תשלום')

    @pytest.mark.sanity
    @allure.description('Successfully open Max Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Max_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Max_link()
        text = fotter.Assert_text(Locators_Footer.PAYMENT_SOLUTIONS_LINK_PATH)
        Utils(driver).assertion(text, 'פתרונות תשלום')

    @pytest.mark.sanity
    @allure.description('Successfully open Who we are Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Who_we_are_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Who_We_are_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.WHO_WE_ARE_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Account Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Account_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_My_Account_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.ACCOUNT_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Etrado Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Etrado_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Etrado_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.ETRADO_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Contact Us Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_Us_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Contact_Us_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.CONTACT_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Business_interface Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Business_interface_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Business_interface_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.CONTACT_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Accessibility statement page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Accessibility_statement_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Accessibility_statement_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.ACCESSIBILITY_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Privacy policy Page')  # ????????????????????????
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Privacy_policy_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Privacy_policy_link()
        text = fotter.Assert_text(Locators_Footer.PRIVACY_POLICY_LINK_PATH)
        Utils(driver).assertion("מדיניות פרטיות", text)

    @pytest.mark.sanity
    @allure.description('Successfully open Read and agree term page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Read_and_agree_term_page(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Read_agree_term_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.AGREE_TERM_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open TRADO production Home Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_TRADO_production_Home_Page_from_Who_we_are_page_by_treadingAreaButton(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Who_We_are_link()
        fotter.Click_To_treading_area_button()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.TRADO_PRODUCTION_URL)


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Footer_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Open Facebook page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_facebook_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Facebook_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Instagram Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Instagram_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Instagram_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Twitter Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Twitter_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Twitter_link()
        Utils(driver).assertion('trado', self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Open Question Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Question_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Question_link()
        text = fotter.Assert_text(Locators_Footer.ANY_QUESTION_TEXT)
        Utils(driver).assertion(text, "יש לכם שאלות ?\nהגעתם למקום הנכון")

    @pytest.mark.sanity
    @allure.description('Successfully open shipping Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Shipping_Method_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Shipment_link()
        text = fotter.Assert_text(Locators_Footer.SHIPMENT_TEXT)
        Utils(driver).assertion(text, 'שיטת השילוח שלנו נורא פשוטה.')

    @pytest.mark.sanity
    @allure.description('Successfully open Payment Solution Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Payment_Method_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Shipment_link()
        text = fotter.Assert_text(Locators_Footer.PAYMENT_SOLUTIONS_LINK_PATH)
        Utils(driver).assertion(text, 'פתרונות תשלום')

    @pytest.mark.sanity
    @allure.description('Successfully open Max Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Max_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Max_link()
        text = fotter.Assert_text(Locators_Footer.PAYMENT_SOLUTIONS_LINK_PATH)
        Utils(driver).assertion(text, 'פתרונות תשלום')

    @pytest.mark.sanity
    @allure.description('Successfully open Who we are Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Who_we_are_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Who_We_are_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.WHO_WE_ARE_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Account Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Account_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_My_Account_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.ACCOUNT_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Etrado Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Etrado_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Etrado_link()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.ETRADO_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open Contact Us Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Contact_Us_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Contact_Us_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully open Business_interface Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Business_interface_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Business_interface_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully open Accessibility statement page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Accessibility_statement_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Accessibility_statement_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully open Privacy policy Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Privacy_policy_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Privacy_policy_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully open Read and agree term page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_Read_and_agree_term_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Read_agree_term_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully open TRADO production Home Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_TRADO_production_Home_Page_from_Who_we_are_page_by_treadingAreaButton_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Who_We_are_link()
        fotter.Click_To_treading_area_button()
        Utils(driver).assertion(fotter.driver.current_url, Locators_Footer.TRADO_PRODUCTION_URL)

    @pytest.mark.sanity
    @allure.description('Successfully open TRADO production Home Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_TRADO_production_Home_Page_from_Who_we_are_page_BY_NewOrder_button_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Who_We_are_link()
        Utils(driver).assertion("trado", self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully open TRADO production Home Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_TRADO_production_Home_Page_from_Who_we_are_page_BY_NewOrder_button_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Who_We_are_link()
        Utils(driver).assertion("trado", self.driver.title)


# Compatibility testing using fireFox

# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Footer_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Open Facebook page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Display_facebook_page_(self):
        driver = self.driver
        fotter = Fotter_Page(driver)
        fotter.Click_Facebook_link()
        Utils(driver).assertion("Facebook – log in or sign up", self.driver.title)
