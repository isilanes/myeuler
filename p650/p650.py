# Standard libs:
import sys

# Our libs:
sys.path.append("..")
from libeuler import core


# Globals:
MOD_NUMBER = 10**9 + 7
PRIME_DIVISORS_OF = {}


# Functions:
def p650(n):
    global MOD_NUMBER
    global PRIME_DIVISORS_OF

    PRIME_DIVISORS_OF = get_all_prime_divisors(n)

    ret = 4  # B(0) + B(1) + B(2)
    for J in range(3, n+1):
        integer_factors = get_integer_factors(J)
        prime_factors = get_prime_factors(integer_factors)
        ret += moded_sum_of_divisors(prime_factors)
        
    return ret % MOD_NUMBER


def get_all_prime_divisors(n):
    all_pd = {}
    for i in range(2, n+1):
        all_pd[i] = prime_divisors_of(i)
    
    return all_pd


def get_integer_factors(n):
    return [0, 0] + [2*i - 1 - n for i in range(2, n+1)]


def get_prime_factors(i_factors):
    n = len(i_factors)
    prime_factors = [0 for _ in range(n+1)]
    
    for k, v in enumerate(i_factors):
        if v:
            for divisor, power in PRIME_DIVISORS_OF[k].items():
                prime_factors[divisor] += v*power

    return prime_factors


def prime_divisors_of(n):
    if n == 2:
        return {2: 1}
    
    if not n % 2:
        m = n//2
        divisors = prime_divisors_of(m)
        divisors[2] = divisors.get(2, 0) + 1
        
        return divisors
        
    divisors = {}
    for factor in core.factors_of(n):
        divisors[factor] = divisors.get(factor, 0) + 1

    return divisors


def moded_sum_of_divisors(prime_factors):
    result = 1
    for k, v in enumerate(prime_factors):
        if v:
            # Use inverse modulo:
            # b^-1 mod p = b^(p-2) mod p
            result *= (pow(k, v+1, MOD_NUMBER) - 1) * pow(k - 1, MOD_NUMBER-2, MOD_NUMBER) % MOD_NUMBER
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
#
# Python 3.7.3 times (Manjaro)
#
#     n      res(n)  function  time (ms)
#     5        5736        f4        0.1
#   100   332792866        f4       16.4
#   200   271664942        f4       52.8
#   500   899393748        f4      325.1
#  1000   361160563        f4     1298
#  2000   939425731        f4     5100
#  5000   141450898        f4    31800
# 10000   734570777        f4   125000
# 20000   538319652        f4   486000
#
# pypy 5.10 times (Manjaro)
#
#     n      res(n)  function  time (ms)
#     5        5736        f5        0.2
#   100   332792866        f5       23.7
#  1000   361160563        f5      124.9
# 10000   734570777        f5     7500
# 20000   538319652        f5    30500
