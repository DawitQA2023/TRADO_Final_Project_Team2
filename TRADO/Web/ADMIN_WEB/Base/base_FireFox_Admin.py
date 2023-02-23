import pytest
from selenium import webdriver


class Base_FireFox:
    driver = None

    @pytest.fixture(autouse=True)
    def set_up_Firefox(self):

        print("Initiating Chrome driver")
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-admin.trado.co.il/")
        print("-----------------------------------------")
        print("Tests is started")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
