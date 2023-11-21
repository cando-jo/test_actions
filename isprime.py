from math import sqrt

def is_prime(n):
    if n < 3:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
        
    return True


        