import requests

def test_github_api_status():
    url = "https://api.github.com"
    response = requests.get(url)
    assert response.status_code == 200

