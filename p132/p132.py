import timeit

#------------------------------------------------------------------------------#

def f0(k):
    '''Find first prime factors of R(k) repunit.'''

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


    nfac = 0
    tot = 0
    for p in get_primes(200000)[2:]: # leave 2 and 3 out
        rem = pow(10, k, p)
        if rem == 1:
            tot += p
            nfac += 1
            if nfac >= 40:
                break

    if nfac != 40:
        print("lacking")

    print(tot)

#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(10**9)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:      k  t (ms)
#      10**9      71

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
