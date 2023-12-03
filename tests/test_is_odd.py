from odd import is_odd


def test_sanity():
    assert is_odd(9)
    assert not is_odd(10)
    assert not is_odd(0)


def test_sanity_negative():
    assert is_odd(-9)
    assert not is_odd(-10)


def test_multiple_true():
    for i in range(-999_999, 1_000_000, 2):
        assert is_odd(i)


def test_multiple_false():
    for i in range(-1_000_000, 1_000_000, 2):
        assert not is_odd(i)
