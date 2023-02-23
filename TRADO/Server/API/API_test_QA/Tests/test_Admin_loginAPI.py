import allure
import pytest
import requests
from API_test_QA.locator.login_Admin_locatorsAPI import Login_Locators_Admin_API


class Test_Trado_Admin_Login(Login_Locators_Admin_API):
    @allure.description('Admin correctly using Valid Phone number')
    @pytest.mark.sanity
    def test_login_correctly(self):
        url = Login_Locators_Admin_API.url_login
        data = Login_Locators_Admin_API.Valid_phone
        Req = requests.post(url, json=data)
        assert Req.status_code == 200
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Admin when Phone incorrectly')
    def test_login_with_incorrectly_PHONE(self):
        url = Login_Locators_Admin_API.url_login
        data = Login_Locators_Admin_API.Invalid_phone1
        Req = requests.post(url, json=data)
        assert Req.status_code == 400
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Admin when phone is null')
    def test_login_with_null_phone(self):
        url = Login_Locators_Admin_API.url_login
        data = Login_Locators_Admin_API.Null_input_phone
        Req = requests.post(url, json=data)
        assert Req.status_code == 205
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Admin when password is null')
    def test_login_with_null_password(self):
        url = Login_Locators_Admin_API.url_login
        data = Login_Locators_Admin_API.Null_password
        Req = requests.post(url, json=data)
        assert Req.status_code == 300
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Admin when password and phone is null')
    def test_login_with_null_password(self):
        url = Login_Locators_Admin_API.url_login
        data = Login_Locators_Admin_API.Null_password
        Req = requests.post(url, json=data)
        assert Req.status_code == 201
        assert Req.elapsed.total_seconds() < 5

