import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from TRADO.Web.ADMIN_WEB.Locators.locators_Admin_Dashbord import Locators_DashBord


class DashBord_Page(Locators_DashBord):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step
    @allure.description('Click dashboard Option')
    def click_dashboard_From_sideBar(self):
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators_DashBord.DASHBORD_SIDEBAR_XPATH2).click()
        self.wait.until(EC.url_to_be(self.driver.current_url))
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Click dashboard Option')
    def Assert_TageName(self, Path):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element(By.TAG_NAME,Path).text
        return element



