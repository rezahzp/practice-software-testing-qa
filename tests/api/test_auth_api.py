import pytest
from jsonschema import validate
from data.schemas.auth_schemas import LOGIN_SUCCESS_SCHEMA, LOGIN_ERROR_SCHEMA

@pytest.mark.api
class TestAuthAPI:
    """Test suite for Authentication API endpoints."""

    def test_successful_login(self, auth_client, admin_credentials):
        # Act
        response = auth_client.login(
            email=admin_credentials["email"],
            password=admin_credentials["password"]
        )
        
        # Assert Status
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Assert Contract (Throws ValidationError if the structure is wrong)
        validate(instance=response.json(), schema=LOGIN_SUCCESS_SCHEMA)

    def test_invalid_login_returns_401(self, auth_client):
        # Act
        response = auth_client.login(
            email="nonexistent@practicesoftwaretesting.com",
            password="wrongpassword"
        )
        
        # Assert Status
        assert response.status_code == 401, f"Expected 401, got {response.status_code}"
        
        # Assert Contract
        validate(instance=response.json(), schema=LOGIN_ERROR_SCHEMA)