# Standard libs:
import sys
import math

# Our libs:
sys.path.append("..")
from libeuler import core


# Functions:
def f0(n=None):
    
    def repunit(base, r):
        """Return decimal representation of r-digit repunit in base 'base'."""
        
        return sum([base**i for i in range(r)])
    
    repunit_count = {}
    for base in range(2, n+1):
        r = 2
        while True:
            ru = repunit(base, r)
            if ru > n:
                break

            repunit_count[ru] = repunit_count.get(ru, 0) + 1
            r += 1
    
    return sum([x for x, y in repunit_count.items() if y > 1]) + 1


# Main code:
if __name__ == "__main__":
    core.run_functions([f0])

# Python 3.7.3 times (Manjaro)
#
#      n       res(n)  function  time (ms)
#     50          171        f0        0.5
#   1000        15864        f0        3.8
#  10**4       450740        f0       41.7
#  10**5     12755696        f0      407.8
#  10**6    372810163        f0     4200
#  10**7  11302817869        f0    42600
#
# PyPy 5.10.0 times (Manjaro)
#
#      n       res(n)  function  time (ms)
#     50          171        f0        0.7
#   1000        15864        f0       17.9
#  10**4       450740        f0       27.7
#  10**5     12755696        f0       72.0
#  10**6    372810163        f0      565.6
#  10**7  11302817869        f0     5200
#  10**8  MemoryError        f0
