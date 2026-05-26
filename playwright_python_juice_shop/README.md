# Playwright Python Automation Project: OWASP Juice Shop
![Playwright Python Tests](https://github.com/khadirz/Master_QA_References/actions/workflows/playwright-python-tests.yml/badge.svg)

This project is a practical QA automation project using **Playwright with Python** and **pytest**.

The target application is **OWASP Juice Shop**, running locally with Docker.

The project covers a realistic e-commerce workflow, including signup, login, product search, basket operations, checkout, address creation, delivery selection, payment selection, order summary, and order confirmation.

The project also includes **GitHub Actions CI** and reusable **pytest fixtures** so selected tests can run reliably in a fresh CI environment.

---

## Project Goal

The goal of this project is to demonstrate practical QA automation skills with:

- Playwright with Python
- pytest test execution
- End-to-end UI automation
- Positive and negative test scenarios
- Form validation testing
- Basket and checkout workflow testing
- Reusable helper functions
- Reusable pytest fixtures
- Shared test data management
- GitHub Actions CI
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
- GitHub Actions

---

## Application Under Test

OWASP Juice Shop runs locally at:

```text
http://localhost:3000
```

Start the application with Docker:

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
│   ├── test_TC006_login_user_with_fixture.py
│   ├── test_TC007_add_product_to_basket.py
│   ├── test_TC007_add_product_with_logged_in_fixture.py
│   ├── test_TC008_add_specific_product_to_basket.py
│   ├── test_TC008_add_specific_product_with_fixture.py
│   ├── test_TC009_remove_product_from_basket.py
│   ├── test_TC009_remove_product_with_fixture.py
│   ├── test_TC010_negative_login.py
│   ├── test_TC011_login_form_validation.py
│   ├── test_TC012_search_no_result.py
│   ├── test_TC013_helpers_refactor_check.py
│   ├── test_TC013_product_in_basket_fixture_check.py
│   ├── test_TC014_basket_quantity_update.py
│   ├── test_TC014_basket_quantity_with_fixture.py
│   ├── test_TC015_checkout_first_step.py
│   ├── test_TC015_checkout_address_fixture_check.py
│   ├── test_TC016_add_checkout_address.py
│   ├── test_TC017_select_address_continue.py
│   ├── test_TC017_checkout_delivery_fixture_check.py
│   ├── test_TC018_select_delivery_method.py
│   ├── test_TC018_checkout_payment_fixture_check.py
│   ├── test_TC019_select_payment_method.py
│   ├── test_TC020_continue_to_order_summary.py
│   ├── test_TC020_checkout_order_summary_fixture_check.py
│   ├── test_TC021_place_order_confirmation.py
│   └── test_TC021_place_order_with_fixture.py
│
├── test_data/
│   └── users.py
│
├── conftest.py
├── requirements.txt
├── playwright.config.ts
├── package.json
├── package-lock.json
└── README.md
```

The GitHub Actions workflow is stored at repository root:

```text
.github/workflows/playwright-python-tests.yml
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

You should see folders and files like:

```text
helpers
python_tests
test_data
conftest.py
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

### Run All Tests Locally

```bash
python3 -m pytest python_tests --headed
```

---

### Run Tests Headless

```bash
python3 -m pytest python_tests
```

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

Use this when everything is already installed.

Start OWASP Juice Shop in one terminal:

```bash
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

In another terminal:

```bash
cd ~/Master_QA_References/playwright_python_juice_shop

source venv/bin/activate

python3 -m pytest python_tests --headed
```

---

## GitHub Actions CI

This project includes a GitHub Actions workflow:

```text
.github/workflows/playwright-python-tests.yml
```

The CI workflow:

- Starts OWASP Juice Shop as a Docker service
- Sets up Python
- Installs project dependencies
- Installs Playwright Chromium browser
- Waits until Juice Shop is ready
- Runs selected CI-friendly tests
- Uploads test artifacts if available

The workflow runs on:

- Push to `main`
- Pull request to `main`
- Manual run from GitHub Actions tab

---

## Current CI Strategy

CI starts with a fresh OWASP Juice Shop database every time.

Because of that, tests should not depend on old local users, addresses, basket data, or payment data.

To solve this, the project uses pytest fixtures in `conftest.py`.

These fixtures create fresh data during the test run.

---

## CI-Ready Fixtures

The current fixture chain includes:

```text
fresh_user
logged_in_page
product_in_basket_page
checkout_address_page
checkout_delivery_page
checkout_payment_page
checkout_order_summary_page
```

### `fresh_user`

Creates a new unique user during the test run.

Useful for login and negative login tests.

---

### `logged_in_page`

Creates a fresh user, logs in with that user, and returns a logged-in page.

Useful for tests that need authenticated user state.

---

### `product_in_basket_page`

Creates a fresh user, logs in, adds Apple Juice to basket, opens the basket page, and returns the page.

Important note:

This fixture does not use search. Search is tested separately. For stable setup, it adds the first product from the homepage, which is Apple Juice in OWASP Juice Shop.

---

### `checkout_address_page`

Starts from basket page, clicks Checkout, adds a new address, verifies the address, and returns the address selection page.

---

### `checkout_delivery_page`

Starts from the address selection page, selects the first address, continues to the delivery method page, and returns the page.

---

### `checkout_payment_page`

Starts from the delivery method page, selects the first delivery method, continues to the payment page, and returns the page.

---

### `checkout_order_summary_page`

Starts from the payment page, adds or selects a payment method, continues to the order summary page, and returns the page.

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
| TC006 Fixture | Login with fresh user fixture | CI-ready |
| TC007 | Add product to basket | Passed |
| TC007 Fixture | Add product with logged-in fixture | CI-ready |
| TC008 | Add specific product to basket and verify basket | Passed |
| TC008 Fixture | Add specific product with logged-in fixture | CI-ready |
| TC009 | Remove product from basket | Passed |
| TC009 Fixture | Remove product with logged-in fixture | CI-ready |
| TC010 | Negative login combinations | CI-ready |
| TC011 | Login form validation | CI-ready |
| TC012 | Search no-result test | CI-ready |
| TC013 | Helper refactor check | Passed |
| TC013 Fixture | Product in basket fixture check | CI-ready |
| TC014 | Basket quantity increase/decrease | Passed |
| TC014 Fixture | Basket quantity with fixture | CI-ready |
| TC015 | Checkout first step | Passed |
| TC015 Fixture | Checkout address fixture check | CI-ready |
| TC016 | Add checkout address | Passed |
| TC017 | Select address and continue to delivery method | Passed |
| TC017 Fixture | Checkout delivery fixture check | CI-ready |
| TC018 | Select delivery method and continue to payment | Passed |
| TC018 Fixture | Checkout payment fixture check | CI-ready |
| TC019 | Add/select payment method | Passed |
| TC020 | Continue to order summary | Passed |
| TC020 Fixture | Checkout order summary fixture check | CI-ready |
| TC021 | Place order and verify confirmation | Passed |
| TC021 Fixture | Place order with checkout fixture | CI-ready |

---

## Main E-commerce Workflow Covered

The project covers the full main user journey:

```text
Signup/Login
Search product
Add product to basket
Open basket
Start checkout
Add/select address
Select delivery method
Add/select payment method
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

---

### `navigation_helper.py`

Common navigation actions:

```text
open_juice_shop_homepage
go_to_homepage
```

---

### `login_helper.py`

Reusable login flow:

```text
login_to_juice_shop
```

---

### `search_helper.py`

Reusable search functions:

```text
search_product
verify_search_result_title
```

---

### `basket_helper.py`

Basket-related actions:

```text
add_first_visible_product_to_basket
open_basket
get_basket_count
verify_product_in_basket
remove_product_from_basket
```

---

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
- Creating reusable pytest fixtures
- Managing shared test data
- Working with tables, rows, cells, and buttons
- Testing positive and negative login scenarios
- Testing form validation behavior
- Handling checkout flow steps
- Debugging accessible names versus visible text
- Scoping locators to avoid filling the wrong field
- Stabilizing tests for CI
- Separating test purpose from test setup
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

This can also match:

```text
Pineapple Juice
```

Better:

```python
page.get_by_text("Apple Juice (1000ml)")
```

Or scope the locator to the correct product card, table row, or section.

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

### 5. Fixtures Should Prefer Stable Setup

Search is tested separately in search test cases.

For setup fixtures, it is better to use stable setup steps instead of testing search again.

Example:

```text
product_in_basket_page fixture adds the first product from the homepage
instead of using the search UI.
```

This makes checkout-related CI tests more stable.

---

## Test Data Notes

Some older local tests use a valid test user stored in:

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

For CI-friendly tests, prefer pytest fixtures instead of relying on `test_data/users.py`.

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

### GitHub Actions Workflow Not Visible

Problem:

GitHub Actions does not show the workflow.

Possible reason:

The workflow file is in the wrong folder.

Correct location:

```text
.github/workflows/playwright-python-tests.yml
```

Wrong location:

```text
playwright_python_juice_shop/.github/workflows/playwright-python-tests.yml
```

---

### GitHub Push Rejected for Workflow File

Problem:

```text
refusing to allow a Personal Access Token to create or update workflow
without workflow scope
```

Reason:

The GitHub token does not have the `workflow` scope.

Fix:

Create a new GitHub Personal Access Token with:

```text
repo
workflow
```

Then push again.

---

## AI-Assisted Development

This project was developed using an AI-assisted learning and development workflow.

AI was used to support:

- Creating initial Playwright test drafts
- Explaining Python and Playwright syntax
- Debugging Playwright errors
- Improving locator strategies
- Refactoring repeated code into helpers
- Creating reusable pytest fixtures
- Designing positive and negative test cases
- Improving CI stability
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

- Add Playwright traces and screenshots on failure
- Start Page Object Model structure
- Add API tests
- Add test data setup and cleanup strategy
- Create more reusable pytest fixtures
- Generate HTML test reports
- Add order history validation
- Add API-based test data reset if available
- Add smoke/regression markers
- Split CI jobs into smoke and full regression

---

## Current Status

The main e-commerce workflow is complete locally and CI-friendly fixture tests are in place for the core checkout flow.

Current core flow:

```text
Login
Add product to basket
Address
Delivery
Payment
Order summary
Place order
Confirmation
```

This project now demonstrates a complete UI automation flow from login to order confirmation using Playwright with Python, reusable helpers, pytest fixtures, Docker, and GitHub Actions CI.

## Pytest Markers

This project uses pytest markers to organize and run specific groups of tests.

Markers are defined in `pytest.ini`.

Available markers:

```text
smoke: quick smoke tests for basic application availability
login: login and authentication related tests
basket: basket related tests
checkout: checkout flow related tests
regression: wider regression test coverage
ci: tests that are safe to run in GitHub Actions CI

for example, Run checkout tests:
python3 -m pytest -m checkout --headed