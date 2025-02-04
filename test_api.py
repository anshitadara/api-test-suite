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


def test_get_valid_response():
    response = requests.get(f"{BASE_URL}/endpoint")
    assert response.status_code == 200
    assert "expected_key" in response.json()

def test_get_invalid_response():
    response = requests.get(f"{BASE_URL}/wrong-endpoint")
    assert response.status_code == 404

def test_post_invalid_data():
    response = requests.post(f"{BASE_URL}/endpoint", json={"wrong_key": "value"})
    assert response.status_code == 400

import requests

def test_get_valid_response():
    response = requests.get(f"{BASE_URL}/endpoint")
    assert response.status_code == 200  # Expecting success
    assert "expected_key" in response.json()  # Check response body

def test_post_invalid_data():
    payload = {"wrong_key": "value"}  # Invalid input
    response = requests.post(f"{BASE_URL}/endpoint", json=payload)
    assert response.status_code == 400  # Expecting bad request

def test_post_valid_data():
    payload = {"correct_key": "valid_value"}  # Correct input
    response = requests.post(f"{BASE_URL}/endpoint", json=payload)
    assert response.status_code == 201  # Expecting created

