from selenium.webdriver.common.by import By


class LoginFormLocators:
    LOGIN_VIEW = (By.ID, "loginView")
    LOGIN_FORM = (By.ID, "homeRealmDiscoveryView")
    EMAIL_LABEL = (
    By.XPATH, f"//div[@id='{LOGIN_FORM}' and not(contains(@style,'display:none')) ]//label[contains(text(),'Email')]")
    EMAIL_TEXT_FIELD = (By.ID,"homeRealmDiscoveryInput")
    LOG_IN_BUTTON = (By.ID, "homeRealmDiscoverySubmit")
    INVALID_EMAIL_ERROR = (By.ID,"homeRealmDiscoveryError")
    PASSWORD_FIELD = (By.ID,"loginPasswordInput")
    CHANGE_EMAIL_LINK = (By.ID, "changeEmailLink")
    SUBMIT_BUTTON =(By.ID,"loginSubmit")
    USER_PASSWORD_ERROR = (By.ID, "usernamePasswordLoginError")
    SIGN_UP_LINK=(By.ID, 'signupFullNameInput')
