from app.square import square


def test_positive():
    assert square(5) == 25
    assert square(2) == 4
    assert square(1) == 1
def test_zero():
    assert square(0) == 0
    
def test_negative():
    assert square(-2) == 4
    assert square(-4) == 16

    

