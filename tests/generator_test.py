from flask_api import status

def test_hello(client):
    response = client.get('/generator/th')
    assert response.status_code == status.HTTP_204_NO_CONTENT