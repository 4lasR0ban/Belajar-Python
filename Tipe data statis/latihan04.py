# latihan projek python 6

# input
C = float(input('Masukkan suhu (celcius): '))

# proses
    # Reamur
Re = 4/5*C
    # Romer
Ro = (C * 21/40) + 7.5
    # Kelvin
K = C + 273
    # Fahrenheit
F = (C * 9/5) + 32
    # Rankin
Ra = (C * 9/5) + 492
    # Newton
N = C * 33/100
    # Delisle
D = (672 - (C * 9/5) + 32) * 5/6

# output
print('Reamur     : ', Re)
print('Romer      : ', Ro)
print('Kelvin     : ', K)
print('Fahrenheit : ', F)
print('Rankin     : ', Ra)
print('Newton     : ', N)
print('Delisle    : ', D)
