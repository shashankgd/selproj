from pytest_bdd import given, when, then, scenarios
from src.conftest import browser
from src.pages.loginpage import LoginPage


# Link the scenario in the feature file
scenarios('../features/')


# Define step for the starting point of the scenario
@given('the user is on the login page', target_fixture='login_page')
def login_page(browser):
    # Assuming you also have a 'load' method in your LoginPage to navigate to the login URL
    login_page = LoginPage(browser)
    login_page.load()
    return login_page


# Define step to enter credentials
@when('the user enters valid credentials')
def enter_valid_credentials(login_page):
    # For the sake of simplicity, I'm using hardcoded "test_user" and "password123"
    # In a real-world scenario, you might want to parameterize this data or fetch it from a data source
    login_page.enter_username("test123")
    login_page.enter_password("test1234")


# Define step to click the login button
@when('clicks the login button')
def click_login_button(login_page):
    login_page.click_submit()


# Define verification step after successful login
@then('the user should be logged in successfully')
def verify_logged_in(browser):
    # Here, you can verify if the user has been successfully logged in
    # This can be done by checking if a specific element is present, the URL has changed, etc.
    print(browser.current_url)
    assert "facebook.com/" in browser.current_url, "Failed to log in"
