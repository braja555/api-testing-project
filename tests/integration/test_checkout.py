import requests

BASE_URL = 'http://localhost:5000'
CHECKOUT_ENDPOINT = "/users/{}/checkout"

def make_post_request(endpoint):
    """Helper function to make a POST request."""
    response = requests.post(endpoint)
    return response

def test_checkout_success():
    """Test successful checkout."""
    user_id = "user1"
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id))
    assert response.status_code == 200
    response_data = response.json()
    assert "orderId" in response_data
    assert response_data.get('message') == "Your order is successful"
    assert response_data.get('userId') == user_id

def test_checkout_user_not_found():
    """Test checkout with a non-existent user."""
    user_id = "non_existent_user"
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id))
    assert response.status_code == 404
    assert response.json().get('error') == "User not found"

def test_checkout_book_not_found():
    """Test checkout with a non-existent book in the cart."""
    user_id = "user_with_invalid_book"
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id))
    assert response.status_code == 404
    assert "Book with ID" in response.json().get('error')

def test_checkout_book_not_available():
    """Test checkout with an unavailable book in the cart."""
    user_id = "user_with_unavailable_book"
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id))
    assert response.status_code == 400
    assert "Not enough stock for book" in response.json().get('error')

def test_checkout_empty_cart():
    """Test checkout with an empty cart."""
    user_id = "user_with_empty_cart"
    response = make_post_request(CHECKOUT_ENDPOINT.format(user_id))
    assert response.status_code == 400
    assert response.json().get('error') == "Cart is empty"

if __name__ == "__main__":
    test_checkout_success()
    test_checkout_user_not_found()
    test_checkout_book_not_found()
    test_checkout_book_not_available()
    test_checkout_empty_cart()
