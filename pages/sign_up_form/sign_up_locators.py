from selenium.webdriver.common.by import By


class SignUpFormLocators:
    FIRST_NAME_LAST_NAME = (By.ID, "signupFullNameInput")
    SIGN_UP_EMAIL_FIELD = (By.ID,"signupEmailInput")
    SING_UP_PASS_FIELD = (By.ID, "signupPasswordInput")
    ACCEPT_AGREEMENT_CHECK_BOX = (By.ID,"privacyPolicyInput")
    SIGN_UP_SUBMIT_BUTTON = (By.ID,"signupSubmit")
    SIGN_UP_ERROR = (By.ID,"signupError")
    PARAGRAPHS_OF_PASS_DESC = (By.XPATH,"//ul/li/")
