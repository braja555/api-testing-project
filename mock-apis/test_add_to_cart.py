import requests

BASE_URL = 'http://127.0.0.1:5000'
ADD_TO_CART_ENDPOINT = "/users/{}/cart"


def make_post_request(endpoint, payload, params):
    """Helper function to make a POST request."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload, params=params)
    return response


def test_add_to_cart_success():
    """Test adding an item to the cart successfully."""
    user_id = "user1"
    payload = {"bookId": "1-e51969c6-df00-4829-afa9-1104749015b", "quantity": 2}
    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data.get('message') == "Item added to cart successfully"
    assert response_data.get('user')['userId'] == user_id
    assert any(item for item in response_data.get('user')['cart'] if item["bookId"] == payload["bookId"])


def test_add_to_cart_user_not_exist():
    """Test adding an item to the cart when the user does not exist."""
    user_id = "new_user_not_exist"
    payload = {"bookId": "1-e51969c6-df00-4829-afa9-1104749015b", "quantity": 1}
    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data.get('message') == "Item added to cart successfully"
    assert response_data.get('user')['userId'] == user_id


def test_add_to_cart_book_not_found():
    """Test adding a non-existent book to the cart."""
    user_id = "user1"
    payload = {"bookId": "9999999", "quantity": 1}
    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    assert response.status_code == 404
    assert response.json().get('error') == "Book not found"


def test_add_to_cart_book_not_available():
    """Test adding an unavailable book to the cart."""
    user_id = "user1"
    payload = {"bookId": "2-e7022c47-0d09-443e-ad65-00281bb7408a", "quantity": 1}
    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Book is not available"


def test_add_to_cart_invalid_input():
    """Test adding an item with invalid input (missing bookId or quantity)."""
    user_id = "user1"
    payload = {"quantity": 1}
    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Invalid input"


def test_add_to_cart_quantity_update():
    """Test adding an item that already exists in the cart to update its quantity."""
    user_id = "user1"
    payload = {"bookId": "1-e51969c6-df00-4829-afa9-1104749015b", "quantity": 1}
    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    response_data = response.json()
    initial_quantity = next(item for item in response_data.get('user')['cart'] if item["bookId"] == payload["bookId"])[
        "quantity"]

    response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    response_data = response.json()
    updated_quantity = next(item for item in response_data.get('user')['cart'] if item["bookId"] == payload["bookId"])[
        "quantity"]

    assert response.status_code == 200
    assert updated_quantity == initial_quantity + payload["quantity"]

def test_clear_cart_success():
    """Test clearing the cart successfully."""
    user_id = "user1"
    payload = {"bookId": "1-e51969c6-df00-4829-afa9-1104749015b", "quantity": 2}

    # Add an item to the cart first
    add_response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), payload)
    assert add_response.status_code == 200
    add_response_data = add_response.json()
    assert add_response_data.get('message') == "Item added to cart successfully"

    # Now clear the cart
    clear_response = make_post_request(ADD_TO_CART_ENDPOINT.format(user_id), {}, params={"clear_cart": "true"})
    assert clear_response.status_code == 200
    clear_response_data = clear_response.json()
    assert clear_response_data.get('message') == "Cart cleared successfully"
    assert clear_response_data.get('user')['userId'] == user_id
    assert len(clear_response_data.get('user')['cart']) == 0


if __name__ == "__main__":
    test_add_to_cart_success()
    test_add_to_cart_user_not_exist()
    test_add_to_cart_book_not_found()
    test_add_to_cart_book_not_available()
    test_add_to_cart_invalid_input()
    test_add_to_cart_quantity_update()
    test_clear_cart_success()
