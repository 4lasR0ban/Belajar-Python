# latihan projek python 7

# input
st = int(input('Berapa Kg stroberi: '))
j = int(input('Berapa Kg jeruk   : '))
an = int(input('Berapa Kg anggur  : '))
ap =int(input('Berapa Kg apel    : '))
se = int(input('Berapa Kg semangka: '))

# proses
    # harga
stroberi = 30000
jeruk = 15000
anggur = 42000
apel = 38000
semangka = 21000

    # menghitung
st_harga = stroberi * st
j_harga = jeruk * j
an_harga = anggur * an
ap_harga = apel * ap
se_harga = semangka * se


totalHarga = st_harga + j_harga + an_harga + ap_harga + se_harga

# output
print('Total harga keseluruhan buah adalah: ', totalHarga)
