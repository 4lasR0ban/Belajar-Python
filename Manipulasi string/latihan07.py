# latihan projek python

mhs = ['K001:VERO BAGUS WARDANA:2002-11-24:BOGOR',
       'K002:NARUTO UZUMAKI:2002-10-17:JAKARTA',
       'K003:KILUA ZOLDYCK:2005-06-11:YOGYAKARTA']

print(80*"=")
print('NIM'.ljust(7, ' '), 'NAMA MAHASISWA'.ljust(20, ' '),
      'TGL LAHIR'.rjust(20, ' '), 'TEMPAT LAHIR'.rjust(20, ' '))
print(80*"-")
for data in mhs:
    newdata = data.split(':')
    tgl = newdata[2].split('-')
    nim = newdata[0]
    nama = newdata[1]
    tempat = newdata[3]

    print(nim.ljust(7, ' '), nama.ljust(20, ' '),
          (tgl[2]+'/'+tgl[1]+'/'+tgl[0]).rjust(20, ' '),
          tempat.rjust(20, ' '))
print(80*"-")
