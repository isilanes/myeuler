#--------------------------------------------------------------------#

def f0():
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

    Nmax = 50*1000*1000 - 1
    pmax = 8000
    primes = get_primes(pmax)
    tups = {}
    for p1 in primes:
        res = p1**4
        if res > Nmax:
            break
        for p2 in primes:
            res = p1**4 + p2**3
            if res > Nmax:
                break
            for p3 in primes:
                res = p1**4 + p2**3 + p3**2
                if res > Nmax:
                    break
                tups[res] = True

    print(len(tups.keys()))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 0.7 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
