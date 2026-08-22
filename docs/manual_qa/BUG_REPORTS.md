# Defect Tracking: ToolShop

This document serves as the repository for formally logged defects, ensuring clear communication between QA and Engineering teams.

---

## BUG-001: User Registration API rejects valid flat address payload

**Status:** Open
**Severity:** High (Blocks user registration via standard REST clients)
**Priority:** High
**Environment:** Local Docker (Sprint 5)

### Description
The `POST /users/register` endpoint returns a `422 Unprocessable Content` error when a standard flat string is provided for the `address` field. The API validation explicitly demands an array/object, which may cause integration failures for frontend clients sending standard form data.

### Steps to Reproduce
1. Send a `POST` request to `http://localhost:8091/users/register`.
2. Provide a standard JSON payload with a flat location field:
   ```json
   {
     "first_name": "Regina",
     "last_name": "Morgan",
     "email": "test@practicesoftwaretesting.com",
     "password": "SuperSecure_1234!?",
     "address": "123 Main St, Austin, TX"
   }
   Expected Result
The API returns 201 Created and successfully persists the user, parsing the flat string into the database.

Actual Result
The API returns 422 Unprocessable Content with the following validation error:

JSON
{
  "address": ["The address field must be an array."]
}