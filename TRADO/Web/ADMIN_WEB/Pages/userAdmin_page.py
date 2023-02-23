import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.ADMIN_WEB.Locators.locators_Admin_User import Locators_User
from TRADO.Web.ADMIN_WEB.Utils.utils_Admin import Utils

class User_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    @allure.step
    @allure.description('Click User Menu Option ')
    def click_User_Menu_Option(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,Locators_User.USER_MENU_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(10)
        time.sleep(3)

    @allure.step
    @allure.description('Click LANGUAGE frome admin on user section ')
    def click_LANGUAGE(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.LANGUEGE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('Click Kabab button ')
    def click_Kebab_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.KEBAB_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click Add button ')
    def click_Add_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click Export button ')
    def click_Export_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.EXPORT_BUTTON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click Add by brand button ')
    def click_Add_by_Brand_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_BY_BRAND_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click Import button ')
    def click_Import_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.IMPORT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click Import button ')
    def click_Tampet_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.TAMPLET_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Clear and insert data to FirstName input')
    def enter_FirstName(self, FirstName):
        time.sleep(1)
        FirstName_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.FIRST_NAME_XPATH)))
        FirstName_Input.clear()
        FirstName_Input.send_keys(FirstName)
        Utils(self.driver).assertion(FirstName, FirstName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to LastName input')
    def enter_LastName(self, LastName):
        time.sleep(1)
        LastName_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.LAST_NAME_XPATH)))
        LastName_Input.clear()
        LastName_Input.send_keys(LastName)
        Utils(self.driver).assertion(LastName, LastName_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to EMAIL input')
    def enter_email(self, email):
        time.sleep(1)
        email_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.EMAIL_PATH)))
        email_Input.clear()
        email_Input.send_keys(email)
        Utils(self.driver).assertion(email, email_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert PHONE data to input')
    def enter_phone(self, phone):
        time.sleep(1)
        phone_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.PHONE_XPATH)))
        phone_Input.clear()
        phone_Input.send_keys(phone)
        Utils(self.driver).assertion(phone, phone_Input.get_attribute('value'))


    @allure.step
    @allure.description('Clear and insert ADITIONAL PHONE data to input')
    def enter_aditional_phone(self, adi_phone):
        time.sleep(1)
        adi_phone_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADITIONAL_PHONE_XPATH)))
        adi_phone_Input.clear()
        adi_phone_Input.send_keys(adi_phone)
        Utils(self.driver).assertion(adi_phone, adi_phone_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert PASSWORD data to input')
    def enter_password(self, password):
        time.sleep(1)
        password_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.PASSWORD_XPATH)))
        password_Input.clear()
        password_Input.send_keys(password)
        Utils(self.driver).assertion(password, password_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click TEAM TWO from admin on user button to TO UPDATE ')
    def click_team_two_to_update(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.TEAM_TWO_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('CLICK  STOREID FIELD  data to input')
    def click_storeid_field(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.STOREIDS_FIELD_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Clear and insert SELECT UPDETES TEAM data to input')
    def click_select_teams(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.SELECT_TEAM_TWO_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click UPDATE from admin on user button ')
    def click_update(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.UPDATE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click CHECKING NEXT PAGE buttons from admin on user button ')
    def click_next_page_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.NEXT_PAGE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)
        time.sleep(2)

    @allure.step
    @allure.description('Click CHECKING BACKWAR buttons from admin on user button ')
    def click_backward_page_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.BACKWARD_PAGE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Clear and insert PASSWORD data to input')
    def enter_city(self, city):
        time.sleep(1)
        city_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.CITY_XPATH)))
        city_Input.clear()
        city_Input.send_keys(city)
        Utils(self.driver).assertion(city, city_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert PASSWORD data to input')
    def enter_storeid_pw(self, storeid):
        time.sleep(1)
        storeidp_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.STORID_XPATH)))
        storeidp_Input.clear()
        storeidp_Input.send_keys(storeid)


    @allure.step
    @allure.description('Clear and insert BUILIDING NUMBER data to input')
    def enter_building_no(self, build):
        time.sleep(1)
        building_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.BUILDING_XPATH)))
        building_Input.clear()
        building_Input.send_keys(build)
        Utils(self.driver).assertion(build, building_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert APARTMENT NUMBER data to input')
    def enter_apartment_no(self, apartmen):
        time.sleep(1)
        apartment_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.APARTMENT_XPATH)))
        apartment_Input.clear()
        apartment_Input.send_keys(apartmen)
        Utils(self.driver).assertion(apartmen, apartment_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert FLOOR NUMBER data to input')
    def enter_floor_no(self, floor):
        time.sleep(1)
        flore_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.FLOOR_XPATH)))
        flore_Input.clear()
        flore_Input.send_keys(floor)
        Utils(self.driver).assertion(floor, flore_Input.get_attribute('value'))


    @allure.step
    @allure.description('Clear and insert COMMENT data to input')
    def enter_comments(self, comment):
        time.sleep(1)
        commnt_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.COMMENT_XPATH)))
        commnt_Input.clear()
        commnt_Input.send_keys(comment)
        Utils(self.driver).assertion(comment, commnt_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert ACCOUNTOWNER NUMBER data to input')
    def enter_account_owner(self, accountOwner):
        time.sleep(1)
        accountown = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ACCOUNTOWNER_XPATH)))
        accountown.clear()
        accountown.send_keys(accountOwner)
        Utils(self.driver).assertion(accountOwner, accountown.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert ACCOUNT NUMBER data to input')
    def enter_account_no(self, accountNo):
        time.sleep(1)
        accountnumber_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ACCOUNTNUMBER_XPATH)))
        accountnumber_Input.clear()
        accountnumber_Input.send_keys(accountNo)
        Utils(self.driver).assertion(accountNo, accountnumber_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert BRANCH NUMBER data to input')
    def enter_branch_no(self, branch):
        time.sleep(1)
        branchnum_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.BRANCH_NUMBER_XPATH)))
        branchnum_Input.clear()
        branchnum_Input.send_keys(branch)
        Utils(self.driver).assertion(branch, branchnum_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click CREDICSACCOUWNT BUTTON from admin on user button ')
    def click_credicsaccount(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.CREDICSACCOUNT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click marketlist BUTTON from admin on user button ')
    def click_marketlist(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.MARKETINGLIST_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ETRADOAPROVE BUTTON from admin on user button ')
    def click_eTradoAproved(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ETRADOAPROVED_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Clear and insert INCOME NUMBER data to input')
    def enter_income(self, income):
        time.sleep(1)
        incomes_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.INCOME_XPATH)))
        incomes_Input.clear()
        incomes_Input.send_keys(income)
        Utils(self.driver).assertion(income, incomes_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert OUTCOME NUMBER data to input')
    def enter_outcome(self, outcomes):
        time.sleep(1)
        outcome_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.OUTCOME_XPATH)))
        outcome_Input.clear()
        outcome_Input.send_keys(outcomes)
        Utils(self.driver).assertion(outcomes, outcome_Input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert USERID NUMBER data to input')
    def enter_userIdNo(self, userId):
        time.sleep(1)
        userid_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.USERID_XPATH)))
        userid_Input.clear()
        userid_Input.send_keys(userId)
        Utils(self.driver).assertion(userId, userid_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click TAKANON BUTTON from admin on user button ')
    def click_takanon_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.TAKANON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)
        time.sleep(5)

    @allure.step
    @allure.description('Click ACTIVE BUTTON from admin on user button ')
    def click_active_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ACTIVE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click UPDATE from admin on user button ')
    def click_update(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.UPDATE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click UPDATE from admin on user button ')
    def click_close_x(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.CLOSE_BY_X_ICONE).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)


    def assert_message(self, error):
        self._wait_until_element_is_visible(error)
        return self.driver.find_element(By.XPATH, error).text

    def error_email_xpath(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.EMAIL_ERROR_XPATH)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    def error_fphone_xpath(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ERROR_FIRST_PHONE_XPATH)
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    ####################################################################################################################
    @allure.step
    @allure.description('ClicK ADD butto TO RIGHT FNAME from admin on user categores ')
    def enter_add_user(self, adduser):
        useradd_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_FNAME_XPATH)))
        useradd_Input.clear()
        useradd_Input.send_keys(adduser)
        Utils(self.driver).assertion(adduser, useradd_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write LNAME from admin on user categores ')
    def enter_add_lname(self, lname):
        lnamee_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_LNAME_XPATH)))
        lnamee_Input.clear()
        lnamee_Input.send_keys(lname)
        Utils(self.driver).assertion(lname, lnamee_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER EMAIL from admin on user categores ')
    def enter_add_uemail(self, userEmail):
        uemail_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_EMAIL_XPATH)))
        uemail_Input.clear()
        uemail_Input.send_keys(userEmail)
        Utils(self.driver).assertion(userEmail, uemail_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER PHONE from admin on user categores ')
    def enter_add_uphone(self, userPhone):
        uphone_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_PHONE_XPATH)))
        uphone_Input.clear()
        uphone_Input.send_keys(userPhone)
        Utils(self.driver).assertion(userPhone, uphone_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER RESERVE PHONE from admin on user categores ')
    def enter_add_uphone2(self, userPhone2):
        userphone2_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_PHONE2_XPATH)))
        userphone2_Input.clear()
        userphone2_Input.send_keys(userPhone2)
        Utils(self.driver).assertion(userPhone2, userphone2_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER PASSSWORD from admin on user categores ')
    def enter_add_upasswor(self, userpasswor):
        userpw_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_PASSWORD_XPATH)))
        userpw_Input.clear()
        userpw_Input.send_keys(userpasswor)
        Utils(self.driver).assertion(userpasswor, userpw_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER STOREID from admin on user categores ')
    def enter_add_ustoreid(self, storeid):
        storidd_Input = self.wait.until( EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_PASSWORD_XPATH)))
        storidd_Input.clear()
        storidd_Input.send_keys(storeid)
        Utils(self.driver).assertion(storeid, storidd_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER CITY from admin on user categores ')
    def enter_add_ucityy(self, ucity):
        citys_Input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators_User.ADD_USER_CITY_XPATH)))
        citys_Input.clear()
        citys_Input.send_keys(ucity)
        Utils(self.driver).assertion(ucity, citys_Input.get_attribute('value'))

    @allure.step
    @allure.description('Click ADD butto to write USER CREDICSACCOUNT from admin on user categores ')
    def click_add_ucredicsaccount(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_USER_CREDICSACCOUNT_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ADD butto to write USER MARKETLIST from admin on user categores ')
    def click_add_umarketinglist(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_USER_MARKETLIST_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ADD butto to write USER ETRADOAPROVE from admin on user categores ')
    def click_add_uetradoaprove(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_USER_ETRADOAPROVE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ADD butto to write USER TAKANON from admin on user categores ')
    def click_add_utekanon(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_USER_TAKANON_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ADD butto to write USER ADD from admin on user categores ')
    def click_add_uadd(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_USER_ADD_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ADD butto to write USER GROUP2 xpath  from admin on user categores ')
    def click_add_group2(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.GROUP2GMAIL_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)

    @allure.step
    @allure.description('Click ADD butto to write USER ACTIVE xpath  from admin on user categores ')
    def click_add_user_activate(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locators_User.ADD_USER_ACTIVE_XPATH).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(15)



