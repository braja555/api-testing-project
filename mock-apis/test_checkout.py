import requests

BASE_URL = 'http://127.0.0.1:5000'
ADD_TO_CART_ENDPOINT = "/users/{}/cart"
CHECKOUT_ENDPOINT = "/users/{}/checkout"


def make_post_request(endpoint, payload):
    """Helper function to make a POST request."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload)
    return response


def test_checkout_success():
    """Test successful checkout."""
    user_id = "user1"

    # Now proceed to checkout
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id), user_id)
    assert response.status_code == 200
    response_data = response.json()
    assert "orderId" in response_data
    assert response_data.get('message') == "Your order is successful"
    assert response_data.get('userId') == user_id


def test_checkout_user_not_found():
    """Test checkout with a non-existent user."""
    user_id = "non_existent_user"
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id), user_id)
    assert response.status_code == 404
    assert response.json().get('error') == "User not found"


if __name__ == "__main__":
    test_checkout_success()
    test_checkout_user_not_found()
