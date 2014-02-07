#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def get_primes(nmax):
        # Sieve to find all primes up to nmax:
        composites = {}
        primes = [0,2]
        for mult in range(3,nmax,2):
            if not mult in composites:
                # Log mult as prime:
                primes.append(mult)

                # Sieve its multiples away:
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        return primes

    primes = get_primes(1000000)

    for n in range(1,len(primes),2):
        pn = primes[n]
        p2 = pn**2
        ra = pow(pn-1, n, p2)
        rb = pow(pn+1, n, p2)
        res = (ra+rb) % p2
        if res > 10**10:
            print(n)
            break

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 0.3 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
