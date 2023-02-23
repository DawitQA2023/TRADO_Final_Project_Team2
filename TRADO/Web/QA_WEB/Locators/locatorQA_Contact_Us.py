class Locators_Contact_Us:
    CONTACT_TITLE = "/html/body/div/div/div[2]/div[2]/div/div[1]/h4"
    CONTACT_US_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[4]"
    FIRST_NAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/span[1]/input[1]"
    LAST_NAME_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/span[1]/input[1]"
    EMAIL_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/span[1]/input[1]"
    PHONE_NUMBER_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/span[1]/input[1]"
    CONTENT_REFERRAL_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[5]/textarea[1]"
    SEND_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/input[1]"

    # error mesage path
    SUCCESS_TEXT = "//div[contains(text(),'הפרטים נקלטו בהצלחה')]"
    ERROR_FIRST_NAME = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]"
    ERROR_LAST_NAME = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]"
    ERROR_EMAIL = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]"
    ERROR_PHONE = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]"
    ERROR_CONTACT_REFERRAL = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[5]/div[1]"


    # ---------------------------------CSS SELECTOR XPATH -------------------------------------------------------
    CONTACTUS_CSS = "div:nth-child(1) div:nth-child(1) div.pages_pages div.pages_children.false:nth-child(3) > div:nth-child(1)"
