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
    nmax = 2048000
    propers = {}
    for i in range(1,nmax+1):
        p = i*2
        while p < nmax+1:
            try:
                propers[p].append(i)
            except:
                propers[p] = [i]
            p += i

    def ncombos(z, propers):
        '''
        Return amount of valid (x,y) combos for a given z.
        '''

        combos = []
        for k in propers[z]:
            mn = z / k
            for m in propers[mn]:
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

    max_nc = 0
    ps = [2,3,5,7,11,13,17]
    for combo in [ ps[:2], ps[:3], ps[:4], ps[:5], ps[:6], ps[:7] ]:
            n = 1
            for c in combo:
                n = n*c
            nc = ncombos(n, propers)
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
