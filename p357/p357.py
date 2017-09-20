# Standard libs:
import sys
import itertools
from datetime import datetime
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
        """[WRONG] Optimize and fix f0."""

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

    def f2(self, n=10**8):
        """[WRONG] Ultra-naïve solution, trying to be robust and correct.
        We'll optimize later.
        """

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

            return True


        t0 = datetime.now()
        # Produce all primes up to nmax:
        nmax = n // 2
        composites = {}
        primes = [2]
        pdict = {2: True}
        for mult in range(3, nmax, 2):
            if not mult in composites:
                primes.append(mult)
                pdict[mult] = True
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True

        # Process:
        all = [1, 2]
        for mult in range(3, nmax, 2):
            if not mult % 10**6:
                t = datetime.now()
                dt = (t-t0).total_seconds()
                t0 = t
                print(mult, t, dt)
            target = 2*mult
            factors = core.factors_of(target)
            if is_valid(2*mult, factors, pdict):
                all.append(target)

        return sum(all)

    def f3(self, n=10**8):
        """First valid function (slow)."""

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

            return True


        # Produce all primes up to n:
        composites = {}
        pdict = {2: True}
        for mult in range(3, n, 2):
            if not mult in composites:
                pdict[mult] = True
                for i in range(mult*mult, n, 2*mult):
                    composites[i] = True

        # Process:
        all = [1, 2]
        for mult in range(3, n//2, 2):
            factors = [1, 2] + core.factors_of(mult)
            if is_valid(2*mult, factors, pdict):
                all.append(2*mult)

        return sum(all)

    def f4(self, n=10**8):
        """Optimize f3 by using better factorization function (in core)."""

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

            return True


        # Produce all primes up to n:
        composites = {}
        pdict = {2: True}
        for mult in range(3, n, 2):
            if not mult in composites:
                pdict[mult] = True
                for i in range(mult*mult, n, 2*mult):
                    composites[i] = True

        # Process:
        all = [1, 2]
        pkeys = sorted(pdict.keys())
        for mult in range(3, n//2, 2):
            factors = [1, 2] + core.factors_of_with_primes(mult, pkeys)
            if is_valid(2*mult, factors, pdict):
                all.append(2*mult)

        return sum(all)

    def f5(self, n=10**8):
        """Optimize f4 by using better generation, and avoid factorization altogether."""

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

            return True


        # Produce all primes up to n:
        composites = {}
        pdict = {2: True}
        for mult in range(3, n, 2):
            if not mult in composites:
                pdict[mult] = True
                for i in range(mult*mult, n, 2*mult):
                    composites[i] = True

        primes = sorted(pdict.keys())

        # Produce all composites up to nmax:
        bunch = {
            2: [1, 2],
        }
        for prime in primes[1:]: # avoid number "2", i.e. the first prime
            new = {}
            for pre in range(n+1):
                if pre in bunch:
                    prod = pre * prime
                    if prod > n:
                        break

                    new[prod] = bunch[pre] + [prime]

            bunch.update(new)
        
        tot = 1
        for k,v in bunch.items():
            if is_valid(k, v, pdict):
                tot += k

        return tot


# Main code:
if __name__ == "__main__":
    P = p357()
    P.run()

# Python 3.6.2 times (Burns)
benchmarks = {
    "Python 3.6.2 times (Burns)": {
        "f0": [ # n, result, time (ms)
            [ 10**1,         3,      0.1 ],
            [ 10**2,       113,      0.1 ],
            [ 10**3,      3353,      1.3 ],
            [ 10**4,     70327,     50.2 ],
            [ 10**5,   2309309,   2100   ],
            [ 10**6, 117350739, 142800   ],
        ],
        "f1": [ # n, result, time (ms)
            [ 10**1,            3,      0.1 ],
            [ 10**2,          113,      0.1 ],
            [ 10**3,         3353,      0.6 ],
            [ 10**4,        57759,      3.8 ],
            [ 10**5,      2086107,     23.5 ],
            [ 10**6,    112178977,    230   ],
            [ 10**7,   6621161053,   2700   ],
            [ 10**8, 412170985225,  30800   ],
        ],
        "f2": [ # n, result, time (ms)
            [ 10**1,            3,       0.1 ],
            [ 10**2,          113,       0.2 ],
            [ 10**3,         3791,       1.8 ],
            [ 10**4,        79601,      24.4 ],
            [ 10**5,      3205375,     429.4 ],
            [ 10**6,    152832417,   10700   ],
            [ 10**7,   8373051221,  285800   ],
            [ 10**8, 501311966519, 7690000   ],
        ],
        "f3": [ # n, result, time (ms)
            [ 10**2,          401,       0.3 ],
            [ 10**4,       262615,      53.0 ],
            [ 10**6,    524402305,   20800   ],
        ],
        "f4": [ # n, result, time (ms)
            [ 10**2,           401,       0.3 ],
            [ 10**4,        262615,      21.5 ],
            [ 10**6,     524402305,    3300   ],
            [ 10**8, 1739023853137, 1333700   ],
        ],
        "f5": [ # n, result, time (ms)
            [ 10**2,           401,       0.2 ],
            [ 10**4,        262615,       8.6 ],
            [ 10**6,     524402305,    1002   ],
            [ 10**8, 1739023853137,  134600   ],
        ],
    },
    "Python 3.5.2 times (Skinner)": {
        "f3": [ # n, result, time (ms)
            [ 10**2,           401,       0.1 ],
            [ 10**4,        262615,      13.9 ],
            [ 10**6,     524402305,    5600   ],
            [ 10**8, 1739023853137, 3944600   ],
        ],
    },
}
