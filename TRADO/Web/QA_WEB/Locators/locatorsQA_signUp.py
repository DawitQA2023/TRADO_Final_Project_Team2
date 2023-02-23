class Locators_SignUp:
    TITLE1 = "trado"
    COCKTAIL_XPATH = '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]'
    RESTAURANT_XPATH = '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]'
    SAVE_BUTTON_XPATH = '//*[@id="root"]/div/div[4]/div/div/div/button'
    PERSONAL_AREA_TEXT_LINK_XPATH = "//font[contains(text(),'Personal Area')]"
    USER_AREA_TEXT_LINK_CLASSNAME = "header_userAreaLink"
    HELLO_GUEST_TEXT_LINK_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/a[1]"
    PERSON_IMAGE_LINK_XPATH = "//header/div[1]/div[1]/a[1]/img[1]"
    LEFT_OPEN_ICON_ARROW_XPATH = "//header/div[1]/div[1]/a[1]/span[2]/i[1]"
    SCREEN_TEXT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
    REGISTRATION_OPTION_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]"
    PHONE_BOX_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]"
    BN_NUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/input[1]"
    AGREE_TERM_BOX_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/span[1]/span[1]/i[1]"
    CONNECT_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]"
    LOGINCODE_SCREEN_TEXT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]/font[1]/font[1]"   # Just Making Sure We Know Each Other "רק מוודאים שאנחנו מכירים" #
    LOGIN_CODE_INPUT_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]"
    PERFORM_VERIFICATION_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]"
    FACEBOOK_LOGO_XPATH = '/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/button[1]'
    GOOGLE_LOGO_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]"
    TWITTER_LOGO_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/img[1]"
    X_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/span[1]"


    # ---------------------------------CSS SELECTOR XPATH -------------------------------------------------------
    SIGNUP_CSS = "body:nth-child(2) div:nth-child(1) div:nth-child(1) div.modal_modalWrapper.false.modal_open > div.modal_modal.modal_login_modal.login_modal"
