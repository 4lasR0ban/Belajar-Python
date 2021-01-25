# latihan projek python 1,2,3

# input
n = int(input('Jumlah kamar: '))

p_kamar = int(input('Panjang kamar: '))
l_kamar = int(input('Lebar kamar: '))

pkeramik = int(input('Panjang keramik: '))
lkeramik = int(input('Lebar keramik: '))

# proses
    # mengubah meter ke cm
pkamar = p_kamar * 100
lkamar = l_kamar * 100

    # menghitung luas lantai sebuah kamar tidur
luas1Kamar = pkamar * lkamar

    # menghitung luas total seluruh kamar tidur
luasTotal = luas1Kamar * n

    # menghitung luas sebuah keramik
luasKeramik = pkeramik * lkeramik

    # menghitung jumlah keramik yang diperlukan
jmlKeramik = luasTotal / luasKeramik

    # menghitung jumlah box
jmlBox = jmlKeramik / 5

    # menghitung cadangan keramik & total box
cadanganKeramik = jmlKeramik * 0.1
totalBox = (cadanganKeramik + jmlKeramik)/5

    # menghitung biaya
biaya = totalBox * 125000

# output
print('Jumlah keramik: ', int(jmlKeramik))
print('Jumlah Box: ', int(jmlBox))
print('Jumlah Box ditambah dengan box cadangan: ', int(totalBox))
print('Total biaya: ', int(biaya))
