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


    ps = get_primes(maxp1+10)
    if ps[-1] < maxp1:
        print("error")
        return
    for i in range(2,len(ps)-1): # from 5 on
        p1 = ps[i]
        p2 = ps[i+1]

    print(tot)


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(10)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxp1  t (ms)

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
