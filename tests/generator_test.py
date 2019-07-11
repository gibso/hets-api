def test_hello(client):
    response = client.get('/generator/hello')
    assert response.data == b'Hello, World!'