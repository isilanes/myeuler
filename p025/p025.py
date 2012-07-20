#-------------------------------------------------------------------------#

def f1():

    old, older = 1, 1
    index, digits = 2, 1
    while digits < 1000:
        index += 1
        old, older = old + older, old
        digits = len(str(old))

    return index

#-------------------------------------------------------------------------#

def f2():
    '''Adapted from ook!'s answer 30 dec 2005 @ projecteuler.net.'''
    max = 10**999 + 1

    a, b, c = 0, 1, 1
    while b < max:
        a, b, c = b, a + b, c + 1 

    return c

#-------------------------------------------------------------------------#

res = f2()
print(res)
