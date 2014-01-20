#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math
    import itertools as it

    def ncombos2(n):
        '''
        Return amount of valid (x,y) combos for a given n.
        '''

        combos = []
        for N in range(1,n):
            if N*N > n:
                break
            for k in range(1,n):
                if not n % (k*N):
                    M = n / (k*N)
                    x = k*M*(M+N)
                    y = k*N*(M+N)
                    c = [x,y]
                    c.sort()
                    if not c in combos:
                        combos.append(c)

        return len(combos)
    
    # Find proper divisors of all numbers up to max, using a sieve:
    nmax = 20480
    propers = {}
    for i in range(1,nmax+1):
        p = i*2
        while p < nmax+1:
            try:
                propers[p].append(i)
            except:
                propers[p] = [i]
            p += i

    def ncombos(z, propsz):
        '''
        Return amount of valid (x,y) combos for a given z.
        '''

        combos = []
        for k in propsz:
            mn = z / k
            propsmn = propsz[:]
            if k != 1:
                propsmn.remove(k)
            for m in propsmn:
                if m*m > mn:
                    break
                n = mn/m
                x = k * m * (m+n)
                y = k * n * (m+n)
                if not [x,y] in combos:
                    combos.append([x,y])

        return len(combos)
    
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

        props = [1]
        for n in range(1,len(pfactors)):
            for combo in it.combinations(pfactors, n):
                fac = 1
                for e in combo:
                    fac = fac*e
                props.append(fac)

        return list(set(props))

    ps = [2,2,3,3,5,5,7,7,11,11,13,13,17,17]
    ps = [2,3]
    max_nc = 0
    for N in range(2,3):
        for combo in it.combinations(ps, N):
            n = 1
            for c in combo:
                n = n*c
            props = propers(combo)
            nc = ncombos(n, props)
            if nc > max_nc:
                max_nc = nc
                print n, nc, combo

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
