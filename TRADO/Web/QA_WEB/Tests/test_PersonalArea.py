import allure
import pytest
from TRADO.Web.QA_WEB.Pages.personalAreaQA_Page import PageArea_page
from TRADO.Web.QA_WEB.Locators.locatorsQA_personalArea import Locators_PersonalArea as path
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.QA_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox
from Web.Utils.utils import Utils

"""TEST QA TRADO PRODUCT WITH LOGIN AND CHROME WEB BROWSER"""

Fix_PoneNumber = "3322114455"
# Fix_PoneNumber = "0548890900"


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_personalArea_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Test when all fields are valid')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_field_valid(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        Utils(driver).assertion("trado", driver.title)

    @pytest.mark.sanity
    @allure.description('Test when all fields are empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_field_null(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("")
        page.enter_last_name("")
        page.enter_phone("")
        page.enter_email("")
        page.enter_id("")
        page.enter_number('')
        page.enter_city('')
        page.click_Save_button()
        text = page.Assert_text(path.ERROR_FIRSTNAME_XPATH)
        Utils(driver).assertion('נא למלא שדה זה', text)

    @pytest.mark.sanity
    @allure.description('Test when no first name is entered in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_null_firstName(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        text = page.Assert_text(path.ERROR_FIRSTNAME_XPATH)
        Utils(driver).assertion('נא למלא שדה זה', text)

    @pytest.mark.sanity
    @allure.description('Test when no last name is entered in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_null_lastName(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        Utils(driver).assertion(driver.title, "trado")

    @pytest.mark.sanity
    @allure.description('Test when no id is entered in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_null_id(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        text = page.Assert_text(path.ERROR_ID_XPATH)
        Utils(driver).assertion('נא למלא שדה זה', text)

    @pytest.mark.sanity
    @allure.description(' Test when not entering a street number in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_null_street(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('')
        page.click_Save_button()
        Utils(driver).assertion("trado", driver.title)

    @pytest.mark.sanity
    @allure.description('Test when not entering a city in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_null_city(self): #  ????????????????????????????????
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("2222222222")
        page.enter_city('')
        page.enter_number('2')
        page.click_Save_button()
        Utils(driver).assertion("trado", driver.title)

    @pytest.mark.sanity
    @allure.description('Test when email is not entered in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_null_email(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        Utils(driver).assertion("trado", driver.title)

    @pytest.mark.sanity
    @allure.description('Test when email is not entered invalid in the field')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_with_Invalid_email(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("223@113")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        Utils(driver).assertion("trado", driver.title)


# ---------------------------------------------------------------------------------------------------------
""""TEST TRADO WEB PRODUCT WITH LOGIN AND FIREFOX WEB BROWSER"""


@pytest.mark.usefixtures('Valid_Login_With_login_Code')
class Test_personalArea_Firefox(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Test when all fields are valid')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Personal_area_all_field_valid_(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        page.click_Edit_button()
        page.enter_first_name("dawit")
        page.enter_last_name("samson")
        page.enter_phone(Fix_PoneNumber)
        page.enter_email("dawit@gmail.com")
        page.enter_id("2222222222")
        page.enter_city('Beersheva')
        page.enter_number('2')
        page.click_Save_button()
        Utils(driver).assertion("trado", driver.title)


""" Personal Area page GUI """


class Test_Personal_Area_GUI(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Check UI for Personal Area page using Login')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_With_login_Code')
    def test_Personal_Area_Using_with_Login(self):
        driver = self.driver
        page = PageArea_page(driver)
        page.Click_Personal_Area()
        font_size = page.Check_font_size(path.PERSONAL_AREA_CSS)
        assert font_size == "16px"
        font_weight = page.Check_font_weight(path.PERSONAL_AREA_CSS)
        assert font_weight == "400"
        text_align = page.Check_text_align(path.PERSONAL_AREA_CSS)
        assert text_align == 'start'
