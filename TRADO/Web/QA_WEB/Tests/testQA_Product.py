import time
import allure
import pytest
from TRADO.Web.QA_WEB.Pages.ProductQA_page import Product_page
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox
from TRADO.Web.QA_WEB.Locators.locatoreQA_products import Locators_Products as path

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Product01(Pre_Requirement_Login_Chrome):
    #  -------------------------------------- PROMOTION CATEGORIES -------------------------------------
    @pytest.mark.sanity
    @allure.description('CLICK "GORILLA PRODUCTS" IN PROMOTION ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Gorilla_glue_Product_01(self):
        driver = self.driver
        sales = Product_page(driver)
        sales.Click_gorila_product()
        Text = sales.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("גורילה גלו", Text)

    @pytest.mark.sanity
    @allure.description('CLICK " ADD ALL PRODUCTS "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_product_add_to_cart_chrome_02(self):
        driver = self.driver
        ALL_PRODUCTS = Product_page(driver)
        ALL_PRODUCTS.click_all_products_and_add_cart(2)
        time.sleep(5)

    @pytest.mark.sanity
    @allure.description('CLICK " +  TO CART PRODUCTS" IN sales  ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_promotion_product_Add_To_Cart_03(self):
        driver = self.driver
        sales = Product_page(driver)
        sales.Click_gorila_product()
        sales.Click_plus_button(2)
        Text1 = sales.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = sales.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLICK " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decrease_Quantity_from_Cart_04(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_minus_button(3)
        Text1 = PROMOTION.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = PROMOTION.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_05(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_minus_button(3)
        PROMOTION.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = PROMOTION.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_linkbutton_06(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_minus_button(3)
        PROMOTION.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = PROMOTION.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " PAYMENT  BUTTON " TO PURCHASE THE PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_payment_button_07(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_plus_button(2)
        PROMOTION.Click_payment_button()
        time.sleep(2)

    # --------------------------------------------- SNACK CATEGORIES ------------------------------------------


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Snack_Product02(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('CLICK "SNACK" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_snack_trado_QA_PAGE_08(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        text = SNACK.Assert_text(path.SNACK_TITLE)
        Utils(driver).assertion("חטיפים", text)

    @pytest.mark.sanity
    @allure.description('CLICK "SNACK" CLICK')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_goat_product_trado_QA_PAGE_09(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        text = SNACK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("Goats", text)

    @pytest.mark.sanity
    @allure.description('Click " +  TO CART PRODUCTS" IN SNACK ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_Add_To_Cart_10(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_plus_button(2)
        Text1 = SNACK.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = SNACK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLICK " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decreases_Quantity_from_Cart_11(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_minus_button(3)
        Text1 = SNACK.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = SNACK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_12(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_minus_button(3)
        SNACK.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = SNACK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_link_button_13(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_minus_button(3)
        SNACK.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = SNACK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " PAYMENT  BUTTON " TO PURCHASE THE PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_payment_button_14(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_plus_button(2)
        SNACK.Click_payment_button()


# ---------------------------------------------------- DRINKS CATEGORISE -------------------------------------------
@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Drinks_Product03(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('CLICK "DRINK" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drink_trado_QA_PAGE_15(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        text = DRINK.Assert_text(path.DRINK_TITLE)
        Utils(driver).assertion("משקאות", text)

    @pytest.mark.sanity
    @allure.description('CLICK "DRINK" CATEGORIES')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Goat_milk_trado_QA_PAGE_16(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        text = DRINK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("חטיפים", text)

    @pytest.mark.sanity
    @allure.description('CCLIKC " +  TO CART PRODUCTS" IN PROMOTION ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drink_product_Add_To_Cart_17(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_plus_button(2)
        Text1 = DRINK.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = DRINK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLIKC " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decrease_Quantity_from_Cart_18(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_minus_button(3)
        Text1 = DRINK.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = DRINK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_19(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_minus_button(3)
        DRINK.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = DRINK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_link_button_20(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_minus_button(3)
        DRINK.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = DRINK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " PAYMENT  BUTTON " TO PURCHAS THE PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_payment_button_21(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_plus_button(2)
        DRINK.Click_payment_button()

    # --------------------------------------------  CANNABIS CATEGORIES -----------------------------------


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Cannabis_Product04(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('CLICK "CANNABIS" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cannabis_trado_QA_PAGE_22(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        text = CANNABIS.Assert_text(path.CANABIES_TITLE)
        Utils(driver).assertion("קנאביס", text)

    @pytest.mark.sanity
    @allure.description('CLICK "CANNABIS" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Goat_milk_trado_QA_PAGE_23(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        text = CANNABIS.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("גורילה גלו", text)

    @pytest.mark.sanity
    @allure.description('CLICK " +  TO CART PRODUCTS" IN CANNABIS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drink_product_Add_To_Cart_24(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_plus_button(2)
        Text1 = CANNABIS.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = CANNABIS.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLICK " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decrease_Quantity_from_Cart_25(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_minus_button(3)
        Text1 = CANNABIS.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = CANNABIS.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_26(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_minus_button(3)
        CANNABIS.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = CANNABIS.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_link_button_27(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_minus_button(3)
        CANNABIS.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = CANNABIS.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " PAYMENT  BUTTON " TO PURCHAS THE PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_payment_button_28(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_plus_button(2)
        CANNABIS.Click_payment_button()


# ------------------------------------------------------------------------------------------------------

"""TEST TRADO PRODUCTS WITHOUT LOGIN"""


# ------------------------------------ PROMOTION PRODUCTS- ---------------------------------------------
@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Promotion_Product05(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('CLICK "GORILLA PRODUCTS" IN PROMOTION ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Gorilla_glue_Product_NL_29(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        Text = PROMOTION.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("גורילה גלו", Text)

    @pytest.mark.sanity
    @allure.description('CLICK " +  TO CART PRODUCTS" IN PROMOTION  ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_promotion_product_Add_To_Cart_NL_30(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_plus_button(2)
        Text1 = PROMOTION.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = PROMOTION.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLICK " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decrease_Quantity_from_Cart_NL_31(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_minus_button(3)
        Text1 = PROMOTION.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = PROMOTION.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_NL_32(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_minus_button(3)
        PROMOTION.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = PROMOTION.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_linkbutton_NL_33(self):
        driver = self.driver
        PROMOTION = Product_page(driver)
        PROMOTION.Click_promotion_categories()
        PROMOTION.Click_gorila_product()
        PROMOTION.Click_minus_button(3)
        PROMOTION.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = PROMOTION.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)


"""""  NL = WITH OUT LOGIN """


# -------------------------------------------- CANNABIS PRODUCT ---------------------------------------------


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Cannabis_Product06(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('CLICK "CANNABIS" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cannabis_trado_QA_PAGE_NL_34(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        text = CANNABIS.Assert_text(path.CANABIES_TITLE)
        Utils(driver).assertion("קנאביס", text)

    @pytest.mark.sanity
    @allure.description('CLICK "CANNABIS" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Goat_milk_trado_QA_PAGE_NL_35(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        text = CANNABIS.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("גורילה גלו", text)

    @pytest.mark.sanity
    @allure.description('CLICK " +  TO CART PRODUCTS" IN CANNABIS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drink_product_Add_To_Cart_NL_36(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_plus_button(2)
        Text1 = CANNABIS.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = CANNABIS.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLICK " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decrease_Quantity_from_Cart_NL_37(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_minus_button(3)
        Text1 = CANNABIS.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = CANNABIS.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_NL_38(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_minus_button(3)
        CANNABIS.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = CANNABIS.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_link_button_NL_39(self):
        driver = self.driver
        CANNABIS = Product_page(driver)
        CANNABIS.Click_cannabis_link()
        CANNABIS.Click_Gorilla_glue_product()
        CANNABIS.Click_minus_button(3)
        CANNABIS.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = CANNABIS.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)


"""""  NL = WITH OUT LOGIN """


# ----------------------------------------------- DRINK PRODUCT --------------------------------------------------------
@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Drinks_Product07(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('CLICK "DRINK" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_snack_trado_QA_PAGE_NL_40(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        text = DRINK.Assert_text(path.DRINK_TITLE)
        Utils(driver).assertion("משקאות", text)

    @pytest.mark.sanity
    @allure.description('CLICK "DRINK" CATEGORIES')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Goat_milk_trado_QA_PAGE_NL_41(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        text = DRINK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("חטיפים", text)

    @pytest.mark.sanity
    @allure.description('CLIKC " +  TO CART PRODUCTS" IN PROMOTION ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drink_product_Add_To_Cart_NL_42(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_plus_button(2)
        Text1 = DRINK.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = DRINK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLIKC " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decrease_Quantity_from_Cart_NL_43(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_minus_button(3)
        Text1 = DRINK.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = DRINK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_NL_44(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_minus_button(3)
        DRINK.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = DRINK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_link_button_NL_45(self):
        driver = self.driver
        DRINK = Product_page(driver)
        DRINK.Click_drink_link()
        DRINK.Click_goat_milk_product()
        DRINK.Click_minus_button(3)
        DRINK.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = DRINK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)


"""""  NL = WITH OUT LOGIN """


# ------------------------------------------------ SNACK PRODUCTS ----------------------------------------------
@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Snack_Product08(Pre_Requirement_Login_Chrome):

    @pytest.mark.sanity
    @allure.description('CLICK "SNACK" CATEGORIES')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Snack_trado_QA_PAGE_NL_46(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        text = SNACK.Assert_text(path.SNACK_TITLE)
        Utils(driver).assertion("חטיפים", text)

    @pytest.mark.sanity
    @allure.description('CLICK "SNACK" CLICK')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Snack_trado_QA_PAGE_NL_47(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        text = SNACK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion("goats", text)

    @pytest.mark.sanity
    @allure.description('Click " +  TO CART PRODUCTS" IN SNACK ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_snack_product_Add_To_Cart_NL_48(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_plus_button(2)
        Text1 = SNACK.Assert_text(path.ADDED_PRODUCT_NAME)
        Text2 = SNACK.Assert_text(path.DISPLAY_NAME_TITLE)
        Utils(driver).assertion(Text2, Text1)

    @pytest.mark.sanity
    @allure.description('CLICK " -  TO DECREASE QUANTITY PRODUCTS" IN CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Decreases_Quantity_from_Cart_NL_49(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_minus_button(3)
        Text1 = SNACK.Assert_text(path.ADDED_PRODUCT_NUM)
        Text2 = SNACK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion(Text1, Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE ICON  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_icon_button_NL_50(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_minus_button(3)
        SNACK.Click_Delete_product_from_Cart_by_delete_icon()
        Text2 = SNACK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " DELETE LINK  BUTTON " TO DELETE THE PRODUCTS" FROM CART ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_link_button_NL_51(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_minus_button(3)
        SNACK.Click_Delete_product_from_Cart_by_delete_link()
        Text2 = SNACK.Assert_text(path.MINUS_PRODUCT_NUM)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " PAYMENT  BUTTON " TO PURCHASE THE PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_payment_buttonNL_52(self):
        driver = self.driver
        SNACK = Product_page(driver)
        SNACK.Click_snack_link()
        SNACK.Click_goat_product()
        SNACK.Click_plus_button(2)
        SNACK.Click_payment_button()

    @pytest.mark.sanity
    @allure.description('CLICK " ADD ALL PRODUCTS "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_product_AddToCart_NL_53(self):
        driver = self.driver
        ALL_PRODUCTS = Product_page(driver)
        ALL_PRODUCTS.click_all_products_and_add_cart(3)

        # ----------------------------------- OTHERS PARTS OF HOME PAGE ----------------------------------------------

    @pytest.mark.sanity
    @allure.description('CLICK " FORMATE CHANGE1 "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_format_change1_button_NL_54(self):
        driver = self.driver
        OTHERS = Product_page(driver)
        OTHERS.Click_format_chang2()
        Text2 = OTHERS.Assert_text(path.GORILLA_POSTION_XPATH)
        Utils(driver).assertion("גורילה גלו", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " FORMATE CHANGE2 "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_format_change2_button_NL_55(self):
        driver = self.driver
        OTHERS = Product_page(driver)
        OTHERS.Click_format_chang2()
        OTHERS.Click_format_chang1()
        Text2 = OTHERS.Assert_text(path.GORILLA_POSTION_XPATH)
        Utils(driver).assertion("גורילה גלו", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " SELECT PRODUCT BY POPULARITY "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_select_by_popularity_price_NL_56(self):
        driver = self.driver
        OTHERS = Product_page(driver)
        OTHERS.Click_sorting()
        OTHERS.Click_popularity()
        Text2 = OTHERS.Assert_text(path.GORILLA_POSTION_XPATH)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " SELECT PRODUCT BY LOWEST PRICE "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_select_by_lowest_price_NL_57(self):
        driver = self.driver
        OTHERS = Product_page(driver)
        OTHERS.Click_sorting()
        OTHERS.Click_lowest_price()
        Text2 = OTHERS.Assert_text(path.GORILLA_POSTION_XPATH)
        Utils(driver).assertion("", Text2)

    @pytest.mark.sanity
    @allure.description('CLICK " SELECT PRODUCT BY HIGHEST PRICE "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_select_by_highest_price_NL_68(self):
        driver = self.driver
        OTHERS = Product_page(driver)
        OTHERS.Click_sorting()
        OTHERS.Click_highest_price()
        Text2 = OTHERS.Assert_text(path.GORILLA_POSTION_XPATH)
        Utils(driver).assertion("", Text2)


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Promotion_Product09(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('CLICK " ADD ALL PRODUCTS "  PRODUCTS ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_product_add_to_cart_firefox59(self):
        driver = self.driver
        ALL_PRODUCTS = Product_page(driver)
        ALL_PRODUCTS.click_all_products_and_add_cart(5)



""" Product page GUI """


class Test_Product_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for Product page using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Product_UI_Using_login(self):
        driver = self.driver
        Product = Product_page(driver)
        font_size = Product.Check_font_size(path.PRODUCT_CSS)
        assert font_size == "16px"
        font_weight = Product.Check_font_weight(path.PRODUCT_CSS)
        assert font_weight == "400"
        text_align = Product.Check_text_align(path.PRODUCT_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Product  page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Product_UI_WithOut_login_2(self):
        driver = self.driver
        Product = Product_page(driver)
        font_size = Product.Check_font_size(path.PRODUCT_CSS)
        assert font_size == "16px"
        font_weight = Product.Check_font_weight(path.PRODUCT_CSS)
        assert font_weight == "400"
        text_align = Product.Check_text_align(path.PRODUCT_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Product  page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant')
    def test_Product_UI_WithOut_login_2(self):
        driver = self.driver
        Product = Product_page(driver)
        font_size = Product.Check_font_size(path.PRODUCT_CSS)
        assert font_size == "16px"
        font_weight = Product.Check_font_weight(path.PRODUCT_CSS)
        assert font_weight == "400"
        text_align = Product.Check_text_align(path.PRODUCT_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Product  page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_cocktails')
    def test_Product_UI_WithOut_login_3(self):
        driver = self.driver
        Product = Product_page(driver)
        font_size = Product.Check_font_size(path.PRODUCT_CSS)
        assert font_size == "16px"
        font_weight = Product.Check_font_weight(path.PRODUCT_CSS)
        assert font_weight == "400"
        text_align = Product.Check_text_align(path.PRODUCT_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Product page Without Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_none')
    def test_Home_UI_Using_Home4(self):
        driver = self.driver
        Product = Product_page(driver)
        font_size = Product.Check_font_size(path.PRODUCT_CSS)
        assert font_size == "16px"
        font_weight = Product.Check_font_weight(path.PRODUCT_CSS)
        assert font_weight == "400"
        text_align = Product.Check_text_align(path.PRODUCT_CSS)
        assert text_align == 'start'
