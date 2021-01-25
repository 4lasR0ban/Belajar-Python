# latihan projek python 7,8

from random import randint

print('Saya telah memilih sebuah bilangan bulat secara acak')
print('antara 0 s/d 100. Silahkan tebak yaa!!')

# komputer random input
answer = randint(0,100)

# player input
guess = int(input('Tebakan anda: '))

# sistem
skor = 100
while guess >= 0:
    if guess > answer:
        print('Bilangan tebakan anda terlalu besar')
        guess = int(input('Tebakan anda: '))
        skor -= 2
    elif guess < answer:
        print('Bilangan tebakan anda terlalu kecil')
        guess = int(input('Tebakan anda: '))
        skor -= 2
    elif guess == answer:
        print('Bilangan tebakan anda BENAR!')
        print('Score anda: ', skor
              )
        break
else:
    print('Masukkan angka')
    guess = int(input('Tebakan anda: '))


