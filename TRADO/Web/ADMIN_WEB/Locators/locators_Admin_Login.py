class Locators_Login:
    TITLE1 = "דשבורד - trado"
    TITLE2 = "Dashboard - trado"
    ERROR_TEXT = "Please fill out this field"
    NO_SUCH_USER_TEXT_XPATH = "//div[contains(text(),'no such user')]"
    FAILED_TO_LOGIN = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]"
    FILL_IN_PATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/div[1]"
    LANGUAGE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]"
    PHONEBOX_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    SEND_ME_CODE_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"
    CODE_INPUT_BOX_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]"
    CONNECT_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]"
    REMEMBER_ME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[2]"
    TRADO_STORE_MANAGEMENT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
    DANI_MEMETIKIM_STORE_MANAGEMENT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"
    DASHBORD_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[1]/span[2]"
    LOGOUT_TEXT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/span[2]/a[1]"
    CURRENT_URL = "https://qa-admin.trado.co.il/#/login"
    STORENAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]"
    FILL_OUT_ERROR = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/div[1]"


class Locators_LogOut:
    LOGOUT_TEXT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/span[2]/a[1]"
