import requests

BASE_URL = 'http://localhost:3001'

def test_search_books_success():
    url = f"{BASE_URL}/books"
    query = "Harry Potter"
    response = requests.get(url, params={"search": query})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    # Add more assertions based on your expected response format

def test_search_books_no_results():
    url = f"{BASE_URL}/books"
    query = "Nonexistent Book"  # Example search query with no results
    response = requests.get(url, params={"search": query})
    assert response.status_code == 404
    assert response.json().get('error') == "No books found."

