import requests

BASE_URL = "http://127.0.0.1:5000"  # Ensure this is set to the correct base URL


def check_200(response):
    assert response.status_code == 200

def check_404(response):
    assert response.status_code == 404
    assert response.json().get('message') == "No books found with the given title"

def check_400(response):
    assert response.status_code == 400
    assert response.json().get('error') == "Title parameter is required"

def test_search_books_by_title(title: str) -> None:
    url = f"{BASE_URL}/book/search"
    response = requests.get(url, params={"title": title})
    return response

if __name__ == "__main__":
    response = test_search_books_by_title("1984")
    check_200(response)
    response = test_search_books_by_title("Nonexistent Book")
    check_404(response)
    response = test_search_books_by_title("")
    check_400(response)
