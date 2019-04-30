# Standard libs:
import sys
sys.path.append("..")

# Out libs:
from libeuler import core


# Globals:
MOD_NUMBER = 1_000_000_007


# Functions:
def p650(n):
    ret = 1

    for J in range(2, n+1):
        integer_factors = {2: 1}  # 2**1 = 2, only factor of B(2) = 2
        for i in range(3, J+1):
            integer_factors[i] = integer_factors.get(i, 0) + i - 1
            for j in range(2, i):
                integer_factors[j] = integer_factors.get(j, 0) - 1
        
        prime_factors = {}
        for k, v in integer_factors.items():
            for divisor, power in prime_divisors_of(k).items():
                prime_factors[divisor] = prime_factors.get(divisor, 0) + v*power
                
        ret += sum_of_divisors(prime_factors) % MOD_NUMBER
        
    return ret % MOD_NUMBER
    
    
def prime_divisors_of(n):
    divisors = {}
    for factor in core.factors_of(n):
        divisors[factor] = divisors.get(factor, 0) + 1

    return divisors


def sum_of_divisors(prime_factors):
    result = 1
    for k, v in prime_factors.items():
        result *= (k**(v+1) - 1) // (k - 1)
    
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
