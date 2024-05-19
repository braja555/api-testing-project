import requests

BASE_URL = 'http://localhost:3002'

def make_request(endpoint, payload):
    """Helper function to make a POST request to the given endpoint with the provided payload."""
    url = f"{BASE_URL}{endpoint}"
    print(url)
    print(payload)
    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.json())
    return response

def test_user_login_success():
    """Test successful user login."""
    payload = {
        "username": "raja_babu",
        "password": "Password123%"
    }
    response = make_request("/users/login", payload)
    assert response.status_code == 200
    assert 'token' in response.json()
    assert response.json().get('message') == "Login successful."

def test_user_login_missing_username():
    """Test login failure due to missing username."""
    payload = {
        "username": "",
        "password": "Password123%"
    }
    response = make_request("/users/login", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing username or password."

def test_user_login_missing_password():
    """Test login failure due to missing password."""
    payload = {
        "username": "raja_babu",
        "password": ""
    }
    response = make_request("/users/login", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing username or password."

def test_user_login_blocked_user():
    """Test login failure due to a blocked user."""
    payload = {
        "username": "BlockedUser",
        "password": "Password123%"
    }
    response = make_request("/users/login", payload)
    assert response.status_code == 403
    assert response.json().get('error') == "Permission not granted for the entered user."


if __name__ == "__main__":
    test_user_login_success()
    test_user_login_missing_username()
    test_user_login_missing_password()
    test_user_login_blocked_user()
