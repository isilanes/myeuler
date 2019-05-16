# Standard libs:
import sys
import numpy as np

# Our libs:
sys.path.append("..")
from libeuler import core


# Globals:
NUMERATOR = 15499
DENOMINATOR = 94744


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


def f2(n=None):
    """If a denominator 'd' has 'nres(d)' resilient fractions, then its resiliency is:

    R(d)= nres(d)/(d-1)
    
    For all multiples of 'd', one can verify that:

    nres(n*d) = n*nres(d)
    
    so:
    
    R(n*d) = nres(n*d)/(n*d -1) = n*nres(d)/(n*d - 1)
    
    It is easy to see that R(n*d) decreases as n increases, but only up to a limit:
    
    lim(n -> inf) R(n*d) = nres(d)/d
    
    So, for a given 'd', its multiples will have progressively smaller R(n*d) values, but never
    smaller than nres(d)/d. The key, then, is to first find a 'd' such that its nres(d)/d is
    smaller than the threshold asked. Then, one must test successive values of 'n', to compute:
    
    R(n*d) = n*nres(d)/(n*d - 1)
    
    until R(n*d) is below the threshold asked.
    
    The values of 'd' with lowest relative values for nres(d) will be those in which each prime number
    appears only once (can I prove this, or is this only a conjecture?). For those, nres(d) can be
    calculated as follows:
    
    d = p1 * p2 * p3 ... -> nres(d) = (p1-1) * (p2-1) * (p3-1) ...
    
    So I will try:
    
    d = 2
    d = 2*3
    d = 2*3*5
    etc
    
    until nres(d)/d is below the threshold asked, then I will compute R(n*d) for increasing values of 'n',
    until R(n*d) is below the threshold asked. That is the answer.
    """
    # Produce successive primes, and use them to build 'd':
    primes = [2]
    d = 2
    nres = 1
    for i in range(3, 100, 2):
        is_prime = True
        for p in primes:
            if not i % p:
                is_prime = False
                break
        
        if is_prime:
            primes.append(i)
            d *= i
            nres *= (i-1)
            
            if nres*DENOMINATOR < NUMERATOR*d:
                break
    
    # Now, find 'n' such that R(n*d) < threshold:
    for factor in range(2, 100):  # we hope factor << 100
        if nres * factor * DENOMINATOR  < NUMERATOR * (d*factor - 1):
            break
    
    return d*factor
    
    
# Main code:
if __name__ == "__main__":
    core.run_functions([f0, f1, f2])

# PyPy 5.10.0 times (Manjaro)
#
#           n              res(n)  function  time (ms)
#        4/10                  12        f0        0.2
# 15499/94744                   -        f0      > 1 h
#
# Python 3.7.3 times (Manjaro)
#
#           n              res(n)  function  time (ms)
#        4/10                  12        f2        0.0
# 15499/94744           892371480        f2        0.0
