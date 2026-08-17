# tests/ui/test_login_ui.py
import pytest
from page_objects.login_page import LoginPage

@pytest.mark.ui
class TestLoginUI:
    
    def test_customer_ui_login(self, page, customer_credentials):
        """Verify a standard customer lands on the My Account page."""
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(
            email=customer_credentials["email"],
            password=customer_credentials["password"]
        )
        
        # Customers should see "My account"
        assert login_page.is_login_successful(expected_header="My account")

    def test_admin_ui_login(self, page, admin_credentials):
        """Verify an admin lands on the Dashboard."""
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(
            email=admin_credentials["email"],
            password=admin_credentials["password"]
        )
        
        # Admins should see the sales dashboard
        assert login_page.is_login_successful(expected_header="Sales over the years")

    def test_invalid_ui_login(self, page):
        """Verify invalid credentials show an error message."""
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("wrong@email.com", "badpass")
        
        error_msg = login_page.get_error_message()
        assert "Invalid email or password" in error_msg