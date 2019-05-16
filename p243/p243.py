# Standard libs:
import sys

# Our libs:
sys.path.append("..")
from libeuler import core


# Globals:
NUMERATOR = 15499
DENOMINATOR = 94744


# Functions:
def f0(n=None):
    d = 2
    while True:
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
        
        d += 2  # check only even denominators
    
    
# Main code:
if __name__ == "__main__":
    core.run_functions([f0])

# PyPy 5.10.0 times (Manjaro)
#
#           n              res(n)  function  time (ms)
#        4/10                  12        f0        0.2
# 15499/94744                   -        f0    > 60 min
