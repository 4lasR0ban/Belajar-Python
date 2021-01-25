# latihan projek python 1,2

# input
bindo = int(input('Masukkan nilai Bhs Indonesia: '))
mtk   = int(input('Masukkan nilai Matematika   : '))
ipa   = int(input('Masukkan nilai IPA          : '))

# proses & output
while bindo >= 0 or mtk >= 0 or ipa >= 0:
    if bindo < 60 or mtk < 70 or ipa < 60:
        status = 'TIDAK LULUS'
        break
    else:
        status = 'LULUS'
        break
else:
    print('MAAF NILAI TIDAK DAPAT DIPROSES')

print('Status kelulusan            : ', status)    

while status == 'TIDAK LULUS':
    print('Sebab                       : ')
    if bindo < 60:
        print('Nilai Bhs Indonesia kurang dari 60')
    if mtk < 70:
        print('Nilai Matematika kurang dari 70')
    if ipa < 60:
        print('Nilai IPA kurang dari 60')
    break


