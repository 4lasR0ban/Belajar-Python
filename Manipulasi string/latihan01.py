# latihan projek python

def statHuruf(s):
    s = s.lower()
    dataHuruf = list(set(s))
    dataHuruf.sort()
    dictHuruf = {}
    for huruf in dataHuruf:
        dictHuruf[huruf] = 0
    for huruf in s:
        dictHuruf[huruf] += 1
    return dictHuruf
