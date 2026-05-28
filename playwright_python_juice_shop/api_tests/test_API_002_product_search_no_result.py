import pytest
import requests


BASE_URL = "http://localhost:3000"


@pytest.mark.api
@pytest.mark.ci
def test_api_search_returns_no_result_for_unknown_product():
    """
    Test goal:
    Verify that the Juice Shop product search API returns an empty result
    when searching for a product that does not exist.
    """

    # STEP 1:
    # Send GET request with a product name that should not exist.
    response = requests.get(
        f"{BASE_URL}/rest/products/search",
        params={"q": "ProductThatDoesNotExist12345"},
        timeout=10,
    )

    # STEP 2:
    # Verify response status code.
    assert response.status_code == 200

    # STEP 3:
    # Parse JSON response.
    response_body = response.json()

    # STEP 4:
    # Verify response contains data field.
    assert "data" in response_body

    # STEP 5:
    # Verify data list is empty.
    assert response_body["data"] == []