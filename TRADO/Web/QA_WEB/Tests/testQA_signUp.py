import allure
import pytest
import random
from TRADO.Web.QA_WEB.Pages.signUpQA_page import SignUp_Page
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Base.base_Chrome_QA import Base_Chrome
from TRADO.Server.DataBase.MongoDB import login_code_Generating_query
from TRADO.Web.QA_WEB.Locators.locatorsQA_signUp import Locators_SignUp as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_Signup import Pre_Requirement_SignUp_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_Signup import Pre_Requirement_SignUp_Firefox

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_SignUp_With_login_Code')
class Test_Signup(Pre_Requirement_SignUp_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Sign up using Valid phone and by using Restaurant and cocktail_field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_By_Using_ValidPhone_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        Utils(driver).assertion(signup.TITLE1, self.driver.title)


class Test_SignUp_using_Cocktail(Base_Chrome):
    @allure.description('Successfully Display SignUp page using Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_Using_Cocktail_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    @allure.description('Successfully CLOSE SignUp page By using "X" BUTTON AND using Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_SignUp_page_Using_Cocktail_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_X_BUTTON()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    # by using Cocktail field AND PHONE OPTION
    @allure.description('Successfully Display SignUp page using cocktail Field and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_Using_Cocktail_field_and_Use_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        assert_text = signUp.Assert_SignUp_page_screen_displayed()
        assert assert_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"  # "Glad you came! Let's create an account"

    @allure.description('Successfully Display SignUp page using cocktail Field and Person_image link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_Using_Cocktail_field_and_Use_Person_image_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Person_Image_Link()
        assert_text = signUp.Assert_SignUp_page_screen_displayed()
        assert assert_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"  # "Glad you came! Let's create an account"

    @allure.description('Successfully Display SignUp page using cocktail Field and left open icon arrow link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_Using_Cocktail_field_and_Use_left_open_icon_arrow_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Left_open_icon_arrow()
        assert_text = signUp.Assert_SignUp_page_screen_displayed()
        assert assert_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"  # "Glad you came! Let's create an account"

    @allure.description('Successfully SignUp using cocktail Field,PHONE and Use Hello Text link')  # xxxxxxxxxxxxxx
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Valid_Phone_number_and_ID_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        Phone_generate = random.randint(1000000000, 10000000000)  # this number need to be chage every time
        PhoneNum = Phone_generate
        signUp.Enter_Phone_number(PhoneNum)
        signUp.Enter_BN_number("2222222222")
        signUp.Click_Agree_terms_box()
        signUp.Click_Connect_Button()
        sms = login_code_Generating_query(PhoneNum)
        signUp.Enter_LoginCode(sms)
        signUp.Click_Perform_Verification_Button()
        Utils(driver).assertion(signUp.TITLE1, driver.title)

    @allure.description('Successfully SignUp using cocktail Field,PHONE and Use Person_image link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Valid_Phone_number_and_ID_from_Cocktail_field_by_using_Person_image_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Person_Image_Link()
        signUp.Click_Registration_option()
        Phone_generate = random.randint(1000000000, 10000000000)  # this number need to be chage every time
        PhoneNum = Phone_generate
        signUp.Enter_Phone_number(PhoneNum)
        signUp.Enter_BN_number("0123456789")
        signUp.Click_Agree_terms_box()
        signUp.Click_Connect_Button()
        sms = login_code_Generating_query(PhoneNum)
        signUp.Enter_LoginCode(sms)
        signUp.Click_Perform_Verification_Button()
        Utils(driver).assertion(signUp.TITLE1, driver.title)

    @allure.description(
        'Successfully SignUp using cocktail Field,PHONE and left open icon arrow link')  # xxxxxxxxxxxxxx
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Valid_Phone_number_and_ID_from_Cocktail_field_by_using_left_open_icon_arrow_link(
            self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Left_open_icon_arrow()
        signUp.Click_Registration_option()
        Phone_generate = random.randint(1000000000, 10000000000)  # this number need to be chage every time
        PhoneNum = Phone_generate
        signUp.Enter_Phone_number(PhoneNum)
        signUp.Enter_BN_number("0123456789")
        signUp.Click_Agree_terms_box()
        signUp.Click_Connect_Button()
        sms = login_code_Generating_query(PhoneNum)
        signUp.Enter_LoginCode(sms)
        signUp.Click_Perform_Verification_Button()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    # by using Cocktail field AND Facebook/Google/Twitter OPTION
    @allure.description('Successfully SignUp using cocktail Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Google_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Google_logo()

    @allure.description('Successfully SignUp using cocktail Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Facebook_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Facebook_logo()

    @allure.description('Successfully SignUp using cocktail Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Twitter_from_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Twitter_logo()


# ============================================================================================================================================


class Test_SignUp_using_Restaurant(Base_Chrome):
    @allure.description('Successfully Display SignUp page using Restaurant Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_Using_Restaurant_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    @allure.description('Successfully CLOSE SignUp page By using "X" BUTTON AND using Restaurant Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_SignUp_page_Using_Restaurant_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_X_BUTTON()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    # by using Restaurant field AND PHONE OPTION

    # by using Restaurant field AND Facebook/Google/Twitter OPTION

    @allure.description('Successfully SignUp using Restaurant Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Google_from_Restaurant_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Google_logo()

    @allure.description('Successfully SignUp using Restaurant Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Facebook_from_Restaurant_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Facebook_logo()

    @allure.description('Successfully SignUp using Restaurant Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Twitter_from_Restaurant_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Twitter_logo()


# ============================================================================================================================================


class Test_SignUp_using_Restaurant_and_Cocktail(Base_Chrome):

    @allure.description('Successfully Display SignUp page using Both Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    @allure.description('Successfully CLOSE SignUp page By using "X" BUTTON AND using Restaurant_and_Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_SignUp_page_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_X_BUTTON()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    # by using Both field AND PHONE OPTION

    # by using both Restaurant & Cocktail field AND Facebook/Google/Twitter OPTION

    @allure.description('Successfully SignUp using Restaurant Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Google_from_Both_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Google_logo()

    @allure.description('Successfully SignUp using Restaurant Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Facebook_from_Both_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Facebook_logo()

    @allure.description('Successfully SignUp using Restaurant Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Twitter_from_Both_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Select_Restaurant_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Twitter_logo()


# ============================================================================================================================================


class Test_SignUp_With_out_Restaurant_and_Cocktail(Base_Chrome):

    @allure.description('Successfully Display SignUp page not using any Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_navigating_to_SignUp_page_With_out_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    @allure.description('Successfully CLOSE SignUp page By using "X" BUTTON AND With_out_Restaurant_and_Cocktail Field')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Close_to_SignUp_page_With_out_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Restaurant_Field()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_X_BUTTON()
        Utils(driver).assertion(signUp.TITLE1, self.driver.title)

    # by using Both field AND PHONE OPTION

    # by using both Restaurant & Cocktail field AND Facebook/Google/Twitter OPTION

    @allure.description(
        'Successfully SignUp Successfully Display SignUp page not using any Field Field,Google LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Google_from_Blank_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Google_logo()

    @allure.description(
        'Successfully SignUp With_out_Restaurant_and_Cocktail Field,FACEBOOK LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Facebook_With_out_Restaurant_and_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Facebook_logo()

    @allure.description(
        'Successfully SignUp With_out_Restaurant_and_Cocktail Field,Twitter LOGO and Use Hello Text link')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_SignUp_using_Twitter_With_out_Restaurant_and_Cocktail_field_by_using_Hello_Text_link(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        signUp.Click_Registration_option()
        signUp.Click_Twitter_logo()


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_SignUp_With_login_Code')
class Test_Signup_Firefox(Pre_Requirement_SignUp_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Sign up using Valid phone and by using Restaurant and cocktail_field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_SignUp_By_Using_ValidPhone_Restaurant_and_Cocktail_field1(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        Utils(driver).assertion(signup.TITLE1, self.driver.title)


""" SignUp page GUI """


class Test_Signup_GUI(Pre_Requirement_SignUp_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for sign up page using cocktail and restaurant')
    @allure.severity(allure.severity_level.NORMAL)
    def test_SignUp_page_UI_Using_Cocktail_and_Restaurant(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        font_size = signUp.Check_font_size(path.SIGNUP_CSS)
        assert font_size == "16px"
        font_weight = signUp.Check_font_weight(path.SIGNUP_CSS)
        assert font_weight == "400"
        text_align = signUp.Check_text_align(path.SIGNUP_CSS)
        assert text_align == 'start'


    @pytest.mark.sanity
    @allure.description('Check UI for sign up page using cocktail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_SignUp_page_UI_Using_Cocktail(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        font_size = signUp.Check_font_size(path.SIGNUP_CSS)
        assert font_size == "16px"
        font_weight = signUp.Check_font_weight(path.SIGNUP_CSS)
        assert font_weight == "400"
        text_align = signUp.Check_text_align(path.SIGNUP_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for sign up page restaurant')
    @allure.severity(allure.severity_level.NORMAL)
    def test_SignUp_page_UI_Using_Restaurant(self):
        driver = self.driver
        signUp = SignUp_Page(driver)
        signUp.open_Main_page()
        signUp.Select_Cocktail_Field()
        signUp.Click_Save_button()
        signUp.Click_Hello_Text_Link()
        font_size = signUp.Check_font_size(path.SIGNUP_CSS)
        assert font_size == "16px"
        font_weight = signUp.Check_font_weight(path.SIGNUP_CSS)
        assert font_weight == "400"
        text_align = signUp.Check_text_align(path.SIGNUP_CSS)
        assert text_align == 'start'
