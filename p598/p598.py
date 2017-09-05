# Standard libs:
import sys
import math
import itertools
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p598(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n):
        """Basic, "by hand" result for C(10!).

        10! = 2**8 * 3**4 * 5**2 * 7
        if A * B = 10!, then:
        A = 2**a * 3**b * 5**c * 7**c
        B = 2**(8-a) * 3**(4-b) * 5**(2-c) * 7**(1-d)
         
        The amount of divisors would be:
        divA = (a+1) * (b+1) * (c+1) * (d+1)
        divB = (8-a+1) * (4-b+1) * (2-c+1) * (1-d+1)
         
        and we want to know when divA == divB
        """
        res = 0
        for a in range(9):
            for b in range(5):
                for c in range(3):
                    for d in range(2):
                        divA = (a+1)*(b+1)*(c+1)*(d+1)
                        divB = (9-a)*(5-b)*(3-c)*(2-d)
                        if divA == divB:
                            A = 2**a * 3**b * 5**c * 7**d
                            B = 2**(8-a) * 3**(4-b) * 5**(2-c) * 7**(1-d)
                            if A < B:
                                res += 1

        return res

    def f1(self, n):
        """Generalization of f0.
        Assumes argument "n" means C(n!).
        """
        def combo2ndivs(combo, pvals):
            """Given a combo, return (divA, divB),
            meaning amount of divisors for combo and
            for complementary of combo (according to pvals).
            """
            divA, divB = 1, 1
            for i, c in enumerate(combo):
                divA *= c + 1
                divB *= pvals[i] - c + 1

            return divA, divB
        
        def combo2nums(combo, pkeys, pvals):
            """Return number given by combo exponents, and complementary."""
            A, B = 1, 1
            for i, c in enumerate(combo):
                A *= pkeys[i]**c
                B *= pkeys[i]**(pvals[i] - c)

            return A, B


        # Factorize n!:
        powers = {
            2: 8,
            3: 4,
            5: 2,
            7: 1,
        }

        pkeys = sorted(powers.keys())
        pvals = [powers[k] for k in pkeys]

        lists = [tuple(range(p+1)) for p in pvals]
        
        # Proceed:
        res = 0
        for combo in itertools.product(*lists):
            divA, divB = combo2ndivs(combo, pvals)
            if divA == divB:
                A, B = combo2nums(combo, pkeys, pvals)
                if A < B:
                    #print(combo, A, B)
                    res += 1

        return res



# Main code:
if __name__ == "__main__":
    P = p598()
    P.run()

# Python 3.6.2 times (Skinner)
#
#    n      res(n)  function  time (ms)
#   10           3        f0        0.2
