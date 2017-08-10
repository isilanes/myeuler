# Standard libs:
import sys
import random
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p152(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n):
        lcm = core.lcm_of_many(range(2, n))
        elements = [(lcm // e)**2 for e in range(2, n)]
        DEST = lcm // 2

        for e in elements:
            print(e)




# Main code:
if __name__ == "__main__":
    P = p152()
    P.run()

# Python 3.6.2 times (Skinner)
#
#    n      res(n)  function  time (ms)
#
#    -           -        f0         -

