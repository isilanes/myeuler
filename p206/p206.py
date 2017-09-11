"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

# Standard libs:
import sys
import math
import itertools
sys.path.append("..")

# Out libs:
from libeuler import core

# Classes:
class p206(core.FunctionSet):
    """Group of solutions."""

    # Solutions:
    def f0(self, n):
        """Straightforward (inefficient) method."""

        def is_valid(num):
            """Return True if num is of the form 1_2_3_4_5_6_7_8_9_0,
            False otherwise.
            """
            snum = str(num)
            if snum[18] != "0":
                return False

            if snum[16] != "9":
                return False

            if snum[14] != "8":
                return False

            if snum[12] != "7":
                return False

            if snum[10] != "6":
                return False

            if snum[8] != "5":
                return False

            if snum[6] != "4":
                return False

            if snum[4] != "3":
                return False

            if snum[2] != "2":
                return False

            if snum[0] != "1":
                return False

            return True


        # Minimum value would be all zeros:
        smin = 1020304050607080900

        # Maximum value, all nines:
        smax = 1929394959697989990

        # Limits of base:
        bmin = int(math.sqrt(smin))
        bmax = int(math.sqrt(smax))+1

        # Try all:
        for res in range(bmin, bmax+1):
            s = res*res
            if is_valid(s):
                return res

        return None


# Main code:
if __name__ == "__main__":
    P = p206()
    P.run()

# Python 3.6.2 times (Burns)
#
#    n      res(n)  function  time (ms)
#   10  1389019170        f0     180000
#
# pypy 5.1.2 @ Python 2.7.10 times (Burns)
#
#    n      res(n)  function  time (ms)
#   10  1389019170        f0      32700
