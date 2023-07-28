from utils import arrs
import pytest


@pytest.mark.parametrize('array, index, deafult, expected', [
    ([1, 2, 3], 1, "test", 2),
    ([], -1, "test", "test")
])
def test_get(array, index, deafult, expected):
    assert arrs.get(array, index, deafult) == expected


@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([], 1, None, []),
    ([1, 2, 3, 4, 5], -2, None, [4, 5]),
    ([1, 2, 3, 4], -8, 3, [1, 2, 3])
])
def test_slice(coll, start, end, expected):
    assert arrs.my_slice(coll, start, end) == expected