# latihan projek python 10

# input
noKomputer = input('Masukkan No Komputer: ')

print('----------------------------------')

print('Waktu Mulai Akses')
jam0 = int(input('Jam       :'))
menit0 = int(input('Menit     :'))
detik0 = int(input('Detik     :'))

print('----------------------------------')

print('Waktu Selesai Akses')
jam1 = int(input('Jam       :'))
menit1 = int(input('Menit     :'))
detik1 = int(input('Detik     :'))

print('----------------------------------')

# proses
awal = jam0 * 3600 + menit0 * 60 + detik0
akhir = jam1 * 3600 + menit1 * 60 + detik1

if awal < akhir:
    durasi = akhir - awal
else:
    durasi = (akhir+24*3600)-awal

    # konversi
durasiJam = durasi/3600
durasiMenit = (durasi%3600)/60
durasiDetik = durasi%60

    # biaya
biaya = durasi/1800*2250


# output
print("Total waktu akses: %d jam %d menit %d detik" % (durasiJam, durasiMenit, durasiDetik))
print('Total biaya akses No Komputer', noKomputer,': Rp', biaya)

