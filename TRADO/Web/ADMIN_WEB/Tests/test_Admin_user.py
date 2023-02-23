import allure
import pytest
from TRADO.Web.ADMIN_WEB.Utils.utils_Admin import Utils

from TRADO.Web.ADMIN_WEB.Pages.userAdmin_page import User_Page
from TRADO.Web.ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Chrome
from TRADO.Web.ADMIN_WEB.Pages.Pre_Requirment_page.Pre_Requirement_login import Pre_Requirement_Login_Firefox


@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Chrome_Valid_data_and_Trado_store')
class Test_User_Chrome(Pre_Requirement_Login_Chrome):
    @pytest.mark.sanity
    @allure.description('Successfully Login to admin trado and EXPORT files')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Export_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully IMPORT XLCEL file from admin user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_import_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Import_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully downlod(templet) XLCEL file from admin user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_templet_user_from_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Tampet_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully NEXT and BACKWARD page BUTTONS from admin user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_next_page_button(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_next_page_button()
        user.click_backward_page_button()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user with EMAIL NULL fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_with_allRequirement_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("0511111112")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("team2pas")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user with EMAIL NULL fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_without_Email_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("")
        user.enter_phone("0511111112")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("team2pas")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user with incorect PHONE fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_incorrect_first_phone_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("0511111")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("team2pas")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user without PHONE fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_without_first_phone_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("team2pas")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user  PHONE WITH LETTER fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_without_letter_phone_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("050101TEAM")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("team2pas")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user WITHOUT STOREID fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_without_storeid_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("0501010101")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user STOREID only ltters fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_storeid_onlyleter_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("0501010101")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("abcdefg")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user incorrect STOREID fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_storeid_incorrect_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("0501010101")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("a1")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to UPDATE DATA from admin user STOREID only number fields')
    @allure.severity(allure.severity_level.NORMAL)
    def test_storeid_onlynumber_update_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("teamtwo@gmail.co")
        user.enter_phone("0501010101")
        user.enter_aditional_phone("0500000000")
        user.enter_storeid_pw("12344444")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('close by "X" from UPDATE DATA page from admin user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_close_user_to_admin_ByX(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.click_close_x()

    ###################################################################################################################
    @pytest.mark.sanity
    @allure.description('Add users from admin user category')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Add_user_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("TEAME")
        user.enter_add_lname("TWO")
        user.enter_add_uemail("GROUP@GMAIL.COM")
        user.enter_add_uphone("0599999999")
        user.enter_add_uphone2("0588888888")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("str123")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to Add users from admin user category without first name')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Add_user_witout_fname_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("")
        user.enter_add_lname("TWO")
        user.enter_add_uemail("GROUP@GMAIL.COM")
        user.enter_add_uphone("0599999999")
        user.enter_add_uphone2("0588888888")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("str123")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to Add users from admin user category without last name')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Add_user_witout_fname_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("TEAME")
        user.enter_add_lname("")
        user.enter_add_uemail("GROUP@GMAIL.COM")
        user.enter_add_uphone("0599999999")
        user.enter_add_uphone2("0588888888")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("str123")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to Add users from admin user category without EMAIL')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Add_user_witout_email_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("TEAME")
        user.enter_add_lname("TWO")
        user.enter_add_uemail("")
        user.enter_add_uphone("0599999999")
        user.enter_add_uphone2("0588888888")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("str123")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to Add users from admin user category with incorrect phone')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Add_user_incorrect_phone_to_admin(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("TEAME")
        user.enter_add_lname("TWO")
        user.enter_add_uemail("group2@gmail.com")
        user.enter_add_uphone("0599")
        user.enter_add_uphone2("058")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("str1999923")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to Add users from admin user category without storeid')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Add_user_witout_storeid_to_admin_add(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("TEAME")
        user.enter_add_lname("TWO")
        user.enter_add_uemail("GROUP@GMAIL.COM")
        user.enter_add_uphone("0599999999")
        user.enter_add_uphone2("0588888888")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')

    @pytest.mark.sanity
    @allure.description('Trying to Add users from admin user category without requirements')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Add_user_without_requirements_to_admin_add(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_Kebab_button()
        user.click_Add_button()
        user.click_add_user_activate()
        user.enter_add_user("")
        user.enter_add_lname("")
        user.enter_add_uemail("")
        user.enter_add_uphone("")
        user.enter_add_uphone2("0588888888")
        user.enter_add_upasswor("teameT2")
        user.enter_add_ustoreid("str123344")
        user.enter_add_ucityy("jerusalem")
        user.click_add_ucredicsaccount()
        user.click_add_umarketinglist()
        user.click_add_uetradoaprove()
        user.click_add_utekanon()
        user.click_add_uadd()
        Utils(driver).assertion(driver.title, 'Users - trado')


###############################################################################################################

# this is for firefox
@pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
class Test_User_Firefox(Pre_Requirement_Login_Firefox):
    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures('Valid_Login_to_Admin_homePage_With_Firefox_Valid_data_and_Trado_store')
    def test_Validate_Export_user_from_admin_fire(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_Kebab_button()
        user.click_Export_button()
        Utils(driver).assertion(self.driver.title, "משתמשים - trado")

    @pytest.mark.sanity
    @allure.description('Successfully Logout to Admin website using valid data and Chrome')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Validate_Add_user_to_admin_byfire(self):
        driver = self.driver
        user = User_Page(driver)
        user.click_User_Menu_Option()
        user.click_LANGUAGE()
        user.click_team_two_to_update()
        user.enter_FirstName("Team")
        user.enter_LastName("Two")
        user.enter_email("Trado2@gmail.com")
        user.enter_phone("0511111112")
        user.enter_aditional_phone("0500000000")
        user.enter_password("")
        user.enter_storeid_pw("team2pas")
        user.enter_city("Telavive")
        user.enter_building_no("22")
        user.enter_apartment_no("4")
        user.enter_floor_no("7")
        user.enter_comments("suuuuuuuuuuu")
        user.enter_account_owner("Group2")
        user.enter_account_no("123")
        user.enter_branch_no("21")
        user.click_credicsaccount()
        user.enter_income("2000,0000")
        user.enter_outcome("10000")
        user.enter_userIdNo("35")
        user.click_marketlist()
        user.click_eTradoAproved()
        user.click_takanon_button()
        user.click_active_button()
        user.click_update()
        Utils(driver).assertion(driver.title, 'Users - trado')
