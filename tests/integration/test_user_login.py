import requests

BASE_URL = 'http://localhost:3001'

def test_user_login_success():
    url = f"{BASE_URL}/users/login"
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert 'token' in response.json()
    assert response.json().get('message') == "Login successful."

def test_user_login_invalid_credentials():
    url = f"{BASE_URL}/users/login"
    payload = {
        "username": "invaliduser",
        "password": "wrongpassword"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 401
    assert response.json().get('error') == "Invalid credentials."
