# latihan projek python

sayur = ['bayam', 'kangkung', 'wortel', 'selada']

print('Menu:')
print('1. Tambah data sayur')
print('2. Hapus data')
print('3. Tampilkan data sayur')
tambah = 1
hapus = 2
show = 3
choice = int(input('Pilihan anda: '))

while True:
    if choice == 1:
        x = str(input('Tambah data sayur: '))
        sayur = sayur + [x]
        print(sayur)
        break
    if choice == 2:
        x = str(input('Sayur yang akan dihapus: '))
        sayur.remove(x)
        print(sayur)
        break
    if choice == 3:
        print(sayur)
        break
else:
    print('Maaf input salah')
