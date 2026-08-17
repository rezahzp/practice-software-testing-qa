from faker import Faker

fake = Faker()

def generate_random_user() -> dict:
    """Generates dynamic, realistic user registration data."""
    
    # Create a completely unique string for this specific test run
    unique_id = fake.uuid4().split('-')[0]
    
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": f"test_{unique_id}@practicesoftwaretesting.com",
        
        # FIX: Combine a strong base with our unique ID to guarantee it passes the data leak check
        "password": f"SuperSecure_{unique_id}!?", 
        
        "phone": "0987654321",
        "dob": "1990-01-01",
        "address": {
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country(),
            "postcode": fake.postcode()
        }
    }