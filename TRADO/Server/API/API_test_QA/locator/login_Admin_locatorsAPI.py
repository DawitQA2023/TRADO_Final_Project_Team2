class Login_Locators_Admin_API:
    url_login = 'https://qa-api.trado.co.il/api/admin-user/logincode'
    Valid_phone = {"phone": "1951111111", "code": 1234, "rememberMe": "true"}
    Invalid_phone1 = {"phone": "1236547895", "code": 5412652456, "rememberMe": "true"}
    Null_input_phone = {"phone": "", "code": 5412652456, "rememberMe": "true"}
    Null_password = {"phone": "195111111", "code": "", "rememberMe": "true"}
    Null_password_phone = {"phone": "", "code": "", "rememberMe": "true"}