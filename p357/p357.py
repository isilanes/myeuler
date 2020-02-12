import math
import bisect
import itertools
from datetime import datetime

from libeuler import core


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
                    tot += prod

            bunch.update(new)

        return tot

    def f2(self, n=10**8):
        """
        [WRONG] Ultra-naïve solution, trying to be robust and correct.
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
            """
            Returns True if all divisors d in 'divisors' are such
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
            """
            Returns True if all divisors d in 'divisors' are such
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
            """
            Returns True if all divisors d in 'divisors' are such
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

    def f6(self, n=10**8):
        """De-optimize f5 by not sorting sorting."""

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
            """
            Returns True if all divisors d in 'divisors' are such
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
            for pre in bunch.keys():
                prod = pre * prime
                if prod > n:
                    continue

                new[prod] = bunch[pre] + [prime]

            bunch.update(new)
        
        tot = 1
        for k,v in bunch.items():
            if is_valid(k, v, pdict):
                tot += k

        return tot

    def f7(self, n=10**8):
        """Optimize f5 by using bisect module."""

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
            """
            Returns True if all divisors d in 'divisors' are such
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
        blist = [2]
        for prime in primes[1:]: # avoid number "2", i.e. the first prime
            new = {}
            for pre in blist:
                prod = pre * prime
                if prod > n:
                    break

                new[prod] = bunch[pre] + [prime]

            bunch.update(new)
            for k in new:
                bisect.insort(blist, k)
        
        tot = 1
        for k,v in bunch.items():
            if is_valid(k, v, pdict):
                tot += k

        return tot

    def f8(self, n=10**8):
        """Go back to semi brute force, with some optimizations."""

        def is_valid(N, pdict):
            for d in range(1, int(math.sqrt(N))+1):
                if not N % d and (d + N/d) not in pdict:
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

        # Check all numbers:
        tot = 3 # n = 1 and 2
        for num in range(4, n+1, 2):
            if is_valid(num, pdict):
                tot += num

        return tot

    def f9(self, n=10**8):
        """Jorge's algorithm."""

        # Produce all primes up to n:
        composites = {}
        pdict = {2: True}
        for mult in range(3, n, 2):
            if not mult in composites:
                pdict[mult] = True
                for i in range(mult*mult, n, 2*mult):
                    composites[i] = True

        list_test = {}
        for i in range(4, n+1, 2):
            list_test[i] = True

        # Check all divisors:
        tot = 3  # 1 and 2
        div = 1
        while list_test:
            for divisible in [x for x in list_test if not x % div]:
                if not div + divisible/div in pdict:
                    del list_test[divisible]
                else:
                    if div**2 > divisible:
                        tot += divisible
                        del list_test[divisible]
            div += 1

        return tot


if __name__ == "__main__":
    P = p357()
    P.run()

# Python 3.6.2 times (Burns)
benchmarks = {
    "Python 3.6.2 (Burns)": {
        "f0": {
            "skip": True,
            "data": [  # n, result, time (ms)
                [10**1,         3,      0.1],
                [10**2,       113,      0.1],
                [10**3,      3353,      1.3],
                [10**4,     70327,     50.2],
                [10**5,   2309309,   2100  ],
                [10**6, 117350739, 142800  ],
            ],
        },
        "f1": {
            "skip": True,
            "data": [  # n, result, time (ms)
                [10**1,            3,      0.1],
                [10**2,          113,      0.1],
                [10**3,         3353,      0.6],
                [10**4,        57759,      3.8],
                [10**5,      2086107,     23.5],
                [10**6,    112178977,    230  ],
                [10**7,   6621161053,   2700  ],
                [10**8, 412170985225,  30800  ],
            ],
        },
        "f2": {
            "skip": True,
            "data": [  # n, result, time (ms)
                [10**1,            3,       0.1],
                [10**2,          113,       0.2],
                [10**3,         3791,       1.8],
                [10**4,        79601,      24.4],
                [10**5,      3205375,     429.4],
                [10**6,    152832417,   10700  ],
                [10**7,   8373051221,  285800  ],
                [10**8, 501311966519, 7690000  ],
            ],
        },
        "f3": {
            "data": [  # n, result, time (ms)
                [10**2,          401,       0.3],
                [10**4,       262615,      53.0],
                [10**6,    524402305,   20800  ],
            ],
        },
        "f4": {
            "data": [  # n, result, time (ms)
                [ 10**2,           401,       0.3 ],
                [ 10**4,        262615,      21.5 ],
                [ 10**6,     524402305,    3400   ],
                [ 10**8, 1739023853137, 1333700   ],
            ],
        },
        "f5": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.2],
                [10**4,        262615,      11.8],
                [10**6,     524402305,    1004  ],
                [10**8, 1739023853137,  134600  ],
            ],
        },
        "f6": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.2],
                [10**4,        262615,     161.7],
                [10**6,     524402305, 1023000  ],
            ],
        },
        "f7": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.2],
                [10**4,        262615,       6.7],
                [10**6,     524402305,    6400  ],
            ],
        },
        "f8": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.1],
                [10**4,        262615,       9.3],
                [10**6,     524402305,     796  ],
                [10**8, 1739023853137,  102500  ],
            ],
        },
        "f9": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.1],
                [10**4,        262615,      34.0],
                [10**5,       9157937,    2500  ],
                [10**6,     524402305,  415200  ],
            ],
        },
    },
    "PyPy 5.1.2 (Burns)": {
        "f8": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.4],
                [10**4,        262615,      35.7],
                [10**5,       9157937,      55.1],
                [10**6,     524402305,     189.8],
                [10**7,   27814470277,    2300  ],
                [10**8, 1739023853137,   30700  ],
            ],
        },
    },
    "Python 3.5.2 (Skinner)": {
        "f3": {
            "data": [  # n, result, time (ms)
                [10**2,           401,       0.1],
                [10**4,        262615,      13.9],
                [10**6,     524402305,    5600  ],
                [10**8, 1739023853137, 3944600  ],
            ],
        },
    },
    "Matlab R2012b (Burns)": {
        "m0": {
            "data": [  # n, result, time (ms)
                [10**2,           401,     160  ],
                [10**4,        262615,     179.6],
                [10**6,     524402305,     684.7],
                [10**8, 1739023853137,   86700  ],
            ],
        },
    },
}
