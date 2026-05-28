import pytest
import requests


BASE_URL = "http://localhost:3000"


@pytest.mark.api
@pytest.mark.ci
def test_api_search_returns_apple_juice():
    """
    Test goal:
    Verify that the Juice Shop product search API returns Apple Juice.

    This is an API-level test and does not use the browser.
    """

    # STEP 1:
    # Send GET request to product search API.
    response = requests.get(
        f"{BASE_URL}/rest/products/search",
        params={"q": "Apple Juice"},
        timeout=10,
    )

    # STEP 2:
    # Verify response status code.
    assert response.status_code == 200

    # STEP 3:
    # Parse JSON response.
    response_body = response.json()

    # STEP 4:
    # Verify response contains products.
    assert "data" in response_body
    assert len(response_body["data"]) > 0

    # STEP 5:
    # Verify Apple Juice is included in the result.
    product_names = [
        product["name"]
        for product in response_body["data"]
    ]

    assert "Apple Juice (1000ml)" in product_names