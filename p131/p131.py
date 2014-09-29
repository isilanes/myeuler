import math
import timeit

#------------------------------------------------------------------------------#

def f0(nmax):
    print("--- f0 ---")

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


        p += 2
        if p % 5 and not isprime(p):
            a = A(p)
            if not (p - 1) % a:
                comps.append(p)
    
    def is_cube(num):
        tmp = pow(num, 1./3)
        if int(math.ceil(tmp))**3 == num:
            return True
        if int(math.floor(tmp))**3 == num:
            return True
        return False


    nprim = 0
    for p in get_primes(nmax):
        for n in range(1,2*p):
            c3 = n**3 + p*n**2
            if is_cube(c3):
                nprim += 1
                print(p, '->', n)

    print(nprim)

def f1(nmax):
    '''For each p, find d, where c = n + d, where c**3 = n**3 + p*n**2. Then substitute
    into equality, and find n. d must be below 4*p/3 (and be integer), otherwise
    the equation yields complex n.'''

    print("--- f1 ---")

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


        p += 2
        if p % 5 and not isprime(p):
            a = A(p)
            if not (p - 1) % a:
                comps.append(p)
    
    def is_cube(num):
        tmp = pow(num, 1./3)
        if int(math.ceil(tmp))**3 == num:
            return True
        if int(math.floor(tmp))**3 == num:
            return True
        return False


    nprim = 0
    for p in get_primes(nmax):
        for d in range(1,int(p/3)):
            s = d*(4*p - 3*d)
            n = (-3*d**2 - d*math.sqrt(s))/(2*(3*d-p))
            n = int(n+0.5)
            if n > 0:
                c3 = n**3 + p*n**2
                if is_cube(c3):
                    nprim += 1
                    break

    print(nprim)

def f2(nmax):
    '''Like f1, but check only d = i**2. Not rigorous, but realized that
    d = c - n, where c**3 = n**3 + p*n**2, was always square.'''

    print("--- f2 ---")

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


        p += 2
        if p % 5 and not isprime(p):
            a = A(p)
            if not (p - 1) % a:
                comps.append(p)
    
    def is_cube(num):
        tmp = pow(num, 1./3)
        if int(math.ceil(tmp))**3 == num:
            return True
        if int(math.floor(tmp))**3 == num:
            return True
        return False


    nprim = 0
    for p in get_primes(nmax)[2:]:
        i = 0
        d = i**2
        while d < int(p/3):
            i += 1
            d = i**2
            s = d*(4*p - 3*d)
            n = (-3*d**2 - d*math.sqrt(s))/(2*(3*d-p))
            n = int(n+0.5)
            if n > 0:
                c3 = n**3 + p*n**2
                if is_cube(c3):
                    nprim += 1
                    break

    print(nprim)


#------------------------------------------------------------------------------#

times = []
for i in [2]:
    t = timeit.Timer('f{0}(1000*1000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:    nmax  t (ms)
#         100      19
#        >200  wrong?

# f1:    nmax    t (ms)
#         100         4
#        1000        26
#       10000       453
#      100000     32000
#     1000000  too slow

# f1:    nmax  t (ms)
#         100       1
#        1000      27
#       10000      41
#      100000     283
#     1000000   10700

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
