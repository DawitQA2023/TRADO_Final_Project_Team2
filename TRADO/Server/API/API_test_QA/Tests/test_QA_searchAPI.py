import allure
import pytest
import requests
from API_test_QA.locator.Search_QA_locatorsAPI import Locators_Search


class Test_Trado_QA_Login(Locators_Search):
    @allure.description('Search existing products using search box')
    @pytest.mark.sanity
    def test_search_exist_product(self):
        url = Locators_Search.URL_SEARCH
        data = Locators_Search.EXIST_PRODUCT
        Req = requests.post(url, json=data)
        assert Req.status_code == 200
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Search non existing products using search box')
    @pytest.mark.sanity
    def test_search_non_exist_product(self):
        url = Locators_Search.URL_SEARCH
        data = Locators_Search.NON_EXiST_PRODUCT
        Req = requests.post(url, json=data)
        assert Req.status_code == 201
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Search  products by numbers using search box')
    @pytest.mark.sanity
    def test_search_product_by_number(self):
        url = Locators_Search.URL_SEARCH
        data = Locators_Search.PRODUCT_BY_NUMBER
        Req = requests.post(url, json=data)
        assert Req.status_code == 300
        assert Req.elapsed.total_seconds() < 5

    @allure.description('Search  products using null value  using search box')
    @pytest.mark.sanity
    def test_search_product_by_null_input(self):
        url = Locators_Search.URL_SEARCH
        data = Locators_Search.NULL_PRODUCT
        Req = requests.post(url, json=data)
        assert Req.status_code == 400
        assert Req.elapsed.total_seconds() < 5