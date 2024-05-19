import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"  # Ensure this is set to the correct base URL


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def search_books_by_title(base_url):
    def _search(title):
        url = f"{base_url}/book/search"
        response = requests.get(url, params={"title": title})
        return response

    return _search


def test_book_search_success(search_books_by_title):
    response = search_books_by_title("1984")
    assert response.status_code == 200


def test_invalid_book_search(search_books_by_title):
    response = search_books_by_title("Nonexistent Book")
    assert response.status_code == 404
    assert response.json().get('message') == "No books found with the given title"


def test_book_query_required(search_books_by_title):
    response = search_books_by_title("")
    assert response.status_code == 400
    assert response.json().get('error') == "Title parameter is required"
