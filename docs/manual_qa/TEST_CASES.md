# Manual Test Cases: ToolShop

This document serves as the system of record for manual functional testing and exploratory charters. These test cases act as the blueprint for our automated E2E and UI test suites.

---

## Format 1: BDD (Behavior-Driven Development)
*Used for Agile user stories, easily translatable into automated tests using frameworks like Behave or Pytest-BDD.*

### TC-001: Customer User Registration (Happy Path)
**Priority:** High | **Severity:** Critical
**Description:** Verify that a new user can successfully register an account using valid data.

**Feature:** User Authentication
**Scenario:** Successful Customer Registration
  **Given** I navigate to the ToolShop Registration page
  **And** I do not currently have an account
  **When** I fill out the registration form with valid, unique data
  **And** I submit the form
  **Then** the system should route me to the Login page
  **And** a 201 Created response should be recorded in the API network logs
  **And** I should be able to log in with the newly created credentials

---

## Format 2: Traditional Step-by-Step
*Used for complex End-to-End flows requiring specific data setup, explicit assertions, and strict auditing.*

### TC-002: End-to-End Order Checkout Flow
**Priority:** High | **Severity:** Critical
**Description:** Verify an authenticated customer can add a product to the cart, complete the checkout flow, and generate an invoice.

**Preconditions:**
1. The web application is accessible.
2. The user has a valid, authenticated customer account.
3. The database inventory has at least one product with `stock > 0`.

| Step # | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Navigate to the homepage and log in as a Customer. | The header displays the user's name, confirming successful authentication. |
| 2 | Search for a product that is in stock and click on its details. | The Product Details page loads correctly, displaying price, description, and an "Add to Cart" button. |
| 3 | Click the "Add to Cart" button. | A success notification appears, and the cart icon counter increments by 1. |
| 4 | Click the Cart icon in the header. | The Shopping Cart page loads, displaying the correct item, quantity (1), and accurate total price. |
| 5 | Click "Proceed to Checkout". | The system routes to the first step of the Checkout wizard (Billing Address). |
| 6 | Populate valid Billing and Shipping addresses, then proceed. | Address inputs are accepted and the user progresses to the Payment method screen. |
| 7 | Select "Cash on Delivery" or mock credit card, and click "Confirm". | The order is submitted successfully. |
| 8 | **Assertion:** Wait for the order confirmation screen. | The screen displays "Payment Successful" and provides a unique Order/Invoice ID. |
| 9 | **Database Verification:** Check the `invoices` table for the Order ID. | A new row exists in the `invoices` table matching the Order ID, user ID, and total amount. |

---

### TC-003: Product Search & Filtering (Boundary / Negative Test)
**Priority:** Medium | **Severity:** Major
**Description:** Verify the behavior of the product catalog when applying overlapping or extreme filters.

**Preconditions:**
1. User is on the homepage (authentication not required).

| Step # | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Enter a non-existent product string (e.g., `@@@XYZ_NO_PRODUCT@@@`) into the search bar. | The UI gracefully handles the empty state, displaying a message like "No products found," without throwing console errors. |
| 2 | Clear the search. Adjust the price filter slider so that `Min Price > Max Price` (if UI allows). | The slider should natively prevent the Min handle from crossing the Max handle. |
| 3 | Adjust the price filter to `Min: $100`, `Max: $150`. | The catalog updates dynamically. |
| 4 | **Assertion:** Inspect the displayed products. | EVERY product displayed on the page has a price strictly between $100 and $150. |