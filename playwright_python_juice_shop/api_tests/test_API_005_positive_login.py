from datetime import datetime

import pytest
import requests


BASE_URL = "http://localhost:3000"


@pytest.mark.api
@pytest.mark.login
@pytest.mark.ci
def test_api_login_succeeds_with_valid_user():
    """
    Test goal:
    Create a new user through API,
    then verify that login succeeds with valid credentials.
    """

    # STEP 1:
    # Create unique user data.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    email = f"api_user_{timestamp}@test.com"
    password = "Test12345!"

    # STEP 2:
    # Register a new user through API.
    register_payload = {
        "email": email,
        "password": password,
        "passwordRepeat": password,
        "securityQuestion": {
            "id": 1,
            "question": "Your eldest siblings middle name?",
        },
        "securityAnswer": "Helsinki",
    }

    register_response = requests.post(
        f"{BASE_URL}/api/Users/",
        json=register_payload,
        timeout=10,
    )

    # STEP 3:
    # Verify user registration succeeded.
    assert register_response.status_code in [200, 201]

    # STEP 4:
    # Login with the created user.
    login_payload = {
        "email": email,
        "password": password,
    }

    login_response = requests.post(
        f"{BASE_URL}/rest/user/login",
        json=login_payload,
        timeout=10,
    )

    # STEP 5:
    # Verify login succeeded.
    assert login_response.status_code == 200

    # STEP 6:
    # Parse response body.
    login_body = login_response.json()

    # STEP 7:
    # Verify authentication data exists.
    assert "authentication" in login_body
    assert "token" in login_body["authentication"]

    # STEP 8:
    # Verify token is not empty.
    token = login_body["authentication"]["token"]
    assert token is not None
    assert len(token) > 0

    print("\nCreated API user:", email)
    print("Login token was returned successfully.")