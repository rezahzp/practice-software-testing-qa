# page_objects/login_page.py
from page_objects.base_page import BasePage
from core.config import settings
from playwright.sync_api import expect

class LoginPage(BasePage):
    """
    Page Object representing the Login screen.
    """
    
    # Locators (Tag-agnostic, relying purely on the data-test attribute)
    EMAIL_INPUT = "[data-test='email']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-submit']"
    ERROR_ALERT = "[data-test='login-error']"
    ACCOUNT_HEADER = "[data-test='page-title']"

    def __init__(self, page):
        super().__init__(page)
        self.url = f"{settings.base_ui_url.rstrip('/')}/auth/login"

    def goto(self):
        self.navigate(self.url)

    def login(self, email: str, password: str):
        """Executes the login workflow."""
        self.fill_text(self.EMAIL_INPUT, email)
        self.fill_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Retrieves the text of the error alert."""
        self.page.locator(self.ERROR_ALERT).wait_for(state="visible")
        return self.page.locator(self.ERROR_ALERT).inner_text()
        
    def is_login_successful(self, expected_header: str = "My account") -> bool:
        """
        Checks if we landed on the correct page after login.
        Defaults to 'My account' for regular users.
        """
        expect(self.page.locator(self.ACCOUNT_HEADER)).to_have_text(
            expected_header, ignore_case=True, timeout=10000
        )
        return True   