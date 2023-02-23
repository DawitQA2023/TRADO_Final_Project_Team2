import allure
import pytest
from TRADO.Web.QA_WEB.Pages.upload_new_productQA_page import Upload_New_Product_Page
from TRADO.Web.QA_WEB.Locators.locatorsQA_upload_product import Locators_Upload_New_Product as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils


"""Tests Upload new product when User not having Store """


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Upload_New_Product_not_having_store(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Upload a product incorrectly when the user does not have a store')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_without_store01(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', 'Team2@trado.com', 'team2.com', 'beersheva',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.store_validation_failed_message(), "Undefined' לא תקין")

    @pytest.mark.regression
    @allure.description('Upload a product incorrectly when the user does not have a store and storeID is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_storeID_is_null02(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['', 'Team2', '0147258367', 'Team2@trado.com', 'team2.com', 'beersheva',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(0), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and storeName is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_storeName_is_null03(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', '', '0147258367', 'Team2@trado.com', 'team2.com', 'beersheva',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(1), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(1), "נא למלא שדה זה")

    @pytest.mark.regression
    @allure.description('Upload a product incorrectly when the user does not have a store and phoneNumber is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_PhoneNumber_is_null04(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Brands', '', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                               'Herzel', '1'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(2), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(2), "נא למלא שדה זה")

    @pytest.mark.regression
    @allure.description('Upload a product incorrectly when the user does not have a store and email is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_email_is_null05(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', '', 'team2.com', 'beersheva',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(3), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(3), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and webLink is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_webLink_is_null06(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', 'Team2@trado.com', '', 'beersheva',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(4), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(4), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and cityName is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_CityName_is_null07(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', 'Team2@trado.com', 'team2.com', '',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(5), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(5), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and addressName is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_AddressName_is_null08(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', 'Team2@trado.com', 'team2.com', 'beersheva',
                                               '', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(6), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(6), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and streetNumber is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_StreetName_is_null09(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', 'Team2@trado.com', 'team2.com', 'beersheva',
                                               'nurit', ''])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(7), 'Please fill in this field.')
        Utils(driver).assertion(upload_product.enter_the_field_message(7), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and email is Invalid(Chars)')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_Email_is_Invalid_character10(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        data = ['1', 'Team2', '0147258367', 'team2', 'team2.com', 'beersheva', 'nurit', '2']
        upload_product.enter_all_inputs_filed(data)
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(3), "Please include an '@' in the email "
                                                                               f"address. '{data[3]}' is missing an '@'.")
        Utils(driver).assertion(upload_product.enter_the_field_message(3), "דוא״ל לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and email is Invalid(Chars@)')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_Email_is_Invalid_character11(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        data = ['1', 'Team2', '0147258367', 'team2@', 'team2.com', 'beersheva', 'nurit', '2']
        upload_product.enter_all_inputs_filed(data)
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(3),
                                f"Please enter a part following '@'. '{data[3]}' is incomplete.")
        Utils(driver).assertion(upload_product.enter_the_field_message(3), "דוא״ל לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and email is Invalid(Chars+.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_Email_is_Invalid_character12(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        data = ['1', 'Team2', '0147258367', 'team2@trado.', 'team2.com', 'beersheva', 'nurit', '2']
        upload_product.enter_all_inputs_filed(data)
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.messages_for_all_the_fields(3),
                                f"'.' is used at a wrong position in '{upload_product.js_email_msg_point(data[3])}'.")
        Utils(driver).assertion(upload_product.enter_the_field_message(3), "דוא״ל לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and phone is Invalid (+) ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_phone_number_having_more_digits13(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        data = ['1', 'Team2', '014725836777', 'team2@trado.com', 'team2.com', 'beersheva', 'nurit', '2']
        upload_product.enter_all_inputs_filed(data)
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.enter_the_field_message(2), "מס׳ טלפון לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and phone is Invalid (-)')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_when_phone_number_having_less_digits14(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        data = ['1', 'Team2', '014', 'team2@trado.com', 'team2.com', 'beersheva', 'nurit', '2']
        upload_product.enter_all_inputs_filed(data)
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.enter_the_field_message(2), "מס׳ טלפון לא תקין")


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Upload_New_Product_having_store(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Upload a product incorrectly when the user does not have a store')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_without_store15(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        upload_product.enter_all_inputs_filed(['1', 'Team2', '0147258367', 'Team2@trado.com', 'team2.com', 'beersheva',
                                               'nurit', '2'])
        upload_product.click_add_new_product_button()
        Utils(driver).assertion(upload_product.store_validation_failed_message(), "'Undefined' לא תקין")


""" Upload product page GUI """


class Test_Home_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for Home page using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Home_UI_Using_Home16(self):
        driver = self.driver
        upload_product = Upload_New_Product_Page(driver)
        upload_product.click_add_new_product_section()
        font_size = upload_product.Check_font_size(path.UPLOAD_CSS)
        assert font_size == "16px"
        font_weight = upload_product.Check_font_weight(path.UPLOAD_CSS)
        assert font_weight == "400"
        text_align = upload_product.Check_text_align(path.UPLOAD_CSS)
        assert text_align == 'start'
