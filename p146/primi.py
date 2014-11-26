import timeit

#------------------------------------------------------------------------------#

def get_primes(nmax):
    # Sieve to find all primes up to nmax:
    composites = {}
    primes = [2]
    for mult in range(3,nmax,2):
        if not mult in composites:
            # Log mult as prime:
            primes.append(mult)

            # Sieve its multiples away:
            for i in range(mult*mult, nmax, 2*mult):
                composites[i] = True

    return primes


primes = get_primes(10**6)

def isprime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def isprime2(num):
    '''Returns True if num is prime, False otherwise.'''

    # Use Fermat primality (compositeness) test as a filter:
    if pow(2, num-1, num) != 1:
        return False

    if num == 1:
        return False

    if num in [2,3,5,7]:
        return True

    if num % 10 in [0,2,4,5,6,8]:
        return False

    i = 3
    while i*i < num+1:
        if not num % i:
            return False
        i += 2

    return True

def isprime3(n):
    # Use Fermat primality (compositeness) test as a filter:
    if pow(2, n-1, n) != 1:
        return False

    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def isprime4(n):
    # Use Fermat primality (compositeness) test as a filter:
    if pow(2, n-1, n) != 1:
        return False

    for k in primes:
        if k >= n:
            break
        if not n % k:
            return False

    i0 = 6 * (primes[-1] // 6)
    for i in range(i0, int(n**0.5) + 1, 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


def loop(nmax):
    for n in range(10, nmax, 2):
        isprime(n**2+1)

def loop2(nmax):
    for n in range(10, nmax, 2):
        isprime2(n**2+1)

def loop3(nmax):
    for n in range(10, nmax, 2):
        isprime3(n**2+1)

def loop4(nmax):
    for n in range(10, nmax, 2):
        isprime4(n**2+1)

if 0:
    # Test correctness:
    for n in range(10, 10**6, 2):
        if not isprime(n**2+1) == isprime4(n**2+1):
            print "Error with", n**2+1
            exit()

else:
    # Test speed:
    for fun in [ 'loop', 'loop2', 'loop3', 'loop4' ]:
        t = timeit.Timer('{0}({1})'.format(fun, 10**6), "from __main__ import {0}".format(fun))
        print "{0:6}:  {1:6.2f} s".format(fun, t.timeit(number=1)/1.)
