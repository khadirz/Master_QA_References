import pytest
import requests


BASE_URL = "http://localhost:3000"


@pytest.mark.api
@pytest.mark.ci
def test_api_product_search_response_contract_for_apple_juice():
    """
    Test goal:
    Verify that the product search API returns Apple Juice
    with the expected response structure and key fields.

    This is a contract-style API test.
    """

    # STEP 1:
    # Send GET request to product search API.
    response = requests.get(
        f"{BASE_URL}/rest/products/search",
        params={"q": "Apple Juice"},
        timeout=10,
    )

    # STEP 2:
    # Verify successful response.
    assert response.status_code == 200

    # STEP 3:
    # Parse response body.
    response_body = response.json()

    # STEP 4:
    # Verify top-level response structure.
    assert "status" in response_body
    assert "data" in response_body
    assert isinstance(response_body["data"], list)

    # STEP 5:
    # Find Apple Juice product from the response.
    apple_juice = None

    for product in response_body["data"]:
        if product.get("name") == "Apple Juice (1000ml)":
            apple_juice = product
            break

    # STEP 6:
    # Verify Apple Juice exists in the response.
    assert apple_juice is not None

    # STEP 7:
    # Verify key product fields exist.
    assert "id" in apple_juice
    assert "name" in apple_juice
    assert "description" in apple_juice
    assert "price" in apple_juice
    assert "image" in apple_juice

    # STEP 8:
    # Verify key field values and types.
    assert apple_juice["name"] == "Apple Juice (1000ml)"
    assert isinstance(apple_juice["description"], str)
    assert isinstance(apple_juice["price"], (int, float))
    assert apple_juice["price"] > 0