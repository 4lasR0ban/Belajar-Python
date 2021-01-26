# latihan projek python 9

def dec2Bin(n):
    step = n
    biner = ''
    while step != 1:
        sisa = step % 2
        step = step // 2
        biner = str(sisa) + biner
    biner = "1" + biner
    return biner
