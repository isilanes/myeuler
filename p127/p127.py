#--------------------------------------------------------------------#

def f0(Nmax):
    print("--- f0 ---")

    def rad(N):
        '''
        Return rad(N), and the list of distinct primes that make up
        rad(N). E.g.:
        504 = 2**3 * 3**2 * 7 -> rad(504) = 2*3*7 = 42
        return 42, [2,3,7]
        '''

        r = 1
        facs = []
        for i in range(2,N+1):
            if not N % i:
                r = r * i
                facs.append(i)
                N = N / i
            while not N % i:
                N = N / i
            if N == 1:
                break
            i += 1
        
        return r, facs

    def invalid(i,facs):
        for fac in facs:
            if not i % fac:
                return True
        return False

    sumc = 0
    for c in range(1,Nmax):
        rad_c, facs_c = rad(c)
        rem_list = []
        for i in range(1,c):
            if not invalid(i, facs_c):
                rem_list.append(i)
            
        for j in range(len(rem_list)):
            a = rem_list[j]
            if 2*a > c:
                break
            rad_a, facs_a = rad(a)
            b = c - a
            if b in rem_list:
                if not invalid(b,facs_a):
                    rad_b, facs_b = rad(b)
                    rad_abc = rad_a * rad_b * rad_c
                    if rad_abc < c:
                        sumc += c

    print(sumc)

#--------------------------------------------------------------------#

def f1(Nmax):
    print("--- f1 ---")

    def rad(N):
        '''
        Return rad(N), and the list of distinct primes that make up
        rad(N). E.g.:
        504 = 2**3 * 3**2 * 7 -> rad(504) = 2*3*7 = 42
        return 42, [2,3,7]
        '''

        r = 1
        facs = []
        for i in range(2,N+1):
            if not N % i:
                r = r * i
                facs.append(i)
                N = N / i
            while not N % i:
                N = N / i
            if N == 1:
                break
            i += 1
        
        return r, facs

    def invalid(i,facs):
        for fac in facs:
            if not i % fac:
                return True
        return False

    class Memoize(object):

        def __init__(self, fun):
            self.fun = fun
            self.cache = {}

        def __call__(self, *args):
            if not args in self.cache:
                self.cache[args] = self.fun(*args)
            return self.cache[args]

    rad = Memoize(rad)

    sumc = 0
    for c in range(1,Nmax):
        rad_c, facs_c = rad(c)
        rem_list = []
        for i in range(1,c):
            if not invalid(i, facs_c):
                rem_list.append(i)
            
        for j in range(len(rem_list)):
            a = rem_list[j]
            if 2*a > c:
                break
            rad_a, facs_a = rad(a)
            b = c - a
            if b in rem_list:
                if not invalid(b,facs_a):
                    rad_b, facs_b = rad(b)
                    rad_abc = rad_a * rad_b * rad_c
                    if rad_abc < c:
                        sumc += c

    print(sumc)

#--------------------------------------------------------------------#

def f2(Nmax):
    print("--- f2 ---")

    def rad(N):
        '''
        Return rad(N), and the list of distinct primes that make up
        rad(N). E.g.:
        504 = 2**3 * 3**2 * 7 -> rad(504) = 2*3*7 = 42
        return 42, [2,3,7]
        '''

        r = 1
        facs = []
        for i in range(2,N+1):
            if not N % i:
                r = r * i
                facs.append(i)
                N = N / i
            while not N % i:
                N = N / i
            if N == 1:
                break
            i += 1
        
        return r, facs

    def invalid(i,facs):
        for fac in facs:
            if not i % fac:
                return True
        return False

    class Memoize(object):

        def __init__(self, fun):
            self.fun = fun
            self.cache = {}

        def __call__(self, *args):
            if not args in self.cache:
                self.cache[args] = self.fun(*args)
            return self.cache[args]

    rad = Memoize(rad)

    sumc = 0
    for a in range(1,Nmax):
        rad_a, facs_a = rad(a)
        for b in range(a+1,Nmax):
            if not invalid(b, facs_a):
                rad_b, facs_b = rad(b)
                c = b + a
                if c >= Nmax:
                    break
                if not invalid(c, facs_a):
                    rad_c, facs_c = rad(c)
                    rad_abc = rad_a * rad_b * rad_c
                    if rad_abc < c:
                        sumc += c

    print(sumc)

#--------------------------------------------------------------------#

def f3(Nmax):
    print("--- f3 ---")

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

    class MemoRad(object):

        def calc(self, N):
            '''
            Return rad(N), and the list of distinct primes that make up
            rad(N). E.g.:
            504 = 2**3 * 3**2 * 7 -> rad(504) = 2*3*7 = 42
            return 42, [2,3,7]
            '''

            N_initial = N

            r = 1
            facs = []
            for prime in self.primes:
                if not N % prime:
                    r = r * prime
                    facs.append(prime)
                    N = N / prime
                while not N % prime:
                    N = N / prime
                if N == 1:
                    break
            
            self.cache[N_initial] = (r, facs)

        def __init__(self, primes):
            self.primes = primes
            self.cache = {}

        def rad(self, N):
            if not N in self.cache:
                self.calc(N)
            return self.cache[N]

    def invalid(i,facs):
        for fac in facs:
            if not i % fac:
                return True
        return False

    primes = get_primes(Nmax)
    MR = MemoRad(primes)

    sumc = 0
    for a in range(1,Nmax):
        rad_a, facs_a = MR.rad(a)
        for b in range(a+1,Nmax-a):
            if not invalid(b, facs_a):
                c = a + b
                rad_b, facs_b = MR.rad(b)
                rad_c, facs_c = MR.rad(c)
                rad_abc = rad_a * rad_b * rad_c
                if rad_abc < c:
                    sumc += c

    print(sumc)

#--------------------------------------------------------------------#

def f4(Nmax):
    print("--- f4 ---")

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

    class MemoRad(object):

        def calc(self, N):
            '''
            Return rad(N), and the list of distinct primes that make up
            rad(N). E.g.:
            504 = 2**3 * 3**2 * 7 -> rad(504) = 2*3*7 = 42
            return 42, [2,3,7]
            '''

            N_initial = N

            r = 1
            facs = []
            for prime in self.primes:
                if not N % prime:
                    r = r * prime
                    facs.append(prime)
                    N = N / prime
                while not N % prime:
                    N = N / prime
                if N == 1:
                    break
            
            self.cache[N_initial] = (r, facs)

        def __init__(self, primes):
            self.primes = primes
            self.cache = {}

        def rad(self, N):
            if not N in self.cache:
                self.calc(N)
            return self.cache[N]

    def invalid(i,facs):
        for fac in facs:
            if not i % fac:
                return True
        return False

    primes = get_primes(Nmax)
    MR = MemoRad(primes)

    sumc = 0
    for a in range(1,Nmax):
        rad_a, facs_a = MR.rad(a)
        invalids = {}
        for fac in facs_a:
            not_b = a + fac
            while not_b < Nmax:
                invalids[not_b] = True
                not_b += fac
        for b in range(a+1,Nmax-a):
            if not b in invalids:
                c = a + b
                rad_b, facs_b = MR.rad(b)
                rad_c, facs_c = MR.rad(c)
                rad_abc = rad_a * rad_b * rad_c
                if rad_abc < c:
                    sumc += c

    print(sumc)

#--------------------------------------------------------------------#

import timeit

f4(12000)
exit()

times = []
for i in [4]:
    t = timeit.Timer('f{0}(120000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
