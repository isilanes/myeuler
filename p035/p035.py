def f1(max):
    ncirculars = 4 # 2, 3, 5, 7 are circular primes
    for i in range(11,max,2):
        if isprime(i):
            si = str(i)
            if not '2' in si and not '4' in si and not '5' in si and not '6' in si and not '8' in 'si' and not '0' in si:
                iscircular = True
                for j in range(len(si)-1):
                    si = si[1:] + si[0]
                    ii = int(si)
                    if not isprime(ii):
                        iscircular = False
                        break
                if iscircular:
                    ncirculars += 1

    return ncirculars

#-------------------------------------------------------------------------#

def isprime(m):
    '''Returns True if m is prime. Code taken from p027.'''

    import math

    if not m % 2:
        return False

    for i in range(3, int(math.sqrt(m)+1), 2):
        if not m % i:
            return False

    # If we reach so far, it is prime:
    return True

#-------------------------------------------------------------------------#

def f2(max):
    # First use sieve to get all composites below "max":
    composites = {}
    primes = [2]
    for mult in range(3,max,2):
        if not mult in composites:
            primes.append(mult)
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    ncirculars = 2 # the 2 1-digit primes that will be rejected below (2 and 5)
    # Check all primes to see if they are circular:
    for prime in primes:
        si = str(prime)
        if not '2' in si and not '4' in si and not '5' in si and not '6' in si and not '8' in 'si' and not '0' in si:
            iscircular = True
            for j in range(len(si)-1):
                si = si[1:] + si[0]
                ii = int(si)
                if ii in composites or not ii % 2: # remeber we didn't bother about even composites above (all of 'em)
                    iscircular = False
                    break
            if iscircular:
                ncirculars += 1

    return ncirculars

#-------------------------------------------------------------------------#

res = f2(1000000)
print(res)
