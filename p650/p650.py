# Standard libs:
import sys
import numpy as np
from functools import lru_cache

# Our libs:
sys.path.append("..")
from libeuler import core


# Globals:
MOD_NUMBER = 1_000_000_007


# Functions:
def p650(n):
    ret = 4  # B(0) + B(1) + B(2)

    for J in range(3, n+1):
        integer_factors = get_integer_factors(J)
        prime_factors = get_prime_factors(integer_factors)
        ret += moded_sum_of_divisors(prime_factors)
        
    return ret % MOD_NUMBER


def get_integer_factors(n):
    integer_factors = np.zeros(n+1, dtype=np.int16)
    
    for i in range(2, n+1):
        integer_factors[i] = 2*i - 1 - n
        
    return integer_factors


def get_prime_factors(i_factors):
    n = len(i_factors)
    prime_factors = np.zeros(n+1, dtype=np.int16)
    
    for k, v in enumerate(i_factors):
        if v:
            for divisor, power in prime_divisors_of(k).items():
                prime_factors[divisor] += v*power

    return prime_factors
    
    
@lru_cache(maxsize=20000)
def prime_divisors_of(n):
    divisors = {}
    for factor in core.factors_of(n):
        divisors[factor] = divisors.get(factor, 0) + 1

    return divisors


def moded_sum_of_divisors(prime_factors):
    result = 1
    for k, v in enumerate(prime_factors):
        if v:
            k = int(k)
            v = int(v)
            r = (k**(v+1) - 1) // (k - 1)
            result *= r
            result = result % MOD_NUMBER  # truncating early speeds up previously long multiplications
    
    return result


# Main code:
if __name__ == "__main__":
    core.run_functions([p650])

# Python 3.7.3 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    5         5736        f0        0.1
#   10   1721034274        f0        1.6 <-- wrong (bug)
#   15   5198581147        f0       37.6 <-- wrong (bug)
#   20   7131742875        f0     7100   <-- wrong (bug)
#   22  MemoryError
#
# Python 3.7.3 times (Fry)
#
#    n       res(n)  function  time (ms)
#    5         5736        f1        0.1
#   10    721034267        f1        0.2
#   15    198581112        f1        0.6
#   20    131742826        f1        1.2
#   50    217147306        f1       10.2
#  100    332792866        f1       73.1
#  200    271664942        f1      449.4
#  500    899393748        f1     7600
#  750     75285818        f1    31500
# 1000    361160563        f1    87900
#
#    n       res(n)  function  time (ms)
#    5         5736        f2        0.1
#   10    721034267        f2        0.2
#   20    131742826        f2        0.6
#   50    217147306        f2        2.4
#  100    332792866        f2       19.6
#  200    271664942        f2       48.2
#  500    899393748        f2     1429
# 1000    361160563        f2    33000
# 1500    762946177        f2   212000
#
#    n       res(n)  function  time (ms)
#    5         5736        f3        0.1
#  100    332792866        f3       18.8
#  200    271664942        f3       45.3
#  500    899393748        f3      256.5
# 1000    361160563        f3     1255
# 2000    939425731        f3     8300
# 3000    665284696        f3    27800
# 4000    809670819        f3    69600
