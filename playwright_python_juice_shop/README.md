# Playwright Python Automation Project: OWASP Juice Shop

This project is a practical QA automation project using **Playwright with Python** and **pytest**.

The target application is **OWASP Juice Shop**, running locally with Docker.

The project covers a realistic e-commerce workflow, including signup, login, product search, basket operations, checkout, address creation, delivery selection, payment selection, order summary, and order confirmation.

---

## Project Goal

The goal of this project is to demonstrate practical test automation skills with:

- Playwright with Python
- pytest test execution
- End-to-end UI automation
- Positive and negative test scenarios
- Form validation testing
- Basket and checkout workflow testing
- Reusable helper functions
- Shared test data management
- Debugging locator and strict mode issues
- AI-assisted test development and refactoring

---

## Tech Stack

- Python
- Playwright
- pytest
- OWASP Juice Shop
- Docker
- VS Code
- Git and GitHub

---

## Application Under Test

OWASP Juice Shop runs locally at:

```text
http://localhost:3000
```

The application is started with Docker:

```bash
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

On macOS, Docker Desktop must be running before this command works.

---

## Project Structure

```text
playwright_python_juice_shop/
│
├── helpers/
│   ├── popup_helper.py
│   ├── login_helper.py
│   ├── navigation_helper.py
│   ├── search_helper.py
│   ├── basket_helper.py
│   └── checkout_helper.py
│
├── python_tests/
│   ├── test_TC001_homepage.py
│   ├── test_TC002_locators_basic.py
│   ├── test_TC003_search_product.py
│   ├── test_TC004_assertions_basic.py
│   ├── test_TC005_signup_user.py
│   ├── test_TC006_login_user.py
│   ├── test_TC007_add_product_to_basket.py
│   ├── test_TC008_add_specific_product_to_basket.py
│   ├── test_TC009_remove_product_from_basket.py
│   ├── test_TC010_negative_login.py
│   ├── test_TC011_login_form_validation.py
│   ├── test_TC012_search_no_result.py
│   ├── test_TC013_helpers_refactor_check.py
│   ├── test_TC014_basket_quantity_update.py
│   ├── test_TC015_checkout_first_step.py
│   ├── test_TC016_add_checkout_address.py
│   ├── test_TC017_select_address_continue.py
│   ├── test_TC018_select_delivery_method.py
│   ├── test_TC019_select_payment_method.py
│   ├── test_TC020_continue_to_order_summary.py
│   └── test_TC021_place_order_confirmation.py
│
├── test_data/
│   └── users.py
│
├── requirements.txt
├── playwright.config.ts
├── package.json
├── package-lock.json
└── README.md
```

---

## Setup Guide

### 1. Prerequisites

Make sure these tools are installed:

- Python 3
- Docker Desktop
- VS Code
- Git

Check Python version:

```bash
python3 --version
```

Check Docker version:

```bash
docker --version
```

---

### 2. Start Docker Desktop

On macOS, Docker commands work only when Docker Desktop is running.

Open Docker Desktop from Applications and wait until it is fully started.

Check Docker is running:

```bash
docker ps
```

If Docker is not running, you may see an error like:

```text
failed to connect to the docker API
```

Fix:

Open Docker Desktop and wait until it is fully running.

---

### 3. Start OWASP Juice Shop

Run this command in a separate terminal window:

```bash
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

The application should be available at:

```text
http://localhost:3000
```

Keep this terminal window open while running tests.

---

### 4. Open the Project Folder

Go to the project folder:

```bash
cd ~/Master_QA_References/playwright_python_juice_shop
```

Check the files:

```bash
ls
```

You should see folders like:

```text
helpers
python_tests
test_data
requirements.txt
README.md
```

---

### 5. Create Python Virtual Environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, your terminal should show something like:

```text
(venv)
```

---

### 6. Install Python Dependencies

Install dependencies from `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
```

Check pytest is installed:

```bash
python3 -m pytest --version
```

---

### 7. Install Playwright Browsers

Run:

```bash
python3 -m playwright install
```

This installs the browsers needed by Playwright.

---

## Running Tests

### Run One Test

Example:

```bash
python3 -m pytest python_tests/test_TC010_negative_login.py --headed
```

---

### Run All Tests in Headed Mode

```bash
python3 -m pytest python_tests --headed
```

Headed mode opens the browser during test execution.

---

### Run All Tests in Headless Mode

```bash
python3 -m pytest python_tests
```

Headless mode runs tests without opening the browser UI.

---

### Run Tests with Detailed Output

```bash
python3 -m pytest python_tests --headed -s -v
```

Options:

- `--headed`: opens the browser
- `-s`: shows print output in the terminal
- `-v`: shows more detailed pytest output

---

## Quick Start Summary

Use this when everything is already installed:

```bash
cd ~/Master_QA_References/playwright_python_juice_shop

source venv/bin/activate

python3 -m pytest python_tests --headed
```

Start OWASP Juice Shop in a separate terminal first:

```bash
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

---

## Test Coverage

| Test Case | Description | Status |
|---|---|---|
| TC001 | Homepage smoke test | Passed |
| TC002 | Basic locators | Passed |
| TC003 | Product search | Passed |
| TC004 | Basic assertions | Passed |
| TC005 | Signup user | Passed |
| TC006 | Login user | Passed |
| TC007 | Add product to basket | Passed |
| TC008 | Add specific product to basket and verify basket | Passed |
| TC009 | Remove product from basket | Passed |
| TC010 | Negative login combinations | Passed |
| TC011 | Login form validation | Passed |
| TC012 | Search no-result test | Passed |
| TC013 | Helper refactor check | Passed |
| TC014 | Basket quantity increase/decrease | Passed |
| TC015 | Checkout first step | Passed |
| TC016 | Add checkout address | Passed |
| TC017 | Select address and continue to delivery method | Passed |
| TC018 | Select delivery method and continue to payment | Passed |
| TC019 | Add/select payment method | Passed |
| TC020 | Continue to order summary | Passed |
| TC021 | Place order and verify confirmation | Passed |

---

## Main E-commerce Workflow Covered

The project covers the full main user journey:

```text
Signup/Login
Search product
Add product to basket
Open basket
Start checkout
Select address
Select delivery method
Select payment method
Review order summary
Place order
Verify order confirmation
```

---

## Negative Testing Coverage

Negative and validation scenarios include:

- Valid email with invalid password
- Invalid email with valid password
- Invalid email with invalid password
- Empty email and empty password
- Valid email with empty password
- Empty email with valid password
- Invalid email format
- Search with no matching product

---

## Helper Functions

The project uses helper files to keep tests clean, readable, and reusable.

### `navigation_helper.py`

Common navigation actions:

```text
open_juice_shop_homepage
go_to_homepage
```

### `login_helper.py`

Reusable login flow:

```text
login_to_juice_shop
```

### `search_helper.py`

Reusable search functions:

```text
search_product
verify_search_result_title
```

### `basket_helper.py`

Basket-related actions:

```text
add_first_visible_product_to_basket
open_basket
get_basket_count
verify_product_in_basket
remove_product_from_basket
```

### `checkout_helper.py`

Checkout-related actions:

```text
click_checkout
verify_address_selection_page
open_add_new_address_form
fill_checkout_address_form
submit_checkout_address_form
verify_address_in_address_list
select_first_address
click_continue_to_delivery_method
verify_delivery_method_page
select_first_delivery_method
click_continue_to_payment
verify_payment_page
open_add_new_card_form
fill_payment_card_form
submit_payment_card_form
select_first_payment_option
verify_payment_option_is_selected
click_continue_to_order_summary
verify_order_summary_page
place_order
verify_order_confirmation_page
```

---

## Key Learning Points

This project includes practical examples of:

- Using `get_by_role`, `get_by_text`, `get_by_placeholder`, and CSS locators
- Handling Playwright strict mode violations
- Avoiding unstable dynamic locators
- Using pytest parameterization
- Creating reusable helper functions
- Managing shared test data
- Working with tables, rows, cells, and buttons
- Testing positive and negative login scenarios
- Testing form validation behavior
- Handling checkout flow steps
- Debugging accessible names versus visible text
- Scoping locators to avoid filling the wrong field
- Adjusting tests based on real application behavior

---

## Important Playwright Lessons Learned

### 1. Accessible Name May Be Different from Visible Text

Example:

```text
Visible text: Continue
Accessible name: Proceed to delivery method selection
```

So this may fail:

```python
page.get_by_role("button", name="Continue")
```

But this works:

```python
page.get_by_role("button", name="Proceed to delivery method selection")
```

---

### 2. Strict Mode Violations Need More Specific Locators

If Playwright finds more than one matching element, it raises a strict mode violation.

Example problem:

```python
page.get_by_text("Apple Juice")
```

Better:

```python
page.get_by_text("Apple Juice (1000ml)")
```

Or even better in a table:

```python
page.locator("mat-cell").filter(has_text="Apple Juice (1000ml)")
```

---

### 3. Avoid Dynamic Angular Material IDs

Dynamic IDs like this can change:

```python
page.locator("#mat-input-3")
```

Better options include:

```python
page.get_by_placeholder("Country")
page.get_by_role("textbox", name="Text field for the login email")
page.locator("mat-cell").filter(has_text="Apple Juice (1000ml)")
```

---

### 4. Scope Locators to the Correct Section

A global locator can accidentally fill the wrong field.

Bad example:

```python
page.locator("input:visible")
```

Better example:

```python
card_panel = page.locator("mat-expansion-panel").filter(
    has_text="Add a credit or debit card"
)

card_inputs = card_panel.locator("input")
```

This keeps the locator inside the payment card form.

---

## Test Data Notes

Some tests use a valid test user stored in:

```text
test_data/users.py
```

Example:

```python
VALID_USER_EMAIL = "test_user_YYYYMMDD_HHMMSS@test.com"
VALID_USER_PASSWORD = "Test12345!"

INVALID_USER_EMAIL = "invalid_user@test.com"
INVALID_USER_PASSWORD = "WrongPassword123!"
```

OWASP Juice Shop stores users, addresses, basket items, and payment data in the running application environment.

If the Docker container is restarted or removed, the Juice Shop database may reset.

When that happens, the old test user may no longer exist.

If login fails with:

```text
Invalid email or password
```

run the signup test again:

```bash
python3 -m pytest python_tests/test_TC005_signup_user.py --headed -s
```

Copy the generated email from the terminal and update:

```text
test_data/users.py
```

---

## Common Problems and Fixes

### Docker Daemon Error

Problem:

```text
failed to connect to the docker API
```

Fix:

Open Docker Desktop and wait until it is fully running.

Then check:

```bash
docker ps
```

---

### pytest Not Found

Problem:

```text
No module named pytest
```

Fix:

Make sure the virtual environment is activated and install dependencies:

```bash
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

---

### Playwright Browser Missing

Problem:

```text
Executable doesn't exist
```

Fix:

```bash
python3 -m playwright install
```

---

### Login Fails After Docker Restart

Problem:

```text
Invalid email or password
```

Reason:

The Juice Shop database may have been reset.

Fix:

Run signup again:

```bash
python3 -m pytest python_tests/test_TC005_signup_user.py --headed -s
```

Then update the generated email in:

```text
test_data/users.py
```

---

## AI-Assisted Development

This project was developed using an AI-assisted learning and development workflow.

AI was used to support:

- Creating initial Playwright test drafts
- Explaining Python and Playwright syntax
- Debugging Playwright errors
- Improving locator strategies
- Refactoring repeated code into helpers
- Designing positive and negative test cases
- Improving test coverage
- Improving README and project documentation

All AI-generated suggestions were manually reviewed, executed, debugged, and validated.

The goal was not to blindly copy AI-generated code, but to use AI as a pair testing and pair programming assistant while keeping engineering ownership of the final implementation.

---

## Git Commands

After updating tests or documentation:

```bash
git status
git add .
git commit -m "Update Playwright Python Juice Shop project"
git push
```

---

## Future Improvements

Possible next improvements:

- Add GitHub Actions CI pipeline
- Add Playwright traces and screenshots on failure
- Start Page Object Model structure
- Add API tests
- Add test data setup and cleanup strategy
- Create reusable pytest fixtures
- Generate HTML test reports
- Add full test execution instructions for CI
- Add order history validation
- Add API-based test data reset if available

---

## Current Status

The main e-commerce workflow is complete and passing up to:

```text
TC021: Place order and verify confirmation
```

This project now demonstrates a complete UI automation flow from login to order confirmation using Playwright with Python.