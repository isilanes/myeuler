#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def ncombos(pfactors):
        '''
        Return amount of valid (x,y) combos for a given z.
        '''

        pz = propers(pfactors+pfactors)
        return len(pz) + 1

    def primes(n):
        ps = []
        for i in range(2,n):
            while not n % i:
                ps.append(i)
                n = n / i
            if n == 1:
                return ps

    def propers(pfactors):
        '''
        Given prime factors pfactors, return list of all
        proper divisors.
        '''

        props = { 1: (1,) }
        for n in range(1,len(pfactors)):
            for combo in it.combinations(pfactors, n):
                fac = 1
                for e in combo:
                    fac = fac*e
                props[fac] = True

        return props.keys()

    combo = [2,3,5,7,11,13,17,19,23]               #                  9842
    combo = [2,2,3,5,7,11,13,17,19,23]             #                 16403
    combo = [2,2,3,3,5,7,11,13,17,19,23]           #    1338557220,  27338
    combo = [2,2,3,3,5,5,7,11,13,17,19,23]         #    6692786100,  45563
    combo = [2,2,3,3,5,5,7,7,11,13,17,19,23]       #   46849502700,  75938
    combo = [2,2,3,3,5,5,7,7,11,11,13,17,19,23]    #  515344529700, 126563
    combo = [2,2,3,3,5,5,7,7,11,11,13,13,17,19,23] # 
    d = (ncombos(combo) + 1)/2
    n = 1
    for e in combo:
        n = n * e
    print n, combo, d, d/4000*1000.0

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
