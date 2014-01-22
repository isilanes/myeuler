#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math
    import itertools as it

    def isprime(num):
        '''
        Returns True if num is prime, False otherwise.
        '''

        # Only odd numbers are fed to this function, so no need
        # to check num % 2:
        for i in range(3,int(math.sqrt(num))+2,2):
            if not num % i:
                return False

        return True

    # Number of digits we check for (10 in p111):
    N = 10

    # TS4d  =       273700 (     31 ms)
    # TS5d  =      5630641 (     54 ms)
    # TS6d  =     43058225 (     90 ms)
    # TS7d  =   1143408516 (    712 ms)
    # TS8d  =   4060851254 (   2572 ms)
    # TS9d  =  41880229159 (  23887 ms)
    # TS10d = 594629790343 ( 311891 ms)

    TSNd = 0
    for d in range(10):
        nd = N-1
        others = [0,1,2,3,4,5,6,7,8,9]
        others.remove(d)
        while True:
            SNd = 0

            nothers = N - nd
            permus = []
            for combo in it.permutations(others, nothers):
                for permu in it.permutations((d,)*nd+combo, N):
                    if permu[-1] in [1,3,7,9]: # else, can't be prime
                        if permu[0] != 0: # else, has N-1 digits or less
                            num = ''.join([ str(x) for x in permu ])
                            num = int(num)
                            permus.append(num)
            permus = sorted(set(permus))
            for num in permus:
                if isprime(num):
                    SNd += num

            if SNd == 0:
                nd -= 1
            else:
                print(d, nd, SNd)
                TSNd += SNd
                break

    print(TSNd)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
