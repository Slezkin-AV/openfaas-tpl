
import pytest
import index

@pytest.fixture
def app():
    app = index.create_app()
    app.debug = True
    return app.test_client()

def test_handle(app):
    res = app.get("/")
    assert res.status_code == 200
    assert b"Hello from OpenFaaS!" == res.data
    pass