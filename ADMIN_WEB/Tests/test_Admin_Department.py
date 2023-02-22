import allure
import pytest
from selenium.webdriver.common.by import By

from ADMIN_WEB.Utils.utils_Admin import Utils
from ADMIN_WEB.Pages.department_page import Department_Page
from ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from ADMIN_WEB.Locators.locators_Admin_Department import Locators_Dep


@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
class Test_User_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Click Export button ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Export_Deparment_from_admin(self):
        driver = self.driver
        user = Department_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        Text = self.driver.find_element(By.XPATH, Locators_Dep.EXPORT_NAME).text
        assert Text == 'ייצוא'


    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Successfully Display Add Page In Department Page')
    def test_Validate_Add_Department_from_admin(self):
        driver = self.driver
        user = Department_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Add_button()
        Text = self.driver.find_element(By.XPATH, Locators_Dep.Add_Name).text
        assert Text == 'הוספה'

    @pytest.mark.sanity
    @allure.description('Successfully Display Admin Department page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
    def test_Validate_Display_Admin_Department_page_using_Logo(self):
        driver = self.driver
        home = Department_Page(driver)
        home.click_User_Menu_Option()
        assert self.driver.title == "מחלקות - trado"

    @pytest.mark.sanity
    @allure.description('Successfully Hide The Department Sidebar to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_DashBord_Display(self):
        driver = self.driver
        dashBord = Department_Page(driver)
        dashBord.click_User_Menu_Option()
        dashBord.click_Department_From_sideBar()
        assert self.driver.title == 'מחלקות - trado'

    @pytest.mark.sanity
    @allure.description('Successfully search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate__Search_existing_product_By_Using_search_Button(self):
        driver = self.driver
        Search = Department_Page(driver)
        Search.click_User_Menu_Option()
        Search.Enter_Search_product("wert")
        Utils(driver).assertion(Locators_Dep.Title, self.driver.title)

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Add_Department_from_admin(self):
        driver = self.driver
        Dep = Department_Page(driver)
        Dep.click_User_Menu_Option()
        Dep.click_Kebab_button()
        Dep.click_Add_button()
        assert self.driver.title == 'מחלקות - trado'


    @pytest.mark.sanity
    @allure.description('Successfully Take all The Amount Of Product')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Department_Amount_Display(self):
        driver = self.driver
        Dep = Department_Page(driver)
        Dep.click_User_Menu_Option()
        Dep. click_Drop_down_icon()
        Text = self.driver.find_element(By.XPATH,Locators_Dep.TOTAL_PRODUCTS).text
        assert Text == "סה״כ: 31 שורות"

    @pytest.mark.sanity
    @allure.description('Successfully ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Add_Department_from_admin(self):
        driver = self.driver
        Dep = Department_Page(driver)
        Dep.click_User_Menu_Option()
        Dep.click_Kebab_button()
        Dep.click_Add_button()
        assert self.driver.title == 'מחלקות - trado'
    @pytest.mark.sanity
    @allure.description('Invalid search for Non Existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Validate_login_and_Search_existing_product_By_Using_Restaurant_and_Cocktail_field(self):
        driver = self.driver
        Search = Department_Page(driver)
        Search.click_User_Menu_Option()
        Search.Enter_Search_product("Milk")
        Utils(driver).assertion(Locators_Dep.Title, self.driver.title)
    @pytest.mark.sanity
    @allure.description('Successfully Add Product')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Add_Department_to_admin(self):
        driver = self.driver
        user = Department_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_ADD_button()
        Text = self.driver.find_element(By.XPATH, Locators_Dep.DEPARTMENT_1).text
        assert Text == ''










