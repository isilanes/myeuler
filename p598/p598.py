# Standard libs:
import sys
import math
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
        # Factorize n!:
        powers = (8, 4, 2, 1)

        # proceed:
        res = 0
        divA_parts = []
        divB_parts = []


# Main code:
if __name__ == "__main__":
    P = p598()
    P.run()

# Python 3.6.2 times (Skinner)
#
#    n      res(n)  function  time (ms)
#   10           3        f0        0.2
