import allure
import pytest
from TRADO.QA_WEB.Pages.searchQA_page import Search_Page
from TRADO.QA_WEB.Utils.utils_QA import Utils
from TRADO.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome


class Test_Search_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Validate_login_and_Search_existing_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Validate_login_and_Search_NonExisting_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("qqqqq")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Blank product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Validate_login_and_Search_Blank_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Display Search_box using Cocktail Field')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Validate_Search_existing_product_With_out_Login_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Search.Click_Product_Empty_space()
        Search.Click_SearchBox()
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Validate_With_out_login_and_Search_NonExisting_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("qqqqq")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Blank product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Validate_With_out_login_and_Search_Blank_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully Display Search_box using Cocktail Field')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Validate_Search_existing_product_With_out_Login_By_Using_Restaurant_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Search.Click_Product_Empty_space()
        Search.Click_SearchBox()
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Validate_With_out_login_and_Search_NonExisting_product_By_Using_Restaurant(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("qqqqq")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully search for an Blank product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('WithOut_login_selectField_restaurant_and_cocktails')
    def test_Validate_With_out_login_and_Search_Blank_product_By_Using_Restaurant(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)


class Test_Search_FireFox(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Validate_login_and_Search_existing_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Search_Page(driver)
        Search.Click_SearchBox()
        Search.Enter_Search_product("goats")
        Utils(driver).assertion(Search.TITLE1, self.driver.title)
