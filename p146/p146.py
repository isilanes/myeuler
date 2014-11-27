import math
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

    def isprime(num):
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

    def find_mult_i():
        '''Find "mult" and "i" such that p = mult*m + i is the only viable
        structure for any first prime in requested sextet, for some integer m.'''

        primes = [ 3, 5, 7, 11 ]
        mult = 2
        for p in primes:
            mult *= p

        koshers = []
        for i in range(1,mult,2):
            kosher = True
            for p in primes:
                if not i % p:
                    kosher = False
                    break
            if kosher:
                koshers.append(i)

        for e in koshers[:-4]:
            if e + 2 in koshers:
                if e + 6 in koshers:
                    if e + 8 in koshers:
                        if e + 12 in koshers:
                            if e + 26 in koshers:
                                print(mult, e)


    #find_mult_i()
    tot = 10
    for n in range(2310,maxn,2):
        n2 = n**2
        r = (n2 + 1) % 2310
        if r in [101, 221, 431, 521, 851, 941, 1271, 1361, 1691, 2201]:
            # 19047, 43 ms
            if isprime(n2+1):
                # 3455, 15 s
                if isprime(n2+3):
                    # 628, 17.6 s
                    if isprime(n2+7):
                        # 112, 18 s
                        if isprime(n2+9):
                            # 23, 18.5 s
                            if isprime(n2+13):
                                # 4, 18.3 s
                                if isprime(n2+27):
                                    tot += n

    print(tot)

def f5(maxn):
    print("--- f5 ---")

    def isprime(num):
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

        mx = int(math.sqrt(num))+1
        for i in range(3, mx, 2):
            if not num % i:
                return False

        return True

    def find_mult_i():
        '''Find "mult" and "i" such that p = mult*m + i is the only viable
        structure for any first prime in requested sextet, for some integer m.'''

        primes = [ 2, 3, 5, 7, 11 ]
        mult = 1
        for p in primes:
            mult *= p

        koshers = []
        for i in range(1,mult,2):
            kosher = True
            for p in primes:
                if not i % p:
                    kosher = False
                    break
            if kosher:
                koshers.append(i)

        cutoffs = set([])
        for e in koshers[:-4]:
            if e + 2 in koshers:
                if e + 6 in koshers:
                    if e + 8 in koshers:
                        if e + 12 in koshers:
                            if e + 26 in koshers:
                                cutoffs.add(e)

        return mult, cutoffs


    mult, cutoffs = find_mult_i()
    tot = 0
    if mult > 10:
        tot += 10
    if mult > 315410:
        tot += 315410
    if mult > 927070:
        tot += 927070

    for n in range(mult, maxn, 2):
        n2 = n**2
        r = (n2 + 1) % mult
        if r in cutoffs:
            if isprime(n2+1):
                if isprime(n2+3):
                    if isprime(n2+7):
                        if isprime(n2+9):
                            if isprime(n2+13):
                                if isprime(n2+27):
                                    tot += n

    print(tot)

def f6(maxn):
    print("--- f6 ---")

    def isprimeMR(n):
        '''Use Miller-Rabin primality test. N must be odd and > 2.'''

        # n = 2**s * d + 1
        s = 0
        rem = n - 1
        while not rem % 2:
            s += 1
            rem = rem / 2

        d = (n - 1)/(2**s)

        for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
            test_passed = False # pass = be prime
            m = pow(a, d, n)
            if m == 1:
                test_passed = True
            else:
                for r in range(s):
                    m = pow(a, d*2**r, n)
                    if m == (n - 1):
                        test_passed = True
                        break
            if not test_passed:
                return False
        return True

    def find_mult_i():
        '''Find "mult" and "i" such that p = mult*m + i is the only viable
        structure for any first prime in requested sextet, for some integer m.'''

        primes = [ 2, 3, 5, 7, 11 ]
        mult = 1
        for p in primes:
            mult *= p

        koshers = []
        for i in range(1,mult,2):
            kosher = True
            for p in primes:
                if not i % p:
                    kosher = False
                    break
            if kosher:
                koshers.append(i)

        cutoffs = set([])
        for e in koshers[:-4]:
            if e + 2 in koshers:
                if e + 6 in koshers:
                    if e + 8 in koshers:
                        if e + 12 in koshers:
                            if e + 26 in koshers:
                                cutoffs.add(e)

        return mult, cutoffs


    mult, cutoffs = find_mult_i()
    tot = 0
    if mult > 10:
        tot += 10
    if mult > 315410:
        tot += 315410
    if mult > 927070:
        tot += 927070

    for n in range(mult, maxn, 10):
        n2 = n**2
        r = (n2 + 1) % mult
        if r in cutoffs:
            if isprimeMR(n2+1) and isprimeMR(n2+3):
                if not isprimeMR(n2+5) and isprimeMR(n2+7):
                    if isprimeMR(n2+9) and not isprimeMR(n2+11):
                        if isprimeMR(n2+13) and not isprimeMR(n2+15):
                            if not isprimeMR(n2+17) and not isprimeMR(n2+19):
                                if not isprimeMR(n2+21) and not isprimeMR(n2+23):
                                    if not isprimeMR(n2+25) and isprimeMR(n2+27):
                                        tot += n

    print(tot)


#------------------------------------------------------------------------------#

times = []
for i in [6]:
    t = timeit.Timer('f{0}(15*10**7)'.format(i), "from __main__ import f{0}".format(i))
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

# f4:  maxn   t (ms) - v = 30.7
#      10**5     264
#      10**6   11641
#      10**7  966220

# f5:  maxn   t (ms) - v =
#      10**6   119s!

# f6:  maxn   t (ms) - v =
#      10**5     176
#      10**6    1065
#      10**7   10105
#   15*10**7  144584

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
