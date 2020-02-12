"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
import math

from libeuler import core


# Functions:
def p206_f0(n):
    """Straightforward (inefficient) method."""

    def is_valid(num):
        """Return True if num is of the form 1_2_3_4_5_6_7_8_9_0,
        False otherwise.
        """
        snum = str(num)
        if snum[18] != "0":
            return False

        if snum[16] != "9":
            return False

        if snum[14] != "8":
            return False

        if snum[12] != "7":
            return False

        if snum[10] != "6":
            return False

        if snum[8] != "5":
            return False

        if snum[6] != "4":
            return False

        if snum[4] != "3":
            return False

        if snum[2] != "2":
            return False

        if snum[0] != "1":
            return False

        return True

    # Minimum value would be all zeros:
    smin = 1020304050607080900

    # Maximum value, all nines:
    smax = 1929394959697989990

    # Limits of base:
    bmin = int(math.sqrt(smin))
    bmax = int(math.sqrt(smax))+1

    # Try all:
    for res in range(bmin, bmax+1):
        s = res*res
        if is_valid(s):
            return res

    return None


def p206_f1(n):
    """f0, with major speed tweaks."""
    
    def is_valid(num):
        """Return True if num is of the form 1_2_3_4_5_6_7_8_9_0,
        False otherwise.
        """
        snum = str(num)
        if snum[16] != "9":
            return False
        
        if snum[14] != "8":
            return False
        
        if snum[12] != "7":
            return False
        
        if snum[10] != "6":
            return False
        
        if snum[8] != "5":
            return False
        
        if snum[6] != "4":
            return False
        
        if snum[4] != "3":
            return False
        
        if snum[2] != "2":
            return False
        
        if snum[0] != "1":
            return False
        
        return True
    
    # Minimum value would be all zeros:
    smin = 1020304050607080900
    
    # Maximum value, all nines:
    smax = 1929394959697989990
    
    # Limits of base:
    bmin = int(math.sqrt(smin))
    bmax = int(math.sqrt(smax))+1
    
    # Now, for the square to end in zero, the base must end in zero, so check only multiples of 10:
    bmin = 10*int(bmin/10)
    
    # Try all (multiples of 10):
    for res in range(bmin, bmax+1, 10):
        s = res*res
        if is_valid(s):
            return res
    
    return None


def p206_f2(n):
    """f1, with more tweaks."""
    
    def is_valid(num):
        """Return True if num is of the form 1_2_3_4_5_6_7_8_9_0,
        False otherwise.
        No need to check for 9 and 0 at the end (ensured by construction),
        nor for 1 at the beginning (ensured by limits).
        """
        snum = str(num)
        if snum[14] != "8":
            return False
        
        if snum[12] != "7":
            return False
        
        if snum[10] != "6":
            return False
        
        if snum[8] != "5":
            return False
        
        if snum[6] != "4":
            return False
        
        if snum[4] != "3":
            return False
        
        if snum[2] != "2":
            return False
        
        return True
    
    # Minimum value would be all zeros:
    smin = 1020304050607080900
    
    # Maximum value, all nines:
    smax = 1929394959697989990
    
    # Limits of base:
    bmin = int(math.sqrt(smin))
    bmax = int(math.sqrt(smax))+1
    
    # Now, for the square to end in zero, the base must end in zero, so check only multiples of 10.
    # If our base is xxx0, the square is xxx00, and from the definition we know it is xxx900.
    # For that, our base must be either xxx30 or xxx70:
    bmin = 100*int(bmin/100)
    
    # Try all (multiples of 100 +30 or +70):
    for res in range(bmin, bmax+1, 100):
        for extra in [30, 70]:
            s = (res+extra)**2
            if is_valid(s):
                return res + extra
    
    return None


# Main code:
if __name__ == "__main__":
    core.run_functions([p206_f2])

# Python 3.6.2 times (Burns)
#
#    n      res(n)  function  time (ms)
#    -  1389019170        f0     180000
#
# pypy 5.1.2 @ Python 2.7.10 times (Burns)
#
#    n      res(n)  function  time (ms)
#    -  1389019170        f0      32700
#
# pypy 5.10.0 @ Python 2.7.13 times (Fry)
#
#    n      res(n)  function  time (ms)
#    -  1389019170        f0    19600
#    -  1389019170        f1     1621
#    -  1389019170        f2      426.2
