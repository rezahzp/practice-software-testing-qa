-- QA Script: User Management & Test Data Cleanup

-- 1. Find all Admin users in the system
SELECT id, first_name, last_name, email 
FROM users 
WHERE roles = 'admin';

-- 2. Find recently registered users (Useful for checking E2E test results)
SELECT id, first_name, last_name, email, created_at 
FROM users 
ORDER BY created_at DESC 
LIMIT 10;

-- 3. TEARDOWN: Delete all automation-generated test users to reset the environment
-- (Our Python Faker script generates emails starting with 'test_')
DELETE FROM users 
WHERE email LIKE 'test_%@practicesoftwaretesting.com';