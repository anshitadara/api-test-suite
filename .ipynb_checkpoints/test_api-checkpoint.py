import requests

BASE_URL = "https://api.github.com"

def test_github_api_status():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_github_api_headers():
    response = requests.get(BASE_URL)
    assert "application/json" in response.headers["Content-Type"]

def test_github_user_endpoint():
    response = requests.get(f"{BASE_URL}/users/octocat")
    assert response.status_code == 200
    assert response.json()["login"] == "octocat"