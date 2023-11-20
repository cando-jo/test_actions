from asserts import square


def test_square():
    assert square(5) == 25
    assert square(2) == 4
    assert square(1) == 1
    assert square(0) == 0
    assert square(-2) == 4
    assert square(-4) == 16
    

