from flask import Flask, request, jsonify

BASE_URL = 'http://localhost:3002'

def test_user_registration_success():
    url = f"{BASE_URL}/users/register"
    payload = {
        "username": "testuser",
        "password": "password123",
        "email": "testuser@example.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json().get('message') == "User registered successfully."

if __name__ == "__main__":
    test_user_registration_success()