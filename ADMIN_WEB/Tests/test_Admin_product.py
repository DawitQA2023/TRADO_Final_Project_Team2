import allure
import pytest
from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.productAdmin_page import Product_Page
from QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome



class Test_product_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully select the product moduls in Trado Admin')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_product_moduls(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        Utils(driver).assertion(self.driver.title, "מוצרים - trado")

    @pytest.mark.sanity
    @allure.description('From product moduls  click the kebar and add products buttons ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_add_products_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_plusProduct_buttons()
        Utils(driver).assertion(self.driver.title, "מוצרים - trado")

    @pytest.mark.sanity
    @allure.description('Insert data to only barcode and name field box from required ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_barcodeAndName_fields(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_plusProduct_buttons()
        pro.enter_barcode_fields("123456")
        pro.enter_name_fields("Tela")
        pro.enter_price_fields("")
        pro.click_next_product_buttons()
        pro.click_next_product_buttons()
        text = pro.Assert_price_error()
        Utils(driver).assertion("תאריך תפוגה", text)

    @pytest.mark.sanity
    @allure.description('Insert data to only price and name field box from required ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_priceAndName_fields(self, Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_plusProduct_buttons()
        pro.enter_barcode_fields("")
        pro.enter_name_fields("Tej")
        pro.enter_price_fields("200")
        pro.click_next_product_buttons()
        text = pro.Assert_barcode_error()
        Utils(driver).assertion("נא למלא שדה זהxxx", text)

    @pytest.mark.sanity
    @allure.description('Insert data to only price and barcode field box from required ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_priceAndbarcode_fields(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_plusProduct_buttons()
        pro.enter_barcode_fields("123456")
        pro.enter_name_fields("")
        pro.enter_price_fields("200")
        pro.click_next_product_buttons()
        text = pro.Assert_name_error()
        Utils(driver).assertion("נא למלא שדה זהxxx", text)

    @pytest.mark.sanity
    @allure.description('Insert data for required all field box  ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_valid_input_required_fields(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_plusProduct_buttons()
        pro.enter_barcode_fields("123456")
        pro.enter_name_fields("Arekie")
        pro.enter_price_fields("200")
        pro.click_next_product_buttons()
        text  = pro.Assert_first_page()
        Utils(driver).assertion("קטגוריה על*", text)


    # ----------------------------------------------------------------------------------------------------------------

    @pytest.mark.sanity
    @allure.description('Insert data for required all field box select for each catagoreis  ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_valid_input_pro_info_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        text = production.Assert_product_info_page()
        Utils(driver).assertion("מינימום קרטונים להזמנה", text)

    @pytest.mark.sanity
    @allure.description('Insert data for only storID required all field box with null sctionID ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_only_storeID_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        text = production.Assert_section_id_page()
        Utils(driver).assertion("קטגוריה על*", text)

    @pytest.mark.sanity
    @allure.description('Insert data for ONLY SECTION_ID required all field box with storeID ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_only_sectionID_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_next_productInfo_buttons()
        text = production.Assert_store_id_page()
        Utils(driver).assertion("קטגוריה על*", text)

    @pytest.mark.sanity
    @allure.description('Insert data for NULL required inputs all field box with  null storeID ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_null_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_next_productInfo_buttons()
        text = production.Assert_NULL_page()
        Utils(driver).assertion("בירות", text)


    @pytest.mark.sanity
    @allure.description('Insert data for sectin id and departments required inputs all field box with  null storeID ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_null_store_id_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_next_productInfo_buttons()
        text = production.Assert_store_id_page()
        Utils(driver).assertion("Osem Osemioio", text)

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.sanity
    @allure.description('Enter a data for requierd fields in product unit paga if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_valid_input_unit_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_unitCrtone_fields(10)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        text = production.Assert_unit_page()
        Utils(driver).assertion("מידע נוסף", text)

    @pytest.mark.sanity
    @allure.description('Enter a data onliy "AMOUNT AND MIN ORDER " for requierd fields in product unit paga if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_amount_and_minorder_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        text = production.Assert_unitIncarton()
        Utils(driver).assertion("מינימום קרטונים להזמנה", text)

    @pytest.mark.sanity
    @allure.description('Enter a data onliy "AMOUNT AND UNIT IN CARTON " for requierd fields in product unit paga if ''any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_amount_and_unit_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_unitCrtone_fields(10)
        production.click_next_productUnit_buttons()
        text = production.Assert_min_order()
        Utils(driver).assertion("מינימום קרטונים להזמנה", text)


    @pytest.mark.sanity
    @allure.description('Enter a data onliy "UNIT_IN CARTONE AND MIN ORDER " for requierd fields in product unit paga ' 'if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_with_minOrder_and_unit_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_unitCrtone_fields(10)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        text = production.Assert_amount_carton()
        Utils(driver).assertion("מינימום קרטונים להזמנה", text)

    # -------------------------------------------------------------------------------------------------------------

    @pytest.mark.sanity
    @allure.description('Enter a data for requierd fields in product delivery paga if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_valid_input_delivery_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_unitCrtone_fields(10)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        production.enter_city_fields("TSEFAT")
        production.enter_street_fields("TSEHAL")
        production.click_next_product_Delivery_buttons()
        text = production.Assert_delivery_carton()
        Utils(driver).assertion("תיאור", text)

    @pytest.mark.sanity
    @allure.description('Enter a data for only "CITY" requierd fields in product delivery paga if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_only_city_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_unitCrtone_fields(10)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        production.enter_city_fields("")
        production.enter_street_fields("TSEHAL")
        production.click_next_product_Delivery_buttons()
        text = production.Assert_delivery_city_carton()
        Utils(driver).assertion("תיאור", text)

    @pytest.mark.sanity
    @allure.description('Enter a NULL INPUT  for requeired fields in product delivery paga if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_only_street_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_unitCrtone_fields(10)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        production.enter_city_fields("TSEFAT")
        production.enter_street_fields("")
        production.click_next_product_Delivery_buttons()
        text = production.Assert_delivery_street_carton()
        Utils(driver).assertion("תיאור", text)

    @pytest.mark.sanity
    @allure.description('Enter a NULL INPUT  for requeired fields in product delivery paga if any..')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_only_null_required_fields(self):
        driver = self.driver
        production = Product_Page(driver)
        production.click_on_product_sidebar()
        production.click_kebab_buttons()
        production.click_plusProduct_buttons()
        production.enter_barcode_fields("123456")
        production.enter_name_fields("Arekie")
        production.enter_price_fields("200")
        production.click_next_product_buttons()
        production.click_drope_down_section_button()
        production.select_sections_from_given()
        production.click_department_button()
        production.click_drope_down_productTag_button()
        production.select_product_tag_given()
        production.click_drope_down_store_button()
        production.select_store_from_given()
        production.click_next_productInfo_buttons()
        production.enter_amount_fields(100)
        production.enter_unitCrtone_fields(10)
        production.enter_minOrder_fields(2)
        production.click_next_productUnit_buttons()
        production.enter_city_fields("")
        production.enter_street_fields("")
        production.click_next_product_Delivery_buttons()
        text = production.Assert_delivery_null_carton()
        Utils(driver).assertion("תיאור", text)

# ----------------------------------------------------------------------------------------------------------------
    @pytest.mark.sanity
    @allure.description('From product moduls  click page2  and add products buttons ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_drop_products_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_drop_buttons()
        pro.click_list_number()
        Utils(driver).assertion(self.driver.title, "מוצרים - trado")

    @pytest.mark.sanity
    @allure.description('From product moduls  click the page3 and add products buttons ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_search_products_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.enter_search_box("xxxxxx")
        text = pro.Assert_search_valid_products()
        Utils(driver).assertion("תיאור", text)

    @pytest.mark.sanity
    @allure.description('From product moduls  click the page3 LANGUAGE and add products buttons ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_languageUS_change_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_langugeUS_buttons()
        text = pro.Assert_languageUS_()
        Utils(driver).assertion("display 1-50 of 287 rows", text)

    @pytest.mark.sanity
    @allure.description('From product moduls  click the page3 and add products buttons ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_languageIL_change_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_langugeUS_buttons()
        pro.click_langugeIL_buttons()
        text = pro.Assert_languageIL_()
        Utils(driver).assertion("display 1-50 of 287 rows", text)



    @pytest.mark.sanity
    @allure.description('From product moduls  click the page5and add products buttons ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_page5_products_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_plusProduct_buttons()
        pro.enter_barcode_fields("123456")
        pro.enter_name_fields("Arekie")
        pro.enter_price_fields("200")
        pro.click_next_product_buttons()
        pro.click_back_button()
        pro.Assert_backTitle_()
        Utils(driver).assertion(self.driver.title, "מוצרים - trado")

    @pytest.mark.sanity
    @allure.description('Export file from "ADMIN PRODUCTS" TO ....')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_export_products_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_Export_buttons()
        Utils(driver).assertion(self.driver.title, "מוצרים - trado")

    @pytest.mark.sanity
    @allure.description('Import file from "OTHERS" TO ."ADMIN PRODUCTS"...')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_import_products_too(self):
        driver = self.driver
        pro = Product_Page(driver)
        pro.click_on_product_sidebar()
        pro.click_kebab_buttons()
        pro.click_IMPORT_buttons()
        TEXT = pro.Assert_importTitle_()
        Utils(driver).assertion(TEXT, "Import File")
# ---------------------------------------------------------------------------------------------






