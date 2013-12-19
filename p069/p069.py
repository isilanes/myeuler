#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def get_primes(max):
        # Sieve to find all primes up to max:
        composites = {}
        primes = [2]
        for mult in range(3,max,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, max, 2*mult):
                    composites[i] = True

        return primes

    def factors_of(num, primes):
        '''
        Return prime factors of number num.
        '''

        factors = []
        for prime in primes:
            if not num % prime:
                factors.append(prime)
                num = num / prime
                if num == 1:
                    break

        return factors

    nmax = 2311
    primes = get_primes(nmax)

    max_q = 0
    max_n = None
    for n in range(2,nmax):
        toti = 1.0
        factors = factors_of(n, primes)
        for i in range(2,n):
            coprime = True
            for factor in factors:
                if not i % factor:
                    coprime = False
                    break
            if coprime:
                toti += 1
        q = n/toti
        if q > max_q:
            max_q = q
            max_n = n
            print n, n/toti

    print(max_n, max_q)

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    def get_primes(max):
        # Sieve to find all primes up to max:
        composites = {}
        primes = [2]
        for mult in range(3,max,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, max, 2*mult):
                    composites[i] = True

        return primes

    def factors_of(num, primes):
        '''
        Return prime factors of number num.
        '''

        factors = []
        for prime in primes:
            if not num % prime:
                factors.append(prime)
                num = num / prime
                if num == 1:
                    break

        return factors

    nmax = 2311
    primes = get_primes(nmax)

    max_q = 0
    max_n = None
    for n in range(2,nmax):
        factors = factors_of(n, primes)
        noncoprimes = {}
        for factor in factors:
            for i in range(1,n/factor):
                num = i*factor
                noncoprimes[num] = True

        toti = n - len(noncoprimes.keys()) - 1.0
        q = n/toti
        if q > max_q:
            max_q = q
            max_n = n
            print n, q

    print(max_n, max_q)

#--------------------------------------------------------------------#

def f2():
    print("--- f2 ---")

    def get_primes(max):
        # Sieve to find all primes up to max:
        composites = {}
        primes = [2]
        for mult in range(3,max,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, max, 2*mult):
                    composites[i] = True

        return primes

    def factors_of(num, primes):
        '''
        Return prime factors of number num.
        '''

        factors = []
        for prime in primes:
            if not num % prime:
                factors.append(prime)
                num = num / prime
                if num == 1:
                    break

        return factors

    nmax = 30031
    primes = get_primes(nmax)

    max_q = 0
    max_n = 0
    for n in range(2,nmax):
        toti = 1.0
        factors = factors_of(n, primes)
        cont = False
        for i in range(2,n):
            coprime = True
            for factor in factors:
                if not i % factor:
                    coprime = False
                    break
            if coprime:
                toti += 1
                if toti*max_q > n:
                    cont = True
                    break
        if cont:
            continue

        q = n/toti
        if q > max_q:
            max_q = q
            max_n = n
            print n, n/toti

    print(max_n, max_q)

#--------------------------------------------------------------------#

def f3():
    print("--- f3 ---")

    nmax = 1000000

    res = 2
    mult = 3
    composites = {}
    while True:
        if not mult in composites:
            res = res * mult
            if res > nmax:
                res = res / mult
                break
            for i in range(mult*mult, nmax, 2*mult):
                composites[i] = True
        mult += 2

    print res

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(3,4):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#--------------------------------------------------------------------#

#
# f0(): too slow (~33 s for N = 30030)
# f1(): even slower (~52 s for N = 30030)
# f2(): faster (~16 s for N = 30030)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
