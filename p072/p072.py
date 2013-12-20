#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    # For each denominator, when the numerator is not coprime, the
    # fraction will not be reduced proper (it will be posible to
    # divide numerator and denominator by the common divisor(s)).
    # This means each denominator N provides phi(N) distinct fractions.
    # So, the result the problem asks is the sum of phi(n)s for all
    # n from 2 to N.

    def get_primes(nmax):
        primes = {2:True}
        composites = {}
        for mult in range(3,nmax,2):
            if not mult in composites:
                # Log mult as prime:
                primes[mult] = True

                # Sieve its multiples away:
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        return primes

    def phi(N, primes, plist):
        if N in primes:
            return N - 1
        res = N
        for prime in plist:
            if not N % prime:
                N = N / prime
                res = res * (prime - 1) / prime
                if N == 1:
                    return res
            while not N % prime:
                N = N / prime
                if N == 1:
                    return res

    ndistinct = 0
    nmax = 1000*1000
    primes = get_primes(nmax)
    plist = sorted(primes.keys())
    for num in range(2,nmax+1):
        ndistinct += phi(num, primes, plist)

    print ndistinct

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): ~ 61 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
