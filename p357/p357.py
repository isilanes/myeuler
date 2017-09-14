# Standard libs:
import sys
import itertools
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p357(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n=10**8):
        """[WRONG] Naïve method."""

        def is_valid(N, divisors, primes):
            """Returns True if all divisors d in 'divisors' are such 
            that d+N/d is prime (i.e., is in 'primes'. False otherwise.
            """
            for d in divisors:
                if d + N/d not in primes:
                    return False

            return True


        # Produce all primes up to nmax:
        nmax = n // 2
        composites = {}
        primes = [2]
        for mult in range(3, nmax, 2):
            if not mult in composites:
                primes.append(mult)
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True
        
        # Produce all composites up to nmax:
        bunch = {2: [1, 2]}
        for i, prime in enumerate(primes[1:]): # avoid number "2", i.e. the first prime
            new = {}
            for pre, factors in bunch.items():
                prod = pre * prime
                if prod > n:
                    break
                new[prod] = factors + [prime]

            bunch.update(new)
        
        # Check:
        tot = 1 # 1 is the first valid one
        for N, divisors in bunch.items():
            if is_valid(N, divisors, primes):
                #print(N, divisors)
                tot += N

        return tot

    def f1(self, n=10**8):
        """Optimize and fix f0."""

        def divisors(pdivisors):
            """Given single prime divisors, return list of all divisors."""

            divisors = [1]
            bdivisors = pdivisors[1:]
            for r in range(1, len(bdivisors)+1):
                for subset in itertools.combinations(bdivisors, r):
                    divisor = 1
                    for e in subset:
                        divisor *= e
                    divisors.append(divisor)

            return divisors

        def is_valid(N, pdivisors, primes):
            """Returns True if all divisors d in 'divisors' are such 
            that d+N/d is prime (i.e., is in 'primes'. False otherwise.
            """
            # Check "1":
            if 1 + N not in primes:
                return False

            # Check upwards of "1":
            for d in divisors(pdivisors):
                if d + N/d not in primes:
                    return False

            """
            big_divisors = pdivisors[1:] # take "1" away
            for r in range(1, len(big_divisors)+1):
                for subset in itertools.combinations(big_divisors, r):
                    divisor = 1
                    for s in subset:
                        divisor *= s
                    if divisor + N/divisor not in primes:
                        return False
            """

            return True


        # Produce all primes up to nmax:
        nmax = n // 2
        composites = {}
        primes = [2]
        for mult in range(3, nmax, 2):
            if not mult in composites:
                primes.append(mult)
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        # Prime dictionary, to speed up search:
        pdict = {}
        for prime in primes:
            pdict[prime] = True
        
        # Produce all composites up to nmax:
        tot = 3 # 1 + 2
        bunch = {2: [1, 2]}
        for i, prime in enumerate(primes[1:]): # avoid number "2", i.e. the first prime
            new = {}
            for pre, factors in bunch.items():
                prod = pre * prime
                if prod > n:
                    break
                new_factors = factors + [prime]
                new[prod] = new_factors
                if is_valid(prod, new_factors, pdict):
                    #print(prod, new_factors, divisors(new_factors))
                    tot += prod

            bunch.update(new)

        return tot


# Main code:
if __name__ == "__main__":
    P = p357()
    P.run()

# Python 3.6.2 times (Burns)
#
#       n        res(n)  function  time (ms)
#   10**1             3        f0        0.1
#   10**2           113        f0        0.1
#   10**3          3353        f0        1.3
#   10**4         70327        f0       50.2
#   10**5       2309309        f0     2100
