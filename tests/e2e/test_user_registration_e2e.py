import pytest
from api_clients.base_client import BaseClient
from core.db_client import db
from data.factories import generate_random_user

@pytest.mark.e2e
class TestUserRegistrationE2E:

    def test_user_registration_persists_in_database(self):
        """
        E2E Flow:
        1. Generate dynamic user data.
        2. Send POST request to API to register user.
        3. Verify API returns 201 Created.
        4. Query the database to ensure the user exists.
        5. Verify security: Ensure the password is encrypted in the DB.
        """
        # 1. Arrange: Generate Data
        api = BaseClient()
        new_user = generate_random_user()
        
        # 2. Act: Register via API
        response = api.request("POST", "users/register", json=new_user)
        
        # 3. Assert API layer
        assert response.status_code == 201, f"Failed to register: {response.text}"
        
        # 4. Act: Query the Database layer
        # Notice we use parameterized queries (:email) to prevent SQL injection
        db_user = db.fetch_one(
            "SELECT * FROM users WHERE email = :email", 
            {"email": new_user["email"]}
        )
        
        # 5. Assert Database layer
        assert db_user is not None, "User was not found in the database!"
        assert db_user["first_name"] == new_user["first_name"]
        assert db_user["last_name"] == new_user["last_name"]
        
        # Security Assertion: The database password should NOT equal the plain text password
        assert db_user["password"] != new_user["password"], "SECURITY VULNERABILITY: Password saved in plain text!"