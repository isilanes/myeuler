import math
import timeit

#------------------------------------------------------------------------------#

def f0(maxp1):
    print("--- f0 ---")

    def get_primes(nmax):
        # Sieve to find all primes up to nmax:
        composites = {}
        primes = [2]
        for mult in range(3,nmax,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        return primes


    ps = get_primes(maxp1+100)
    while True:
        if ps[-1] > maxp1:
            if ps[-2] < maxp1:
                break
            else:
                ps.pop()
        else:
            print("error")
            return

    SS = 0
    for i in range(2,len(ps)-1): # from 5 on
        p1 = ps[i]
        p2 = ps[i+1]
        j = int(math.log10(p1)) + 1
        N = 1
        while True:
            S = N*10**j
            if S % p2 == (p2 - p1):
                SS += S + p1
                break
            N += 1

    print(SS)

def f1(maxp1):
    '''Like f0, but take 10**j out of unnecessary loop.'''

    print("--- f1 ---")

    def get_primes(nmax):
        # Sieve to find all primes up to nmax:
        composites = {}
        primes = [2]
        for mult in range(3,nmax,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        return primes


    ps = get_primes(maxp1+1000)
    while True:
        if ps[-1] > maxp1:
            if ps[-2] < maxp1:
                break
            else:
                ps.pop()
        else:
            print("error")
            return

    SS = 0
    for i in range(2,len(ps)-1): # from 5 on
        p1 = ps[i]
        p2 = ps[i+1]
        j = int(math.log10(p1)) + 1
        e = 10**j
        N = 1
        while True:
            S = N*e
            if S % p2 == (p2 - p1):
                SS += S + p1
                break
            N += 1

    print(SS)


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}(10**6)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxp1  t (ms)
#        100       0.6
#       1000       7
#      10000     150
#     100000    8750
#    1000000  682755

# f1:  maxp1  t (ms)
#        100       1
#       1000       6
#      10000      73
#     100000    3800
#    1000000  314497

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
