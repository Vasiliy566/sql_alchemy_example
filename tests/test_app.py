import pytest
from fastapi.testclient import TestClient
from main import app


test_app = TestClient(app)


@pytest.mark.parametrize(
    "a,b,res", [
        (1, 2, 3),
        (3, 2, 5),
        (101, 102, 203),
    ]
)
def test_floyd(a, b, res):
    r = test_app.get("/sum", params={"a": a, "b": b})
    assert r.text == str(res)
