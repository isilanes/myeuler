import timeit

#------------------------------------------------------------------------------#

def f4(maxn):
    print("--- f4 ---")

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
    for c in range(1,maxn//10):
        m = 10*c**2 - 1
        if not m % 3:
            n2 = 100*c**2
            p1 = n2 + 1
            if isprime(p1):
                p3 = n2 + 3
                if isprime(p3):
                    p7 = n2 + 7
                    if isprime(p7):
                        p9 = n2 + 9
                        if isprime(p9):
                            p13 = n2 + 13
                            if isprime(p13):
                                p27 = n2 + 27
                                if isprime(p27):
                                    tot += c
                                    print 10*c, p1, p3, p7, p9, p13, p27
    print(10*tot)

def f5(maxn):
    print("--- f5 ---")

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


    #primes = [3, 5, 7, 11, 13, 17, 19, 23, 29]
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

    print len(koshers), len(koshers)/float(mult)
    for i,e in enumerate(koshers[:-4]):
        if koshers[i+1] - e == 2:
            if koshers[i+2] - e == 6:
                if koshers[i+3] - e == 8:
                    if koshers[i+4] - e == 12:
                        if koshers[i+5] - e == 26:
                            print koshers[i:i+6]
                            continue


#------------------------------------------------------------------------------#

times = []
for i in [5]:
    t = timeit.Timer('f{0}(10**7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxp1  t (ms)

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
