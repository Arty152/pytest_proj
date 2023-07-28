from utils import dicts

def test_get_val():
    data = {'pytest': 'good'}
    assert dicts.get_val(data, 'pytest') == 'good'
    assert dicts.get_val({}, 'pytest') == 'git'
    assert dicts.get_val({}, 'pytest', 'git') == 'git'
    assert dicts.get_val({}, 'pytest', 'github') == 'github'