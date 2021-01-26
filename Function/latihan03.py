# latihan projek python 3

def bintang(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print()
    for i in range(n):
        for j in range(n-i):
            print('*', end='')
        print()
