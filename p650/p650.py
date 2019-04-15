# Standard libs:
import sys
sys.path.append("..")

# Out libs:
from libeuler import core


# Functions:
def prime_divisors_of(n):
    if n == 2:
        return {2: 1}
    
    if n == 3:
        return {3: 1}
    
    if n == 4:
        return {2: 2}
    
    if n == 5:
        return {5: 1}
    
    if n == 6:
        return {2: 1, 3: 1}

    if n == 7:
        return {7: 1}
    
    if n == 8:
        return {2: 3}
    
    if n == 9:
        return {3: 2}
    
    if n == 10:
        return {2: 1, 5: 1}


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


# Classes:
class p650(core.FunctionSet):
    """Group of solutions."""
    
    prime_factors = {}

    # Solutions:
    def f0(self, n):
        
        ret = 0
        
        for j in range(1, n+1):
            self.prime_factors = {}
        
            for i in additive_factorials(j):
                self.add_prime_factors_of_factorial(i)
            
            for i in subtractive_factorials(j):
                self.remove_prime_factors_of_factorial(i)
            
            #print(self.prime_factors)
            #print(self.sum_of_divisors())
            
            ret += self.sum_of_divisors()
        
        return ret
        
    def add_prime_factors_of_factorial(self, n):
        for i in range(2, n+1):
            for p, exp in prime_divisors_of(i).items():
                self.prime_factors[p] = self.prime_factors.get(p, 0) + exp
                
    def remove_prime_factors_of_factorial(self, n):
        for i in range(2, n+1):
            for p, exp in prime_divisors_of(i).items():
                self.prime_factors[p] -= exp  # it is an error if p was not a divisor, anyway
    
    def sum_of_divisors(self):
        return sum(divisor_list_of_factors(self.prime_factors))
    

# Main code:
if __name__ == "__main__":
    P = p650()
    P.run()

# Python 3.7.3 times (Fry)
#
#    n      res(n)  function  time (ms)
#    0           0        f0        0.0

