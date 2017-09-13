# Standard libs:
import sys
import math
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p357(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n):

        # Produce all primes up to 10**8:
        nmax = 5*10**7
        composites = {}
        primes = [2]
        for mult in range(3, nmax, 2):
            if not mult in composites:
                primes.append(mult)
                for i in range(mult*mult, nmax, 2*mult):
                    composites[i] = True
        
        return len(primes), primes[-1]


# Main code:
if __name__ == "__main__":
    P = p357()
    P.run()

# Python 3.6.2 times (Burns)
#
#    n      res(n)  function  time (ms)
#   10           3        f0        0.3
