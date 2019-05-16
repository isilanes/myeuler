# Standard libs:
import sys
import numpy as np

# Our libs:
sys.path.append("..")
from libeuler import core


# Globals:
NUMERATOR = 15499
DENOMINATOR = 94744
NUMERATOR, DENOMINATOR = 4, 10


# Functions:
def f0(n=None):
    d = 0
    while d < n:
        d += 2  # check only even denominators
        single_factors = list(set(core.factors_of(d)))
        n_resilients = 1
        for j in range(2, d):
            valid = True
            for factor in single_factors:
                if not j % factor:
                    valid = False
                    break
            if valid:
                n_resilients += 1

        if NUMERATOR * (d - 1) > DENOMINATOR * n_resilients:
            return d
    

def f1(n=None):
    matrix = np.zeros((n+1, n), dtype=np.int8)
    
    for i_col in range(1, n):
        matrix[i_col+1:, i_col] = 1
    
    for prime in core.primes_up_to(n):
        i_row = prime
        while i_row < n+1:
            for i_col in range(prime, i_col+1, prime):
                matrix[i_row, i_col] = 0
            
            i_row += prime
    
    minres = 1.0
    for d in range(2, n+1, 2):
        n_resilients = sum(matrix[d, :])
        res = n_resilients/d
        if res < minres:
            minres = res
        condition = NUMERATOR * (d - 1) > DENOMINATOR * n_resilients
        if condition:
            return d
    
    
# Main code:
if __name__ == "__main__":
    core.run_functions([f0, f1])

# PyPy 5.10.0 times (Manjaro)
#
#           n              res(n)  function  time (ms)
#        4/10                  12        f0        0.2
# 15499/94744                   -        f0    > 61 min
