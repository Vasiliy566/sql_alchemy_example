import pytest

from app.services.please_test_me import max_number


@pytest.mark.parametrize(
    "a,b,c,r",
    [
        (1, 2, 3, 3),
        (2, 1, 3, 3),
        (3, 2, 1, 3),
        (10, 10, 10, 10)
    ]
)
def test_1(a, b, c, r):
    assert (max_number(a, b, c) == r)
