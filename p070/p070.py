#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math

    def phi(n, ps):
        res = n
        for p in ps:
            res = res * (p - 1)  / p
        return res

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

    def factors_of(num, primes):
        '''
        Return distinct prime factors of number num.
        '''

        factors = []
        for prime in primes:
            if not num % prime:
                factors.append(prime)
                while not num % prime:
                    num = num / prime
                if num == 1:
                    return factors

        return factors

    def are_permu(numA, numB):
        return sorted(str(numA)) == sorted(str(numB))

    nmax = 10*1000*1000
    pmax = int(math.sqrt(nmax))*2
    primes = get_primes(pmax)

    min_ratio = 100
    for primeA in primes:
        for primeB in primes:
            n = primeA * primeB
            if n > nmax:
                break
            ps = [primeA, primeB]
            fi = phi(n, ps)
            if sorted(str(n)) == sorted(str(fi)):
                ratio = float(n) / fi
                if ratio < min_ratio:
                    min_ratio = ratio
                    print n, fi, ratio, ps

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): ~ 0.8 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
