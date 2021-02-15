# latihan projek python

def shufflestring(x, n):
    import random
    result = []
    for i in range(n):
        shuffle = ''.join(random.sample(x,len(x)))
        result.append(shuffle)
    return result
