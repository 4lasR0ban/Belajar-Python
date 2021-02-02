# latihan projek python

daftarBuah = {'apel' : 5000,
              'jeruk' : 8500,
              'mangga' : 7800,
              'duku' : 6500}

while True:
    # tampilkan menu
    print('-'*50)
    print('Menu: ')
    print('1. Tambah data buah')
    print('2. Hapus data buah')
    print('3. Beli buah')
    print('4. Keluar')
    print('='*50)
    pilihan = int(input('Pilihan anda: '))

    if pilihan == 1:
        tambahBuah = input('Masukkan nama buah    : ')
        hargaBuah = input('Masukkan harga satuan : ')
        if tambahBuah not in daftarBuah:
            daftarBuah[tambahBuah] = hargaBuah
            for buah in daftarBuah:
                print(buah, '(Harga Rp ', daftarBuah[buah],')')
        elif tambahBuah in daftarBuah:
            print('Maaf buah sudah dalam daftar')

    elif pilihan == 2:
        namaBuah = input('Buah yang akan dihapus: ')
        if namaBuah in daftarBuah:
            del daftarBuah[namaBuah]
            print(namaBuah, 'Sudah dihapus dalam daftar')
        elif namaBuah not in daftarBuah:
            print(namaBuah, 'tidak ada dalam daftar')

    elif pilihan == 3:  
        # nilai awal total pembelian
        totalHarga = 0

        while True:
            fruit = input('Nama buah yang dibeli : ')
            kg = int(input('Berapa Kg             : '))
            harga = daftarBuah[fruit]
            # harga dijumlahkan
            totalHarga += kg * harga
            jwb = input('Beli buah yang lain (y/n): ')
            if jwb == 'n':
                break
        print('-'*50)
        print('Total harga           : ', totalHarga)

    elif pilihan == 4:
        break
    else:
        print('Pilihan salah')
