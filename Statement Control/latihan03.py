# latihan projek python 5

hitung = 0
sum = 0
for i in range(100):
    bil = i+1
    if bil%2==1:
        hitung += 1
        sum += bil
        print(bil)

print('Banyaknya bilangan ganjil: '+ str(hitung))
print('Jumlah bilangan          : '+ str(sum))
