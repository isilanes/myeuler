#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")
    i = 1
    while True:
        idigits = f1_1(i)
        valid = True
        for mult in [2,3,4,5,6]:
            imult = i * mult
            imultdigits = f1_1(imult)
            if imultdigits != idigits:
                valid = False
                break
        if valid:
            for mult in [1,2,3,4,5,6]:
                print(i*mult)
            break

        i += 1

#--------------------------------------------------------------------#

def f1_1(N):
    '''
    Take integer N and return sorted array of digits. Example:

    N = 145232
    return [1, 2, 2, 3, 4, 5]
    '''

    digs = [ x for x in str(N) ]
    digs.sort()
    return digs

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 0.4 s
