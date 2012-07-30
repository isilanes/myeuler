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

res = f1(1000000)
print(res)
