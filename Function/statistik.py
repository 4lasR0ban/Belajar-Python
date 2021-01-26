# latihan projek Python 6,7

def sum(*myData):
    sum = 0
    i = 0
    for data in myData:
        sum += data
        i += 1
    return sum

def average(*myData):
    sum = 0
    i = 0
    for data in myData:
        sum += data
        i += 1

    average = sum/i
    print(average)

def maks(*myData):
    maks = myData[0]
    for data in myData:
        if data > maks:
            maks = data
    return maks

def min(*myData):
    min = myData[0]
    for data in myData:
        if data < min:
            min = data
    return min
