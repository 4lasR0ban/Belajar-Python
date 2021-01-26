# latihan projek python 5

def isPrime(x):
    if x>1:
        for i in range(2,x):
            if(x%i) == 0:
                return False
        else:
            return True
    else:
        return False
