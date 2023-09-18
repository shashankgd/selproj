from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    SUBMIT = (By.NAME, "login")
