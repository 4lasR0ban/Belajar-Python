# latihan projek python 1

def max(*data):
    maks = data[0]
    for x in data:
        if x > maks:
            maks = x
    return maks
