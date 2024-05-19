import requests

BASE_URL = 'http://localhost:3001'

def test_add_to_cart_success():
    # Assuming userId and bookId are valid and available
    userId = "user123"
    bookId = "book456"
    url = f"{BASE_URL}/users/{userId}/cart"
    payload = {
        "bookId": bookId,
        "quantity": 1
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json().get('message') == "Book added to cart."

def test_add_to_cart_book_not_found():
    # Assuming userId is valid but bookId is invalid or not available
    userId = "user123"
    invalid_bookId = "invalid_book_id"
    url = f"{BASE_URL}/users/{userId}/cart"
    payload = {
        "bookId": invalid_bookId,
        "quantity": 1
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 404
    assert response.json().get('error') == "Book not found."
