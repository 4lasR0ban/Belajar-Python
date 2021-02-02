# latihan projek python

buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

def max(buah):
    tertinggi = max(buah['apel'], buah['jeruk'], buah ['mangga'], buah['duku'])
    print(tertinggi)

def plus(buah):
    tambah = buah['apel'] + buah['jeruk'] + buah ['mangga'] + buah['duku']
    rata2 = tambah/len(buah)
    print(rata2)
    
