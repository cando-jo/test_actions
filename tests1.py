from isprime import is_prime
def test_1():
    assert is_prime(1) == False
    
def test_2():
    assert is_prime(2) == True
    
def test_25():
    assert is_prime(25) == False
        
def test_7():
    assert is_prime(7) == True
        
def test_9():
    assert is_prime(9) == False

def test_5():
    assert is_prime(5) == True    
