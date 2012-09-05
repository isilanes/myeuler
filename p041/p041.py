def f1():
    '''8-pandigital and 9-pandigital numbers can't be prime, as 1+2+3+4+5+6+7+8=36,
    and 1+2+3+4+5+6+7+8+9=45, and thus both are divisible by 3 (by 9, in fact).

    Largest pandigital prime will be 7-pandigital, or maybe less.'''

    import itertools

    for e in itertools.permutations('7654321'):
        num = int(''.join(e))
        if isprime(num):
            return num

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

res = f1()
print(res)
