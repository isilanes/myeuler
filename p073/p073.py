#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def get_primes(nmax):
        primes = [2]
        composites = {}
        for mult in range(3,nmax+1,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        return primes

    def primes_of(N, primes):
        '''
        Return distinct prime factors of N.
        '''

        p = {}
        for prime in primes:
            if not N % prime:
                p[prime] = True
                N = N / prime
                if N == 1:
                    return p
            while not N % prime:
                N = N / prime
                if N == 1:
                    return p

    res = 0
    nmax = 12000
    pof = { 2: [2], 3: [3]}
    primes = get_primes(nmax)
    for N in range(4,nmax+1):
        A = int(N/3) + 1
        B = int(N/2) + 1
        pof[N] = primes_of(N, primes)
        for i in range(A,B):
            copri = True
            for p in pof[N]:
                if p in pof[i]:
                    copri = False
                    break
            if copri:
                res += 1

    print(res)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): ~ 2.5 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
