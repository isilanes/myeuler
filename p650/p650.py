# Standard libs:
import sys
sys.path.append("..")

# Out libs:
from libeuler import core


# Functions:
def p650(n):
    ret = 0

    for j in range(1, n+1):
        prime_factors = {}

        for i in additive_factorials(j):
            add_prime_factors_of_factorial(prime_factors, i)

        for i in subtractive_factorials(j):
            remove_prime_factors_of_factorial(prime_factors, i)

        ret += sum_of_divisors(prime_factors) % 1000000007

    return ret


def prime_divisors_of(n):
    divisors = {}
    for factor in core.factors_of(n):
        divisors[factor] = divisors.get(factor, 0) + 1

    return divisors


def divisor_list_of_factors(factors):
    divisors = [1]
    for factor, exponent in factors.items():
        tmp = []
        tmp2 = [factor**i for i in range(exponent+1)]
        for d in divisors:
            tmp.extend([d*t for t in tmp2])
        divisors = tmp[:]
    
    return divisors


def additive_factorials(n):
    for i in range(n-1):
        yield n
    
    
def subtractive_factorials(n):
    yield n-1
        
    for i in range(1, n-2):
        yield n-i-1
        yield i+1
        
    yield n-1


def add_prime_factors_of_factorial(prime_factors, n):
    for i in range(2, n+1):
        for p, exp in prime_divisors_of(i).items():
            prime_factors[p] = prime_factors.get(p, 0) + exp


def remove_prime_factors_of_factorial(prime_factors, n):
    for i in range(2, n+1):
        for p, exp in prime_divisors_of(i).items():
            prime_factors[p] -= exp  # it is an error if p was not a divisor, anyway


def sum_of_divisors(prime_factors):
    return sum(divisor_list_of_factors(prime_factors))


# Main code:
if __name__ == "__main__":
    core.run_functions([p650])

# Python 3.7.3 times (Manjaro)
#
#    n       res(n)  function  time (ms)
#    5         5736        f0        0.1
#   10   1721034274        f0        1.6
#   15   5198581147        f0       37.6
#   20   7131742875        f0     7100
#   22  MemoryError

