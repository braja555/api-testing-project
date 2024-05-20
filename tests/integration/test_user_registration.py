import requests

BASE_URL = 'http://localhost:3002'


def make_post_request(endpoint, payload):
    """Helper function to make a POST request to the given endpoint with the provided payload."""
    url = f"{BASE_URL}{endpoint}"
    response = None
    try:
        response = requests.post(url, json=payload)
    except:
        print("unable to call given endpoint" + url)
    finally:
        return response


def make_put_request(endpoint, payload, params):
    """Helper function to make a Put request to the given endpoint with the provided payload and params."""
    url = f"{BASE_URL}{endpoint}"
    response = None
    try:
        response = requests.put(url, json=payload, params=params)
    except:
        print("unable to call given endpoint" + url)
    finally:
        return response


def make_del_request(endpoint, params):
    """Helper function to make a Delete request to the given endpoint with the provided params."""
    url = f"{BASE_URL}{endpoint}"
    response = None
    try:
        response = requests.delete(url, params=params)
    except:
        print("unable to call given endpoint" + url)
    finally:
        return response


def test_user_registration_success():
    """Test successful user registration."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_new",
        "password": "Password123%",
        "email": "raja_babu_new@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 201
    assert response.json().get('message') == "User registered successfully."


def test_user_registration_missing_mandatoryfield_firstname():
    """Test registration failure due to missing firstname."""
    payload = {
        "lastname": "Babu",
        "username": "raja_babu_new",
        "password": "Password123%",
        "email": "raja_babu_new@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing required fields: firstname, lastname, username, password, email."


def test_user_registration_missing_mandatoryfield_lastname():
    """Test registration failure due to missing lastname."""
    payload = {
        "firstname": "Raja",
        "username": "raja_babu_new",
        "password": "Password123%",
        "email": "raja_babu_new@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing required fields: firstname, lastname, username, password, email."


def test_user_registration_missing_mandatoryfield_username():
    """Test registration failure due to missing username."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "password": "Password123%",
        "email": "raja_babu_new@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing required fields: firstname, lastname, username, password, email."


def test_user_registration_missing_mandatoryfield_password():
    """Test registration failure due to missing password."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_new",
        "email": "raja_babu_new@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing required fields: firstname, lastname, username, password, email."


def test_user_registration_missing_mandatoryfield_email():
    """Test registration failure due to missing email."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_new",
        "password": "Password123%"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Missing required fields: firstname, lastname, username, password, email."


def test_user_registration_invalid_email():
    """Test registration failure due to invalid email format."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_new",
        "password": "Password123%",
        "email": "raja_babu_newapi.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 400
    assert response.json().get('error') == "Invalid email format."


def test_user_registration_username_exist():
    """Test registration failure due to existing username."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_exist",
        "password": "Password123%",
        "email": "raja_babu_new@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 409
    assert response.json().get('error') == "Username already exists."


def test_user_registration_email_exist():
    """Test registration failure due to existing email."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_new",
        "password": "Password123%",
        "email": "raja_babu_exist@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 409
    assert response.json().get('error') == "Email already registered."


def test_user_registration_password_complexity():
    """Test registration failure due to weak password."""
    payload = {
        "firstname": "Raja",
        "lastname": "Babu",
        "username": "raja_babu_password",
        "password": "password",
        "email": "raja_babu_password@api.com"
    }
    response = make_post_request("/users/register", payload)
    assert response.status_code == 422
    assert response.json().get('error') == "Password is weak."


def test_user_update():
    """Test user details to update"""
    payload = {"firstname": "Raja", "lastname": "Babu", "username": "raja_babu_new", "password": "Password123%",
               "email": "raja_babu_new@api.com"}
    response = make_put_request("/users/register", payload, params={"id": "748efe2f-1087-4ec1-95c1-5a573dae041d"})
    assert response.status_code == 202
    assert response.json().get('message') == "User updated successfully."


def test_user_delete():
    """Test registration to delete the user"""
    response = make_del_request("/users/register", params={"id": "748efe2f-1087-4ec1-95c1-5a573dae041d"})
    assert response.status_code == 204


if __name__ == "__main__":
    test_user_registration_success()
    test_user_registration_missing_mandatoryfield_firstname()
    test_user_registration_missing_mandatoryfield_lastname()
    test_user_registration_missing_mandatoryfield_username()
    test_user_registration_missing_mandatoryfield_password()
    test_user_registration_missing_mandatoryfield_email()
    test_user_registration_invalid_email()
    test_user_registration_username_exist()
    test_user_registration_email_exist()
    test_user_registration_password_complexity()
    test_user_update()
    test_user_delete()
