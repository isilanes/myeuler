# Standard libs:
import sys
import functools

# Our libs:
sys.path.append("..")
from libeuler import core


# Functions:
def p301(n=None):
    res = 0
    for i in range(1, 2**n+1):
        if nim_sum_of(i) == 0:
            res += 1

    return res


def nim_sum_of(n):
    # Copied from:
    # https://en.wikipedia.org/wiki/Nim#Example_implementation
    return functools.reduce(lambda x, y: x ^ y, (n, 2*n, 3*n))


# Main code:
if __name__ == "__main__":
    core.run_functions([p301])

# Python 3.7.3 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#
# pypy 5.10.0 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    1            2        f0        0.1
#   10          144        f0        1.5
#   20        17711        f0     1258
#   30      2178310        f0    65300
