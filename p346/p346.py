import math

from libeuler import core


def f0(n=None):
    
    def repunit(base, r):
        """Return decimal representation of r-digit repunit in base 'base'."""
        
        return sum([base**i for i in range(r)])
    
    repunit_count = {}
    for base in range(2, n+1):
        r = 2
        while True:
            ru = repunit(base, r)
            if ru > n:
                break

            repunit_count[ru] = repunit_count.get(ru, 0) + 1
            r += 1
    
    return sum([x for x, y in repunit_count.items() if y > 1]) + 1


def f1(n=None):
    """Take into account that every number 'N' in base 10 is a length-2 repunit in base N-1:
    N_10 = R_{N-1}(2) = 11_{N-1} = (N-1)**1 + (N-1)**0 = N - 1 + 1 = N
    So a strong repunit is a number with at least a length-3 repunit in some base (because all numbers
    have a lenght-2 repunit already). To find all length-3 repunits we need to check bases up to sqrt(n),
    because:
    R_b(3) = b**2 + b + 1 <= n
    b**2 < n
    b < sqrt(n)
    """
    def repunit(b, r):
        """Return decimal representation of r-digit repunit in base 'b'."""
        
        return sum([b**i for i in range(r)])
    
    max_base = int(math.sqrt(n))
    
    repunit_count = {}
    for base in range(2, max_base + 1):
        repeats = 3  # consider only repunits of length-3 or more
        while True:
            decimal_repunit = repunit(base, repeats)
            if decimal_repunit > n:
                break

            repunit_count[decimal_repunit] = repunit_count.get(decimal_repunit, 0) + 1
            
            repeats += 1
    
    return sum([x for x, y in repunit_count.items()]) + 1


if __name__ == "__main__":
    core.run_functions([f0, f1])

# Python 3.7.3 times (Manjaro)
#
#      n       res(n)  function  time (ms)
#     50          171        f0        0.5
#   1000        15864        f0        3.8
#  10**4       450740        f0       41.7
#  10**5     12755696        f0      407.8
#  10**6    372810163        f0     4200
#  10**7  11302817869        f0    42600
#
# PyPy 5.10.0 times (Manjaro)
#
#       n              res(n)  function  time (ms)
#      50                 171        f0        0.7
#    1000               15864        f0       17.9
#   10**4              450740        f0       27.7
#   10**5            12755696        f0       72.0
#   10**6           372810163        f0      565.6
#   10**7         11302817869        f0     5200
#   10**8         MemoryError        f0
#
#       n              res(n)  function  time (ms)
#      50                 171        f1        0.3
#    1000               15864        f1        0.6
#   10**4              450740        f1        2.0
#   10**5            12755696        f1        6.2
#   10**6           372810163        f1       15.6
#   10**7         11302817869        f1       17.0
#   10**8        348635395606        f1       21.2
#   10**9      10849978873789        f1       31.7
#  10**10     339706288602849        f1       68.5
#  10**11   10673552045628094        f1      178.7
#  10**12  336108797689259276        f1      630.0
