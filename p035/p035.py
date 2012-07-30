def f1(max):
    ncirculars = 1 # 2 is a circular prime
    for i in range(3,max,2):
        if isprime(i):
            si = str(i)
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
