import timeit

#------------------------------------------------------------------------------#

def f0(maxp):
    print("--- f0 ---")

    def A(n):
        '''Returns A(n) for n.'''

        k = 1
        rem = 1
        while True:
            rem = (rem + pow(10, k, n)) % n
            if not rem:
                return k + 1
            k += 1

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

    def ismultiple25(num):
        '''Returns True if num is multiple of 2 and 5 ONLY. False otherwise.'''

        while not num % 2:
            num = num / 2

        while not num % 5:
            num = num / 5

        return num == 1


    tot = 2 + 3 + 5
    for p in get_primes(maxp)[3:]:
        a = A(p)
        if not ismultiple25(a):
            tot += p

    print(tot)


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(1000*100)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxp  t (ms)
#       100       0.7
#      1000      24
#     10000    1356
#    100000  129600

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
