# latihan projek python 3,4

# input
kode = input('Masukkan kode karyawan: ')
nama = str(input('Masukkan nama karyawan: '))
gol = str(input('Masukkan golongan     : '))
nikah= int(input('Masukkan status (1: menikah; 2: blm): '))
if nikah == 1:
    anak = int(input('Masukkan jumlah anak  : '))
    stat = 'Menikah'
if nikah == 2:
    stat = 'Belum menikah'
elif nikah != 1 or nikah != 2:
    print('Maaf terdapat kesalahan input')
    
print('======================================')

print('STRUKTUR RINCIAN GAJI KARYAWAN')

print('--------------------------------------')

print("Nama Karyawan         : ", nama, "(Kode: ", kode,")")
print("Golongan              : ", gol)
print("Status menikah        : ", stat)
if nikah == 1:
    print("Jumlah anak           : ", anak)

print('--------------------------------------')

# proses
while True:
    if gol == 'A':
        gajiPokok = 10000000
        potongan = '2.5%'
        pot = 0.025
    if gol == 'B':
        gajiPokok = 8500000
        potongan = '2.0%'
        pot = 0.02
    if gol == 'C': 
        gajiPokok = 7000000
        potongan = '1.5%'
        pot = 0.015
    if gol == 'D':
        gajiPokok = 5000000
        potongan = '1.0%'
        pot = 0.01
    else:
        print('masukkan golongan A/B/C/D dengan huruf kapital')
    break

if nikah == 1:
    subPair = gajiPokok*0.01
    if anak > 0:
        subChild = gajiPokok*0.05*anak
    else:
        subChild = 0
else:
    subPair = 0
    subChild = 0

cut = gajiPokok*pot
gajiKotor = gajiPokok + subPair + subChild
gajiBersih = gajiKotor - cut


# output
print('Gaji pokok            : Rp', gajiPokok)
if nikah == 1:
    print('Tunjangan istri/suami : Rp', subPair)
    print('Tunjangan anak        : Rp', subChild)
    print('--------------------------------------')
print('Gaji kotor            : Rp', gajiKotor)
print('Potongan (',potongan,')     : Rp', cut)

print('--------------------------------------')

print('Gaji bersih           : Rp', gajiBersih)
