import pytest, os, json
from ASCIIArt import ascii_server as flask_app

@pytest.fixture()
def app():
    flask_app.config.update({
        "TESTING": True,
    })

    yield flask_app


@pytest.fixture()
def client(app):
    app.testing = True
    return app.test_client()

def test_unsupported_method(client):
    response = client.get("/ascii/convert")
    assert response.status_code == 405

def test_no_file_part_in_request(client):
    response = client.post("/ascii/convert")
    assert response.status_code == 400

def test_no_filename(client):
    response = client.post("/ascii/convert", data={"file": None})
    assert response.status_code == 400

def test_unsupported_file_extension(client):
    image = open(os.path.dirname(__file__) + r'\Images\mona_lisa.png', 'rb')
    response = client.post("/ascii/convert", data={"file": image})
    assert response.status_code == 400

def test_successful_conversion(client):
    image = open(os.path.dirname(__file__) + r'\Images\mona_lisa.jpg', 'rb')
    response = client.post("/ascii/convert", data={"file": image})
    assert response.status_code == 200
    assert 'ascii' in json.loads(response.data.decode("utf-8"))
    
