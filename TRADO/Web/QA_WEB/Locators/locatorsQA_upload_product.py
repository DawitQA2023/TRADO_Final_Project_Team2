class Locators_Upload_New_Product:
    # CSS:
    ADD_PRODUCT_PAGE = 'div[class="addProduct_page"]'
    NEW_PRODUCT_FIELDS = 'input[class="add_product_page_form_item"]'
    NEW_PRODUCT_FIELDS2 = '/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/div[1]/div[1]'
    ADD_NEW_PRODUCT_BUTTON = 'input[class="form_submitBtn"]'
    ADD_NEW_PRODUCT_SECTION = 'a[class="verticalMenu_addProduct"]'
    IMAGE = "//input[@id='files']"
    # Xpath:
    CHECKBOX = '//div[1]/div[2]/div[3]/div[1]/input[1]'
    UNIT_AND_WEIGHT = '//div[1]/div[2]/div[3]/div[1]/span'
    PLUS_BUTTON = '//div[3]/div[1]/div[1]/div[1]/span[1]'
    MINUS_BUTTON = '//div[3]/div[1]/div[1]/div[1]/span[2]'
    AMOUNT_OF_DAYS = '//div[1]/input[1]'

    # Messages
    STORE_VALIDATION_FAILED = 'div[class="form_message"]'
    FILL_THE_FIELD = "//form[1]/div[2]/div/div/div/div"
    ERROR_FIELD_IS_EMPTY = 'div[class="form_note "]'


    # ---------------------------------CSS SELECTOR XPATH -------------------------------------------------------
    UPLOAD_CSS = "div:nth-child(1) div.modal_modalWrapper.false.modal_open div.modal_modal.modal_add_product_modal.add_product_modal div.modal_content > div.addProduct_page"



