import allure
import pytest
from QA_WEB.Pages.contact_usQA_page import ContactUS_Page
from QA_WEB.Locators.locatorQA_Contact_Us import *
from QA_WEB.Utils.utils_QA import Utils
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Contact_us_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Open Contact_us PAGE')
    @allure.severity(allure.severity_level.NORMAL)
    def test_display_Contact_us_PAGE(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        text = contact.Assert_text(Locators_Contact_Us.CONTACT_TITLE)
        Utils(driver).assertion("נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.", text)

    @pytest.mark.sanity
    @allure.description('Check contact us using full information ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Full_Information(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.SUCCESS_TEXT)
        Utils(driver).assertion(text, 'הפרטים נקלטו בהצלחה')


    @pytest.mark.sanity
    @allure.description('Send with out filling the detail filed ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_send_with_out_filling_all_details(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName('')
        contact.Insert_Email('')
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_FirstName(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us FirstName using letter and numbers')
    @allure.severity(allure.severity_level.NORMAL)
    def test_FirstName_using_letter_and_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('wesa12345')
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check to contact us  FirstName using only numbers')
    @allure.severity(allure.severity_level.NORMAL)
    def test_FirstName_using_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('12345')
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    # ------------------------------------------------------------------------------------
    @pytest.mark.sanity
    @allure.description('Check contact us without LastName')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_LastName(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName('')
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us LastName using letters and numbers')
    @allure.severity(allure.severity_level.NORMAL)
    def test_LastName_using_letter_and_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName('bo123')
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check contact us LastName using only numbers')
    @allure.severity(allure.severity_level.NORMAL)
    def test_LastName_using_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName('234123')
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check contact us without Email')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_Email(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email('')
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without .com in Email')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_com_in_Email(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email('omi@gmail')
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check contact us in email field letter and number')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Email_using_letter_and_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email('omi123')
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check contact us in email field using number')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Email_using_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email('123123')
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check contact us without Phone Number')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_Phone_Number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check Using letter and number in Phone Number field')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Phone_Number_Using_letter_and_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number('ame23456')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text, "מס׳ טלפון לא תקין")

    @pytest.mark.sanity
    @allure.description('Check Using letter in Phone Number field')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Phone_Number_Using_letter(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number('ametabe')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text, "מס׳ טלפון לא תקין")

    @pytest.mark.sanity
    @allure.description('Check contact us without Content Referral')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_Content_Referral(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without Content Referral')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Content_Referral_using_number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral('45321342')
        contact.Click_Send_Button()

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName and LastName')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_FirstName_and_LastName(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName('')
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName and Email')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_FirstName_and_Email(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName("boboye")
        contact.Insert_Email('')
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without LastName and Email')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_LastName_and_Email(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName()
        contact.Insert_Email()
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName, LastName and Email ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_FirstName_LastName_and_Email(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName()
        contact.Insert_LastName()
        contact.Insert_Email()
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text2, "נא למלא שדה זה")
        text3 = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text3, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName and Phone Number ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_FirstName_and_Phone_Number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName and Phone Number ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_LastName_and_Phone_Number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName('')
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without Email and Phone Number ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_Email_and_Phone_Number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email('')
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName, LastName,Email and Phone Number ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Without_FirstName_LastName_Email_and_Phone_Number(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button('')
        contact.Insert_FirstName('')
        contact.Insert_LastName('')
        contact.Insert_Email('')
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text2, "נא למלא שדה זה")
        text3 = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text3, "נא למלא שדה זה")
        text4 = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text4, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without FirstName and contentReferral ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_without_FirstName_and_contentReferral(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without LastName and contentReferral ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_without_LastName_and_contentReferral(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName('')
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without Email and contentReferral ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_without_Email_and_contentReferral(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email('')
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without Email and contentReferral ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_without_PhoneNumber_and_contentReferral(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text2 = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text2, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without contentReferral ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_without_contentReferral(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Check contact us without full Information ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_without_Information(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName('')
        contact.Insert_LastName('')
        contact.Insert_Email('')
        contact.Insert_Phone_number('')
        contact.Insert_Content_Referral('')
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.ERROR_FIRST_NAME)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        text1 = contact.Assert_text(Locators_Contact_Us.ERROR_LAST_NAME)
        Utils(driver).assertion(text1, "נא למלא שדה זה")
        text3 = contact.Assert_text(Locators_Contact_Us.ERROR_EMAIL)
        Utils(driver).assertion(text3, "נא למלא שדה זה")
        text4 = contact.Assert_text(Locators_Contact_Us.ERROR_PHONE)
        Utils(driver).assertion(text4, "נא למלא שדה זה")
        text5 = contact.Assert_text(Locators_Contact_Us.ERROR_CONTACT_REFERRAL)
        Utils(driver).assertion(text5, "נא למלא שדה זה")


# ---------------------------------------------------------------------------------------------------------------

@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Contact_us_Chrome2(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully Open Contact_us PAGE with out login')
    @allure.severity(allure.severity_level.NORMAL)
    def test_display_Contact_us_PAGE_with_out_login(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        text = contact.Assert_text(Locators_Contact_Us.CONTACT_TITLE)
        Utils(driver).assertion("נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה.", text)

    @pytest.mark.sanity
    @allure.description('Check contact us using full information ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Full_Information_with_out_login(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.SUCCESS_TEXT)
        Utils(driver).assertion(text, 'הפרטים נקלטו בהצלחה')


# ---------------------------------------------------------------------------------------------------------------

@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Contact_us_Firefox1(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Check contact us full information ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Contact_us_Full_Information_Firefox(self):
        driver = self.driver
        contact = ContactUS_Page(driver)
        contact.Click_Contact_Button()
        contact.Insert_FirstName("wesagn")
        contact.Insert_LastName("boboye")
        contact.Insert_Email("omi@gmail.com")
        contact.Insert_Phone_number("0564781524")
        contact.Insert_Content_Referral("Never give up any one")
        contact.Click_Send_Button()
        text = contact.Assert_text(Locators_Contact_Us.SUCCESS_TEXT)
        Utils(driver).assertion(text, 'הפרטים נקלטו בהצלחה')
