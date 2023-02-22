import time

import allure
import pytest
from QA_WEB.Pages.paymentQA_page import Payment_Page
from QA_WEB.Locators.locatorsQA_Payment import Locators_Payment
from QA_WEB.Utils.utils_QA import Utils
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class TestQA_Payment_Chrome1(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully fill all the detail for purchase a product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Product_check_out_by_using_all_valid_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO', '2444666666')
        payments.Click_Complete_Purchase_button()
        text = payments.Assert_text(payments.driver.title)
        Utils(driver).assertion(text, "trado")
# --------------------------------------------------------------------------------------------------------
    @pytest.mark.sanity
    @allure.description('Purchase with not filling the detail for purchase a product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Valid_Product_check_out_by_using_null_valid_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed('', '', '', "", "", "", "", "")
        payments.Enter_all_Shipping_Address_filed('', '', '', '', '', '', '', '', '')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to purchase without busines name ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_out_by_without_bussines_name_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to purchase without a BNnumber')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_BNnumber_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('order products with email account null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_to_with_null_email_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('order products with invalid email account')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_to_invalid_email_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to order products without city ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_order_no_filling_city_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to order products without street number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_order_no_filling_street_number_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to purchase without home number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_order_no_filling_homeNumber_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to purchase without entrance number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checking_to_purchase_no_filling_entranceNumber_fields(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('order products without floor number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_without_floor_number(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without city from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_city_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without street number from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_streetNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', '', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO', '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without home number from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_homeNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without entrance number from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_entranceNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without floor number from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_floorNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order by writing letters on  floor number field from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_floorNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', 'ab', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without contact name from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_contactName_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', '', 'TEAM', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without first name from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_firstName_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', '', 'TWO',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without last name from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_lastName_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', '',
                                                  '2444666666')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order without phoneNumber from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_without_phoneNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO','')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order with invalid phoneNumber by adding more numbers from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_order_by_invalid_phoneNumber_more_digit_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '244466666677')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order with invalid phoneNumber from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_invalid_phoneNumber_from_shipping_field(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2442')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('checking to order by writing phone number with letters from shipping field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_phoneNumber_adding_letters(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "2", "team2@gmail.com", "beersheva", "nurit", "2", "1", "1")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', '1', '1', '2', 'TEAM2', 'TEAM', 'TWO',
                                                  '2444abc')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to order products by incorrect method all numbers field changing by letters')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checking_all_numberField_change_by_letter(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("Trado", "a", "team2@gmail.com", "beersheva", "nurit", "b", "c", "d")
        payments.Enter_all_Shipping_Address_filed('Beersheva', 'nurit', 'e', 'f', 'g', 'TEAM2', 'TEAM', 'TWO', 'opqxyz')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to order products by incorrect method all letters field changing by number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checking_all_numberField_change_by_letter(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("1111", "22", "33", "44", "55", "66", "77", "88")
        payments.Enter_all_Shipping_Address_filed('99', '00', '11', '12', '13', '14', '15', '16', '17')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")

    @pytest.mark.sanity
    @allure.description('Trying to order products by incorrect method all  fields changing by special characters')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checking_all_numberField_change_by_letter(self):
        driver = self.driver
        payments = Payment_Page(driver)
        payments.Valid_open_payment_page()
        payments.Enter_all_Invoice_detail_filed("@@@", "##", "$$", "%%", "^^", "&&", "**", "((")
        payments.Enter_all_Shipping_Address_filed('))', '??', '>>', '<<', '!!', '$%', '%&', '*%', '#$')
        payments.Click_Complete_Purchase_button()
        Utils(driver).assertion(payments.driver.title, "Trado")
