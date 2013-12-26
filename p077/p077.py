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

    def mk_sum(p,c):
        '''
        Use primes p(n) and coefficients c(n) to obtain the sum:
        S = c(0)*p(0) + c(1)*p(1) + etc.
        '''

        S = 0
        for prime,coeff in zip(p,c):
            S += prime*coeff

        return S

    for Nmax in range(10,100):
        # Find all primes < Nmax:
        primes = get_primes(Nmax)

        # Potential coefficients:
        c = [ 0 for x in primes ]

        sums = []

        # Loop:
        digit = -1
        while True:
            s = mk_sum(primes,c)
            if s < Nmax:
                c[-1] += 1
                digit = -1
            else:
                if s == Nmax:
                    sums.append(c[:])
                if digit == -len(primes):
                    break
                c[digit] = 0
                c[digit-1] += 1
                digit -= 1

        print(Nmax, len(sums))
        if len(sums) > 5000:
            break

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: 
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
