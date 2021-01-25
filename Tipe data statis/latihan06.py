# latihan projek python 8

# input
st = int(input('Berapa Kg stroberi: '))
j = int(input('Berapa Kg jeruk   : '))
an = int(input('Berapa Kg anggur  : '))
ap =int(input('Berapa Kg apel    : '))
se = int(input('Berapa Kg semangka: '))

# proses
    # harga beli
st_beli = 25000
j_beli = 12500
an_beli = 39000
ap_beli = 35500
se_beli = 19200

    # harga jual
st_jual = 30000
j_jual = 15000
an_jual = 42000
ap_jual = 38000
se_jual = 21000

    # menghitung harga buah dari data harga jual
st_hjual = st_jual * st
j_hjual = j_jual * j
an_hjual = an_jual * an
ap_hjual = ap_jual * ap
se_hjual = se_jual * se

    # menghitung harga buah dari data harga beli
st_hbeli = st_beli * st
j_hbeli = j_beli * j
an_hbeli = an_beli * an
ap_hbeli = ap_beli * ap
se_hbeli = se_beli * se

totalHargaJual = st_hjual + j_hjual + an_hjual + ap_hjual + se_hjual
totalHargaBeli = st_hbeli + j_hbeli + an_hbeli + ap_hbeli +se_hbeli
profit = totalHargaJual - totalHargaBeli

# output
print('Total harga keseluruhan buah adalah: ', totalHargaJual)
print('Profit yang didapat pedagang adalah: ', profit)
