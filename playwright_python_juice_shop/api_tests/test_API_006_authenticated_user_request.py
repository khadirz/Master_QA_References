from datetime import datetime

import pytest
import requests


BASE_URL = "http://localhost:3000"


@pytest.mark.api
@pytest.mark.login
@pytest.mark.ci
def test_api_authenticated_user_request_with_token():
    """
    Test goal:
    Register a user through API,
    log in through API,
    extract authentication token,
    and use the token to access an authenticated basket endpoint.
    """

    # STEP 1:
    # Create unique user data.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    email = f"api_auth_user_{timestamp}@test.com"
    password = "Test12345!"

    # STEP 2:
    # Register a new user.
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

    print("\nRegistration status:", register_response.status_code)
    print("Registration response:", register_response.text)

    assert register_response.status_code in [200, 201]

    # STEP 3:
    # Log in with the created user.
    login_payload = {
        "email": email,
        "password": password,
    }

    login_response = requests.post(
        f"{BASE_URL}/rest/user/login",
        json=login_payload,
        timeout=10,
    )

    print("\nLogin status:", login_response.status_code)
    print("Login response:", login_response.text)

    assert login_response.status_code == 200

    login_body = login_response.json()

    # STEP 4:
    # Verify authentication data exists.
    assert "authentication" in login_body

    authentication = login_body["authentication"]

    assert "token" in authentication
    assert "bid" in authentication
    assert "umail" in authentication

    token = authentication["token"]
    basket_id = authentication["bid"]
    user_email = authentication["umail"]

    assert token is not None
    assert len(token) > 0
    assert user_email == email

    # STEP 5:
    # Use token in Authorization header.
    headers = {
        "Authorization": f"Bearer {token}",
    }

    # STEP 6:
    # Call authenticated basket endpoint using basket id from login response.
    basket_response = requests.get(
        f"{BASE_URL}/rest/basket/{basket_id}",
        headers=headers,
        timeout=10,
    )

    print("\nBasket status:", basket_response.status_code)
    print("Basket response:", basket_response.text)

    # STEP 7:
    # Verify authenticated request is accepted.
    assert basket_response.status_code == 200

    # STEP 8:
    # Verify response contains basket data.
    basket_body = basket_response.json()

    assert "data" in basket_body