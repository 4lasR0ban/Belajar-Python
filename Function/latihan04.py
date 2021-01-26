# latihan projek python 4

def faktorial(n):
    fact = 1
    for num in range(2, n+1):
        fact *= num
    return fact

def C(a,b):
    kombinatorik = faktorial(a)/faktorial(b)*faktorial(a-b)
    print(kombinatorik)

def P(a,b):
    permutasi = faktorial(a)/faktorial(a-b)
    print(permutasi)
