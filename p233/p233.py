# Standard libs:
import sys
import math

# Our libs:
sys.path.append("..")
from libeuler import core


# Functions:
def f0(n=None):
    max_np = 0
    for N in range(2, n):
        np = 0
        for dx in range(N//2):
            x = int(N/2 + dx)
            y = (math.sqrt(N**2 - 4*x**2 + 4*x*N) + N)*0.5
            y = int(y)
            if 2*N**2 == (2*x - N)**2 + (2*y - N)**2:
                np += 1
        
        if np > 0:
            np = np*8 + 4
            if np > max_np:
                print(N, np)
                max_np = np
        
    return 666
 
    
# Main code:
if __name__ == "__main__":
    core.run_functions([f0])

# PyPy 5.10.0 times (Manjaro)
#
#           n              res(n)  function  time (ms)
