import allure
import pytest
import requests
from API_test_QA.locator.SignUp_QA_locatorsAPI import SignUp_Locators


class Test_Login(SignUp_Locators):
    @allure.description('SignUp correctly using Valid Phone number and NbNumber')
    @pytest.mark.sanity
    def test_SignUp_phone_BnNumber_correctly(self):
        url = SignUp_Locators.URL_SIGN_UP
        data = SignUp_Locators.VALID_DATA
        Req = requests.post(url, json=data)
        assert Req.status_code == 200
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when password incorrectly')
    def test_SignUp_with_incorrectly_BnNumber(self):
        url = SignUp_Locators.URL_SIGN_UP
        data = SignUp_Locators.ICORRECT_NBNUMBER
        Req = requests.post(url, json=data)
        assert Req.status_code == 400
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName incorrectly')
    def test_SignUp_with_incorrectly_phone(self):
        url = SignUp_Locators.URL_SIGN_UP
        data = SignUp_Locators.INCORRECT_PHONE
        Req = requests.post(url, json=data)
        assert Req.status_code == 300
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName & password incorrectly')
    def test_SignUp_with_null_phone(self):
        url = SignUp_Locators.URL_SIGN_UP
        data = SignUp_Locators.NULL_PHONE
        Req = requests.post(url, json=data)
        assert Req.status_code == 400
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName & password are null')
    def test_SignUp_with_null_Phone_and_BnNumber(self):
        url = SignUp_Locators.URL_SIGN_UP
        data = SignUp_Locators.INCORRECT_PHONE_NBNUMBER
        Req = requests.post(url, json=data)
        assert Req.status_code == 203
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName & password are null')
    def test_SignUp_with_null_BnNumber(self):
        url = SignUp_Locators.URL_SIGN_UP
        data = SignUp_Locators.INCORRECT_PHONE_NBNUMBER
        Req = requests.post(url, json=data)
        assert Req.status_code == 203
        assert Req.elapsed.total_seconds() < 10
