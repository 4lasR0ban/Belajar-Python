# latihan projek python 3

# star formation 1
def bintangA(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print()

# star formation 2
def bintangB(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end='')
        print()

# star formation gabungan
def bintangC(n):
    bintangA(n//2)
    bintangB(n-n//2)
