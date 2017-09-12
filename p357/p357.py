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
        
        for d in [1, 2, 3, 5, 6, 10, 15, 30]:
            print(d, d+30//d)

        return


# Main code:
if __name__ == "__main__":
    P = p357()
    P.run()

# Python 3.6.2 times (Burns)
#
#    n      res(n)  function  time (ms)
#   10           3        f0        0.3
