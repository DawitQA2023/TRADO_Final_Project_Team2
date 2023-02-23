import allure
import pytest
from TRADO.Web.QA_WEB.Pages.loginQA_page import Login_Page
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Base.base_Chrome_QA import Base_Chrome
from TRADO.Server.DataBase.MongoDB import login_code_Generating_query
from TRADO.Web.QA_WEB.Locators.locatorsQA_login import Locators_Login as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


class Test_Valid_Login_Chrome(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Sign up using Valid phone and by using Restaurant and cocktail_field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Validate_SignUp_By_Using_ValidPhone_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Utils(driver).assertion(Login.TITLE1, driver.title)


class Test_Login_using_Cocktail(Base_Chrome):
    @allure.description('Successfully Display Login page using Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_Using_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    @allure.description('Successfully CLOSE Login page By using "X" BUTTON AND using Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_Login_page_Using_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_X_BUTTON()
        Utils(driver).assertion(Login.TITLE1, driver.title)

# by using Cocktail field AND PHONE OPTION
    @allure.description('Successfully Display Login page using cocktail Field and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_Using_Cocktail_field_and_Use_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        assert_text = Login.Assert_Login_page_screen_displayed()
        assert assert_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"  # "Glad you came! Let's create an account"

    @allure.description('Successfully Display Login page using cocktail Field and Person_image link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_Using_Cocktail_field_and_Use_Person_image_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Person_Image_Link()
        assert_text = Login.Assert_Login_page_screen_displayed()
        assert assert_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"  # "Glad you came! Let's create an account"

    @allure.description('Successfully Display Login page using cocktail Field and left open icon arrow link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_Using_Cocktail_field_and_Use_left_open_icon_arrow_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Left_open_icon_arrow()
        assert_text = Login.Assert_Login_page_screen_displayed()
        assert assert_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"  # "Glad you came! Let's create an account"

    @allure.description('Successfully Login using cocktail Field,PHONE and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Valid_Phone_number_and_ID_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        phone = "0147258367"
        Login.Enter_Phone_number(phone)
        Login.Click_Remember_me_box()
        Login.Click_Connect_Button()
        sms = login_code_Generating_query(phone)
        Login.Enter_LoginCode(sms)
        Login.Click_Perform_Verification_Button()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    @allure.description('Successfully Login using cocktail Field,PHONE and Use Person_image link')  # xxxxxxxxxxxxxx
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Valid_Phone_number_and_ID_from_Cocktail_field_by_using_Person_image_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Person_Image_Link()
        Login.Click_Connection_option()
        phone = "0147258367"
        Login.Enter_Phone_number(phone)
        Login.Click_Remember_me_box()
        Login.Click_Connect_Button()
        sms = login_code_Generating_query(phone)
        Login.Enter_LoginCode(sms)
        Login.Click_Perform_Verification_Button()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    @allure.description('Successfully Login using cocktail Field,PHONE and left open icon arrow link')  # xxxxxxxxxxxxxx
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Valid_Phone_number_and_ID_from_Cocktail_field_by_using_left_open_icon_arrow_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Left_open_icon_arrow()
        Login.Click_Connection_option()
        phone = "0147258367"
        Login.Enter_Phone_number(phone)
        Login.Click_Remember_me_box()
        Login.Click_Connect_Button()
        sms = login_code_Generating_query(phone)
        Login.Enter_LoginCode(sms)
        Login.Click_Perform_Verification_Button()
        Utils(driver).assertion(Login.TITLE1, driver.title)

# by using Cocktail field AND Facebook/Google/Twitter OPTION
    @allure.description('Successfully Login using cocktail Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Google_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Google_logo()

    @allure.description('Successfully SignUp using cocktail Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Facebook_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Facebook_logo()

    @allure.description('Successfully Login using cocktail Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Twitter_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Twitter_logo()
# ============================================================================================================================================


class Test_Login_using_Restaurant(Base_Chrome):
    @allure.description('Successfully Display Login page using Restaurant Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_Using_Restaurant_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    @allure.description('Successfully CLOSE Login page By using "X" BUTTON AND using Restaurant Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_Login_page_Using_Restaurant_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_X_BUTTON()
        Utils(driver).assertion(Login.TITLE1, driver.title)
# by using Restaurant field AND PHONE OPTION

# by using Restaurant field AND Facebook/Google/Twitter OPTION

    @allure.description('Successfully Login using Restaurant Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Google_from_Restaurant_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Google_logo()

    @allure.description('Successfully Login using Restaurant Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Facebook_from_Restaurant_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Facebook_logo()

    @allure.description('Successfully Login using Restaurant Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Twitter_from_Restaurant_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Twitter_logo()
# ============================================================================================================================================


class Test_Login_using_Restaurant_and_Cocktail(Base_Chrome):

    @allure.description('Successfully Display Login page using Both Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    @allure.description('Successfully CLOSE Login page By using "X" BUTTON AND using Restaurant_and_Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_Login_page_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_X_BUTTON()
        Utils(driver).assertion(Login.TITLE1, driver.title)
# by using Both field AND PHONE OPTION

# by using both Restaurant & Cocktail field AND Facebook/Google/Twitter OPTION

    @allure.description('Successfully Login using Restaurant Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Google_from_Both_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Google_logo()

    @allure.description('Successfully Login using Restaurant Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Facebook_from_Both_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Facebook_logo()

    @allure.description('Successfully Login using Restaurant Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Twitter_from_Both_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Cocktail_Field()
        Login.Select_Restaurant_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Twitter_logo()
# ============================================================================================================================================


class Test_Login_With_out_Restaurant_and_Cocktail(Base_Chrome):

    @allure.description('Successfully Display Login page not using any Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_Login_page_With_out_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    @allure.description('Successfully CLOSE Login page By using "X" BUTTON AND With_out_Restaurant_and_Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_Login_page_With_out_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Select_Restaurant_Field()
        Login.Select_Cocktail_Field()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_X_BUTTON()
        Utils(driver).assertion(Login.TITLE1, driver.title)

    # by using both Restaurant & Cocktail field AND Facebook/Google/Twitter OPTION

    @allure.description('Successfully Login Successfully Display SignUp page not using any Field Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Google_from_Blank_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Google_logo()

    @allure.description('Successfully Login With_out_Restaurant_and_Cocktail Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Facebook_With_out_Restaurant_and_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Facebook_logo()

    @allure.description('Successfully Login With_out_Restaurant_and_Cocktail Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Login_using_Twitter_With_out_Restaurant_and_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        Login = Login_Page(driver)
        Login.open_Main_page()
        Login.Click_Save_button()
        Login.Click_Hello_Text_Link()
        Login.Click_Connection_option()
        Login.Click_Twitter_logo()
# ============================================================================================================================================


# Compatibility testing using fireFox
# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


class Test_Login_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Login using Valid phone and by using Restaurant and cocktail_field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Validate_Login_By_Using_ValidPhone_Restaurant_and_Cocktail_field2(self):
        driver = self.driver
        Login = Login_Page(driver)
        Utils(driver).assertion(Login.TITLE1, driver.title)


""" Login page GUI """


class Test_Signup_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for login page using cocktail and restaurant')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Login_page_UI_Using_Cocktail_and_Restaurant(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.Select_Cocktail_Field()
        login.Click_Save_button()
        login.Click_Hello_Text_Link()
        font_size = login.Check_font_size(path.Login_CSS)
        assert font_size == "16px"
        font_weight = login.Check_font_weight(path.Login_CSS)
        assert font_weight == "400"
        text_align = login.Check_text_align(path.Login_CSS)
        assert text_align == 'center'

    @pytest.mark.sanity
    @allure.description('Check UI for login page using cocktail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Login_page_UI_Using_Cocktail(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.Select_Cocktail_Field()
        login.Click_Save_button()
        login.Click_Hello_Text_Link()
        font_size = login.Check_font_size(path.Login_CSS)
        assert font_size == "16px"
        font_weight = login.Check_font_weight(path.Login_CSS)
        assert font_weight == "400"
        text_align = login.Check_text_align(path.Login_CSS)
        assert text_align == 'center'

    @pytest.mark.sanity
    @allure.description('Check UI for login page restaurant')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Login_page_UI_Using_Restaurant(self):
        driver = self.driver
        login = Login_Page(driver)
        login.open_Main_page()
        login.Select_Cocktail_Field()
        login.Click_Save_button()
        login.Click_Hello_Text_Link()
        font_size = login.Check_font_size(path.Login_CSS)
        assert font_size == "16px"
        font_weight = login.Check_font_weight(path.Login_CSS)
        assert font_weight == "400"
        text_align = login.Check_text_align(path.Login_CSS)
        assert text_align == 'center'
