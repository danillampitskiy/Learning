import requests

def test_get_beer():
    response = requests.get("https://api.punkapi.com/v2/beers/8")
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == "Fake Lager"
    assert data[0]['abv'] == 4.7

def test_delete_beer():
    response = requests.delete("https://api.punkapi.com/v2/beers/8")
    data = response.json()

    assert response.status_code == 404
    assert data['message'] == "No endpoint found that matches '/v2/beers/8'"