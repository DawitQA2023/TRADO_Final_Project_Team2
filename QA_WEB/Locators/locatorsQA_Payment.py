class Locators_Payment:
    PAYMENT_CHANGE_LANGUAGE_XPATH = "/html/body/div/div/div[1]/div/span"
    PAYMENT_TITLE_XPATH = "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/h1"
    SELECT_ITEM_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[5]/div[1]/div[2]/div[1]"
    PLUS_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/i[1]"
    PAYMENT_BUTTON_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]"
    PAYMENT_PAGE_URL = "https://qa.trado.co.il/checkout"
    SELECT_PRODUCT_SECTION_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]"

    # FOR personal account path
    BUSINESS_NAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[1]/div[1]/input[1]"
    BN_NUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[1]/div[2]/input[1]"
    EMAIL_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[1]/div[3]/input[1]"
    CITY_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[2]/div[1]/input[1]"
    STREET_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[2]/div[2]/input[1]"
    HOUSENUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[2]/div[3]/input[1]"
    ENTRANCE_NUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[2]/div[4]/input[1]"
    FLOOR_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[2]/div[5]/input[1]"

    # FOR sending address path
    SHIPPING_CITY_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[1]/div[1]/input[1]"
    SHIPPING_STREET_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[1]/div[2]/input[1]"
    SHIPPING_HOUSENUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[1]/div[3]/input[1]"
    SHIPPING_ENTRANCE_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[1]/div[4]/input[1]"
    SHIPPING_FLOOR_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[1]/div[5]/input[1]"
    SHIPPING_CONTACT_NAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[2]/div[1]/input[1]"
    SHIPPING_FIRST_NAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[2]/div[2]/input[1]"
    SHIPPING_LAST_NAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[2]/div[3]/input[1]"
    SHIPPING_PHONE_NUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[2]/div[4]/input[1]"
    COMPLETE_PURCHASE_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[3]/div[3]/button[1]/input[1]"
    #############################################################################################################################

    # payment page
    B2B_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div[3]/div[1]/label[4]/div[1]"
    PAYMENT_BN_NUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/section[1]/div[1]/input[1]"
    CUSTOMERID_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/section[1]/div[1]/input[1]"
    CONFIRM_TRANSFER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]"
    PAY_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div[3]/button[1]"

    ####### NEW CAR ORDER
    CARD_NUMBER_XPATH = "/html/body/form/div[3]/fieldset/div[1]/input"
    ID_NUMBER = "/html/body/form/div[3]/fieldset/div[2]/input"
    MONTH_XPATH = "/html/body/form/div[3]/fieldset/div[3]/div[1]/select"
    YEAR_XPATH = ""
    CVV_XPATH = "/html/body/form/div[3]/fieldset/div[4]/input"
    PAYMENTXPATH = "/html/body/form/div[3]/input"
    CLOSE_BY_X_XPATH = "/html/body/div[1]/div/div[4]/div/span/i"

