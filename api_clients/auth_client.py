import requests
from api_clients.base_client import BaseClient

class AuthClient(BaseClient):
    """
    Client for interacting with Authentication-related API endpoints.
    """
    
    def __init__(self):
        super().__init__()
        self.login_endpoint = "users/login"

    def login(self, email: str, password: str) -> requests.Response:
        """
        Attempts to authenticate a user.
        Notice we return the Response object so tests can assert on status codes (e.g. 401 vs 200).
        """
        payload = {
            "email": email,
            "password": password
        }
        return self.request("POST", self.login_endpoint, json=payload)