import allure
import pytest
import requests
from  API_test_QA.locator.login_QA_locatersAPI import Login_locaters_QA_api


class Test_Trado_Admin_Login(Login_locaters_QA_api):
    @allure.description('Login correctly using Valid Phone number')
    @pytest.mark.sanity
    def test_login_correct_phone(self):
        url = Login_locaters_QA_api.URL_LOGIN
        data = Login_locaters_QA_api.VALID_PHONE
        Req = requests.post(url, json=data)
        assert Req.status_code == 200
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Login correctly using Invalid Phone number')
    @pytest.mark.sanity
    def test_login_incorrect_phone(self):
        url = Login_locaters_QA_api.URL_LOGIN
        data = Login_locaters_QA_api.INVALID_PHONE
        Req = requests.post(url, json=data)
        assert Req.status_code == 201
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Login correctly using Null Phone number')
    @pytest.mark.sanity
    def test_login_null_phone(self):
        url = Login_locaters_QA_api.URL_LOGIN
        data = Login_locaters_QA_api.NULL_PHONE
        Req = requests.post(url, json=data)
        assert Req.status_code == 300
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Login correctly using Letters Phone number')
    @pytest.mark.sanity
    def test_login_correctly(self):
        url = Login_locaters_QA_api.URL_LOGIN
        data = Login_locaters_QA_api.LETTERS_VALUE_PHONE
        Req = requests.post(url, json=data)
        assert Req.status_code == 400
        assert Req.elapsed.total_seconds() < 5

