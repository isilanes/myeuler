import timeit

#------------------------------------------------------------------------------#

def f0(maxn):
    print("--- f0 ---")

    def isprime(num):
        '''Returns True if num is prime, False otherwise.'''

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


    tot = 0
    for num in range(10,maxn,2):
        if isprime(num**2+1) and isprime(num**2+3) and isprime(num**2+7):
            if isprime(num**2+9) and isprime(num**2+13) and isprime(num**2+27):
                tot += num

    print(tot)

def f1(maxn):
    print("--- f1 ---")

    def isprime(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


    tot = 0
    for num in range(10,maxn,2):
        if isprime(num**2+1) and isprime(num**2+3) and isprime(num**2+7):
            if isprime(num**2+9) and isprime(num**2+13) and isprime(num**2+27):
                tot += num

    print(tot)

def f2(maxn):
    print("--- f2 ---")

    def isprime(n, primes=[]):
        for p in primes:
            if p == n:
                return True
            if not n % p:
                return False
        if not primes:
            pfirst = 5
        else:
            pfirst = 5 * (primes[-1] // 5) - 1
        for i in range(pfirst, int(n**0.5) + 1, 6):
            for k in [0, 2]:
                if not n % (i+k):
                    return False
        return True

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

    def kosher(num, primes):
        '''Return "num" if kosher, 0 if not.'''

        if not isprime(num**2+1, primes):
            return 0

        if not isprime(num**2+3, primes):
            return 0
        
        if not isprime(num**2+7, primes):
            return 0
        
        if not isprime(num**2+9, primes):
            return 0
        
        if not isprime(num**2+13, primes):
            return 0

        if not isprime(num**2+27, primes):
            return 0

        return num


    primes = get_primes(10**6)
    tot = 0
    for num in range(10,maxn,2):
        c1 = not (num % 6) # equiv num**2 % 6 == 0
        c2 = not (num**2 + 2) % 6
        c3 = not (num**2 + 4) % 6
        if c1 or c2: # 1, 7, 13
            if c2 or c3: # 3, 9, 27
                tot += kosher(num, primes)

    print(tot)

def f3(maxn):
    print("--- f3 ---")


    def isprime(n, primes=[]):
        for p in primes:
            if p == n:
                return True
            if not n % p:
                return False
        if not primes:
            pfirst = 5
        else:
            pfirst = 5 * (primes[-1] // 5) - 1
        for i in range(pfirst, int(n**0.5) + 1, 6):
            for k in [0, 2]:
                if not n % (i+k):
                    return False
        return True

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

    def kosher(num, primes):
        '''Return "num" if kosher, 0 if not.'''

        if not isprime(num**2+1, primes):
            return 0

        if not isprime(num**2+3, primes):
            return 0
        
        if not isprime(num**2+7, primes):
            return 0
        
        if not isprime(num**2+9, primes):
            return 0
        
        if not isprime(num**2+13, primes):
            return 0

        if not isprime(num**2+27, primes):
            return 0

        return num


    primes = get_primes(10**6)
    nomults = [ i for i in range(1,274) if i % 3 and i % 7 and i % 13 ]
    tot = 10 # first valid, no other below 273
    for c0 in range(273,maxn//2,273):
        for i in nomults:
            c = c0 + i
            tot += kosher(2*c, primes)

    print(tot)

def f4(maxn):
    print("--- f4 ---")


    def isprime(n, primes=[]):
        for p in primes:
            if p == n:
                return True
            if not n % p:
                return False
        if not primes:
            pfirst = 5
        else:
            pfirst = 5 * (primes[-1] // 5) - 1
        for i in range(pfirst, int(n**0.5) + 1, 6):
            for k in [0, 2]:
                if not n % (i+k):
                    return False
        return True

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

    def kosher(num, primes):
        '''Return "num" if kosher, 0 if not.'''

        if not isprime(num**2+1, primes):
            return 0

        if not isprime(num**2+3, primes):
            return 0
        
        if not isprime(num**2+7, primes):
            return 0
        
        if not isprime(num**2+9, primes):
            return 0
        
        if not isprime(num**2+13, primes):
            return 0

        if not isprime(num**2+27, primes):
            return 0

        return num


    primes = get_primes(10**6)


#------------------------------------------------------------------------------#

times = []
for i in [4]:
    t = timeit.Timer('f{0}(10**7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxn   t (ms) - v = 1.0
#      10**5    4100
#      10**6  357700

# f1:  maxn   t (ms) - v = 1.5
#      10**5    2741
#      10**6  237350

# f2:  maxn   t (ms) - v = 4.2
#      10**5    9540
#      10**6   83412

# f3:  maxn   t (ms) - v = 5.7
#      10**5    7136
#      10**6   62794

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
