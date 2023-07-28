import pytest
from utils import dicts

test_data = {'pytest': 'good'}


@pytest.mark.parametrize('collection, key, deafult, expected', [
    (test_data, 'pytest', 'git', 'good'),
    ({}, 'pytest', 'git', 'git'),
    ({}, 'pytest', 'github', 'github')
])
def test_get_val(collection, key, deafult, expected):
    assert dicts.get_val(collection, key, deafult) == expected