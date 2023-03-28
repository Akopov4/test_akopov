from selenium.webdriver.common.by import By

class MyEventsLocators:
    MY_EVENTS_TOP_BAR = (By.XPATH, '//h1[contains(@class,"EventsDashboardTopbar")]')
    MY_PROFILE_BUTTON = (By.XPATH,'//a[contains(@class,"profile")]')
    LOG_OUT_BUTTON = (By.XPATH,'//div[contains(@class,"SuiButton") and text() ="Log Out"]/..')
