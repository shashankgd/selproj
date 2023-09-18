from src.locators.locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.facebook.com/login"  # Assuming this is your login page's URL

    def load(self):
        """Navigate to the login page."""
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*LoginLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*LoginLocators.SUBMIT).click()
