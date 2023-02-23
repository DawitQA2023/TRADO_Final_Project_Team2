import time
import allure
import pytest
from TRADO.Web.QA_WEB.Pages.businessInterfaceQA_page import Business_Interface_Page
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Locators.locatorsQA_Business_interface import Locators_BusinessInterface as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class TestQA_Business_Interface_Chrome1(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully open Business interface')
    @allure.severity(allure.severity_level.NORMAL)
    def test_display_Business_Interface_PAGE(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        Utils(driver).assertion('trado', join.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Join using Valid input in all detail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_all_valid_detail(self): # ?????????????
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.APPROVE_ERROR_XPATH)
        Utils(driver).assertion(text, 'Please Approve Our Policy')

    @pytest.mark.sanity
    @allure.description('Successfully Join using Valid input in all detail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_all_All_null_details(self): # ?????????????????????????????
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Click_send_button()
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_FIRSTNAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        time.sleep(2)

    @pytest.mark.sanity
    @allure.description('Successfully Join using null first name input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_firstName(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_FIRSTNAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null last name input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_LastName(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_LASTNAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null BnNumber input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_BnNumber(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_BNNUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using letter BnNumber input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Letter_BnNumber(self):  # ???????????????????????????????
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('abcd')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_BNNUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null BusinessName input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_BusinessName(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_BUSNIESS_NAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Phone number input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_PhoneNuber(self):  #  ??????????????????????????????????????????
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_PHONE_NUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using More than 10 digit on phone number input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_more_than_10Digit_PhoneNuber(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('12345678910')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_PHONE_NUMBER_XPATH)
        Utils(driver).assertion(text, "מס׳ טלפון לא תקין")

    @pytest.mark.sanity
    @allure.description('Successfully Join using less than 10 digit on phone number input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_less_than_10Digit_PhoneNuber(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('123456789')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_PHONE_NUMBER_XPATH)
        Utils(driver).assertion(text, "מס׳ טלפון לא תקין")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Email input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_Email(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('0123456789')
        join.Enter_Email_box('')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_EMAIL_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Email bu not using .com input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_invalid_Email_not_using_com(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('0123456789')
        join.Enter_Email_box('team2@techcereer')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_EMAIL_XPATH)
        Utils(driver).assertion(text, 'דוא״ל לא תקין')

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Email bu not using @ input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_invalid_Email_not_using_specialCharacter(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('0123456789')
        join.Enter_Email_box('team2.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_EMAIL_XPATH)
        Utils(driver).assertion(text, 'דוא״ל לא תקין')

    @pytest.mark.sanity
    @allure.description('Successfully Join using null city input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_city(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('Team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_CITY_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Street input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_Street(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('Team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_STRREET_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null HouseNumber input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_HouseNumber(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('Team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('')
        join.Enter_CityStreet_box('1')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_HOUSE_NUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class TestQA_Business_Interface_Chrome2(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('Successfully open Business interface')
    @allure.severity(allure.severity_level.NORMAL)
    def test_display_Business_Interface_PAGE_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        Utils(driver).assertion('trado', join.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Join using Valid input in all detail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_all_valid_detail_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.APPROVE_ERROR_XPATH)
        Utils(driver).assertion(text, 'Please Approve Our Policy')

    @pytest.mark.sanity
    @allure.description('Successfully Join using Valid input in all detail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_all_All_null_details_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Click_send_button()
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_FIRSTNAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")
        time.sleep(2)

    @pytest.mark.sanity
    @allure.description('Successfully Join using null first name input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_firstName_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_FIRSTNAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null last name input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_LastName_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_LASTNAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null BnNumber input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_BnNumber_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_BNNUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using letter BnNumber input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Letter_BnNumber_(self): # ????????????????????????????????????
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('abcd')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_BNNUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null BusinessName input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_BusinessName_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_BUSNIESS_NAME_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Phone number input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_PhoneNumber_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_PHONE_NUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using More than 10 digit on phone number input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_more_than_10Digit_PhoneNumber_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('12345678910')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_PHONE_NUMBER_XPATH)
        Utils(driver).assertion(text, "מס׳ טלפון לא תקין")

    @pytest.mark.sanity
    @allure.description('Successfully Join using less than 10 digit on phone number input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Less_than_10Digit_PhoneNumber_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('123456789')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_PHONE_NUMBER_XPATH)
        Utils(driver).assertion(text, "מס׳ טלפון לא תקין")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Email input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_Email_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('0123456789')
        join.Enter_Email_box('')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_EMAIL_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Email bu not using .com input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_invalid_Email_not_using_com_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('0123456789')
        join.Enter_Email_box('team2@techcereer')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_EMAIL_XPATH)
        Utils(driver).assertion(text, 'דוא״ל לא תקין')

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Email bu not using @ input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_invalid_Email_not_using_specialCharacter_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('2')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('0123456789')
        join.Enter_Email_box('team2.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_EMAIL_XPATH)
        Utils(driver).assertion(text, 'דוא״ל לא תקין')

    @pytest.mark.sanity
    @allure.description('Successfully Join using null city input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_city_(self): # ??????????????????????????????????
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('Team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_CITY_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null Street input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_Street_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('Team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_STRREET_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")

    @pytest.mark.sanity
    @allure.description('Successfully Join using null HouseNumber input')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_Null_HouseNumber_(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('Team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('')
        join.Enter_CityStreet_box('1')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.ERROR_HOUSE_NUMBER_XPATH)
        Utils(driver).assertion(text, "נא למלא שדה זה")


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class TestQA_Business_Interface_Firefox(Pre_Requirement_Login_Firefox):

    @pytest.mark.sanity
    @allure.description('Successfully Join using Valid input in all detail')
    @allure.severity(allure.severity_level.NORMAL)
    def test_JoinUs_using_all_valid_detail_2(self):
        driver = self.driver
        join = Business_Interface_Page(driver)
        join.Click_Business_Interface_Box()
        join.Enter_FirstName_box('team')
        join.Enter_LastName_Box('two')
        join.Enter_BnNumber_box('123456')
        join.Enter_BusinessName_box("tech-career")
        join.Enter_YourPhoneNumber_box('1951111111')
        join.Enter_Email_box('team2@techcereer.com')
        join.Enter_HouseNumber_box('456')
        join.Enter_CityStreet_box('2')
        join.Enter_City_box('beersheva')
        join.Click_send_button()
        text = join.Assert_text(path.APPROVE_ERROR_XPATH)
        Utils(driver).assertion(text, 'Please Approve Our Policy')


""" Business Interface page GUI """


class Test_Business_Interface_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for Business_Interface page using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Business_Interface_UI_Using_login(self):
        driver = self.driver
        Business_Interface = Business_Interface_Page(driver)
        Business_Interface.Click_Business_Interface_Box()
        font_size = Business_Interface.Check_font_size(path.BUSINESS_INTERFACE_CSS)
        assert font_size == "16px"
        font_weight = Business_Interface.Check_font_weight(path.BUSINESS_INTERFACE_CSS)
        assert font_weight == "400"
        text_align = Business_Interface.Check_text_align(path.BUSINESS_INTERFACE_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Business_Interface page with out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Business_Interface_UI_Using_without_login01(self):
        driver = self.driver
        Business_Interface = Business_Interface_Page(driver)
        Business_Interface.Click_Business_Interface_Box()
        font_size = Business_Interface.Check_font_size(path.BUSINESS_INTERFACE_CSS)
        assert font_size == "16px"
        font_weight = Business_Interface.Check_font_weight(path.BUSINESS_INTERFACE_CSS)
        assert font_weight == "400"
        text_align = Business_Interface.Check_text_align(path.BUSINESS_INTERFACE_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Business_Interface page with out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant')
    def test_Business_Interface_UI_Using_without_login02(self):
        driver = self.driver
        Business_Interface = Business_Interface_Page(driver)
        Business_Interface.Click_Business_Interface_Box()
        font_size = Business_Interface.Check_font_size(path.BUSINESS_INTERFACE_CSS)
        assert font_size == "16px"
        font_weight = Business_Interface.Check_font_weight(path.BUSINESS_INTERFACE_CSS)
        assert font_weight == "400"
        text_align = Business_Interface.Check_text_align(path.BUSINESS_INTERFACE_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Business_Interface page with out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_cocktails')
    def test_Business_Interface_UI_Using_without_login03(self):
        driver = self.driver
        Business_Interface = Business_Interface_Page(driver)
        Business_Interface.Click_Business_Interface_Box()
        font_size = Business_Interface.Check_font_size(path.BUSINESS_INTERFACE_CSS)
        assert font_size == "16px"
        font_weight = Business_Interface.Check_font_weight(path.BUSINESS_INTERFACE_CSS)
        assert font_weight == "400"
        text_align = Business_Interface.Check_text_align(path.BUSINESS_INTERFACE_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Business_Interface page with out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_none')
    def test_Business_Interface_UI_Using_without_login04(self):
        driver = self.driver
        Business_Interface = Business_Interface_Page(driver)
        Business_Interface.Click_Business_Interface_Box()
        font_size = Business_Interface.Check_font_size(path.BUSINESS_INTERFACE_CSS)
        assert font_size == "16px"
        font_weight = Business_Interface.Check_font_weight(path.BUSINESS_INTERFACE_CSS)
        assert font_weight == "400"
        text_align = Business_Interface.Check_text_align(path.BUSINESS_INTERFACE_CSS)
        assert text_align == 'start'
