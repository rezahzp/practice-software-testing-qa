import pytest
from api_clients.auth_client import AuthClient
from core.config import settings

@pytest.fixture(scope="session")
def auth_client():
    """
    Provides a reusable AuthClient instance across the entire test session.
    """
    return AuthClient()

@pytest.fixture(scope="session")
def admin_credentials():
    """Returns the admin credentials from configuration."""
    return {
        "email": settings.admin_email,
        "password": settings.admin_password
    }

# @pytest.fixture(scope="session")
# def browser_type_launch_args(browser_type_launch_args):
#     """
#     Tells Playwright to use the local Google Chrome channel instead of 
#     downloading its own custom Chromium binary.
#     """
#     return {
#         **browser_type_launch_args,
#         "channel": "chrome",  
#         "headless": settings.headless
#     }

@pytest.fixture(scope="session")
def customer_credentials():
    """Returns the standard customer credentials from configuration."""
    return {
        "email": settings.customer_email,
        "password": settings.customer_password
    }