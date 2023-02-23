from keyboard import press
import allure
import pytest
from TRADO.Web.QA_WEB.Pages.searchQA_page import Search_Page
from TRADO.Web.QA_WEB.Locators.locatorsQA_Search import Locators_Search as path
from TRADO.Web.QA_WEB.Utils.utils_QA import Utils
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Search_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_login_and_Search_existing_product_By_Using_Restaurant_and_Cocktail_field_S01(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == "goats"

    @pytest.mark.sanity
    @allure.description('Successfully search for an Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_login_and_Search_NonExisting_product_By_Using_Restaurant_and_Cocktail_field_S02(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("qqqqq")
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == "ggggg"

    @pytest.mark.sanity
    @allure.description('Successfully search for an Blank product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_login_and_Search_Blank_product_By_Using_Restaurant_and_Cocktail_field_S03(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("")
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == ""

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_and_add_to_product_page_S04(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Search.Click_Product_Empty_space()
        Search.Click_Product_Search_DropDown_list()
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.PRODUCT_DISPLAY_PAGE_XPATH)
        assert text == "goats"


    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product using enter')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_using_enter_S05(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        press('enter')
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == "goats"


@pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
class Test_Search_Chrome2(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Display Search_box using Cocktail Field')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Search_existing_product_With_out_Login_By_Using_Restaurant_and_Cocktail_field_S06(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_With_out_login_and_Search_NonExisting_product_By_Using_Restaurant_and_Cocktail_field_S07(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("qqqqq")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Blank product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_With_out_login_and_Search_Blank_product_By_Using_Restaurant_and_Cocktail_field__S08(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_and_add_to_product_page__S09(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Search.Click_Product_Empty_space()
        Search.Click_Product_Search_DropDown_list()
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.PRODUCT_DISPLAY_PAGE_XPATH)
        assert text == "goats"

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product using enter')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_using_enter_S10(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        press('enter')
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == "goats"


@pytest.mark.usefixtures('WithOut_login_selectField_none')
class Test_Search_Chrome3(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Display Search_box using Cocktail Field')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Search_existing_product_With_out_Login_By_Using_None_Field_S11(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_With_out_login_and_Search_NonExisting_product_By_None_Field_S12(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("qqqqq")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Blank product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_With_out_login_and_Search_Blank_product_By_None_Field_S13(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_and_add_to_product_page__S14(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Search.Click_Product_Empty_space()
        Search.Click_Product_Search_DropDown_list()
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.PRODUCT_DISPLAY_PAGE_XPATH)
        assert text == "goats"

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product using enter')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_using_enter_S15(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        press('enter')
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == "goats"


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""

@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_Search_FireFox(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_login_and_Search_existing_product_By_Using_Restaurant_and_Cocktail_field_S16(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product using enter')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_Search_existing_product_using_enter_S17(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        press('enter')
        text = Search.Assert_Product_DisplayPage_displayed_Search_Item(path.SEARCH_BOX_XPATH)
        assert text == "goats"


""" Search page GUI """


class Test_Search_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for Search using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Search_UI_Using_Home_S18(self):
        driver = self.driver
        Search = Search_Page(driver)
        font_size = Search.Check_font_size(path.SEARCH_CSS)
        assert font_size == "16px"
        font_weight = Search.Check_font_weight(path.SEARCH_CSS)
        assert font_weight == "400"
        text_align = Search.Check_text_align(path.SEARCH_CSS)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Search using out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Search_UI_Using_Home_S19(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        font_size = Search.Check_font_size(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert font_size == "16px"
        font_weight = Search.Check_font_weight(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert font_weight == "400"
        text_align = Search.Check_text_align(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Search using out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant')
    def test_Search_UI_Using_Home_S20(self):
        driver = self.driver
        Search = Search_Page(driver)
        font_size = Search.Check_font_size(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert font_size == "16px"
        font_weight = Search.Check_font_weight(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert font_weight == "400"
        text_align = Search.Check_text_align(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert text_align == 'start'

    @pytest.mark.sanity
    @allure.description('Check UI for Search using out Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_none')
    def test_Search_UI_Using_Home_S21(self):
        driver = self.driver
        Search = Search_Page(driver)
        font_size = Search.Check_font_size(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert font_size == "16px"
        font_weight = Search.Check_font_weight(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert font_weight == "400"
        text_align = Search.Check_text_align(path.SEARCH_CSS_WITHOUT_LOGIN)
        assert text_align == 'start'
