#--------------------------------------------------------------------#

def f1(nmax):
    #
    # TOO SLOW!
    #
    print("--- f1 ---")

    class Kosher(object):

        def __init__(self, primes):
            self.primes = primes
        
        def are(self,a,b):
            '''
            Returns True if primes a and b also produce primes when
            concatenating them as ab and ba.
            '''

            pab = int(str(a)+str(b))
            if not pab in primes:
                return False

            pba = int(str(b)+str(a))
            if not pba in primes:
                return False
            
            return True

    # Sieve to find all primes up to max:
    composites = {}
    primes = [2]
    pd = {}
    for mult in range(3,nmax,2):
        if not mult in composites:
            # Log mult as prime:
            primes.append(mult)
            pd[mult] = True

            # Sieve its multiples away:
            for i in range(mult*mult, nmax, 2*mult):
                composites[i] = True

    # Explore combos:
    mx = len(str(nmax))+1
    K = Kosher(pd)
    n1 = n2 = n3 = n4 = 0
    for i1 in range(1,len(primes)):
        p1 = primes[i1]
        n1 += 1
        if len(str(p1))*2 >= mx:
            break
        for i2 in range(i1+1,len(primes)):
            p2 = primes[i2]
            n2 += 1
            if len(str(p2))*2 >= mx:
                break
            if K.are(p1,p2): # only go on if these are a-OK
                for i3 in range(i2+1,len(primes)):
                    p3 = primes[i3]
                    n3 += 1
                    if len(str(p3))*2 >= mx:
                        break
                    if K.are(p1,p3) and K.are(p2,p3):
                        for i4 in range(i3+1,len(primes)):
                            p4 = primes[i4]
                            n4 += 1
                            #if len(str(p4))+len(str(p3)) >= mx:
                            #    break
                            if len(str(p4))*2 >= mx:
                                break
                            if K.are(p1,p4) and K.are(p2,p4) and K.are(p3,p4):
                                print p1,p2,p3,p4
                                #found += 1
                                #if found > 3:
                                if True:
                                    print "n1 =", n1
                                    print "n2 =", n2
                                    print "n3 =", n3
                                    print "n4 =", n4
                                for i5 in range(i4+1,len(primes)):
                                    p5 = primes[i5]
                                    if len(str(p4)) + len(str(p5)) >= mx:
                                        break
                                    if K.are(p1,p5) and K.are(p2,p5) and K.are(p3,p5):
                                        print p5
                                        if K.are(p4,p5):
                                            print p1,p2,p3,p4,p5
                                            print p1+p2+p3+p4+p5
                                            return

#--------------------------------------------------------------------#

def f2(nmax):
    print("--- f2 ---")

    def isprime(num):
        '''
        Returns True if num is prime, False otherwise.
        '''

        # Only odd numbers are fed to this function, so no need
        # to check num % 2:
        for i in range(3,int(math.sqrt(num))+1,2):
            if not num % i:
                return False

        return True

    def kosher(a,b):
        '''
        Returns True if ab and ba are prime, False otherwise.
        '''

        ab = int(str(a)+str(b))
        if not isprime(ab):
            return False

        ba = int(str(b)+str(a))
        if not isprime(ba):
            return False

        return True

    # Find first nmax primes (excluding 2):
    primes = []
    i = 3
    while len(primes) < nmax:
        if isprime(i):
            primes.append(i)
        i += 2
    primes.remove(5) # 5 can not be in result (as b5 would be composite for any b)

    #print primes[-1]
    n = nmax - 1
    for i in range(n):
        p1 = primes[i]
        for j in range(i+1,n):
            p2 = primes[j]
            if kosher(p1,p2):
                for k in range(j+1,n):
                    p3 = primes[k]
                    if kosher(p1,p3) and kosher(p2,p3):
                        for l in range(k+1,n):
                            p4 = primes[l]
                            if kosher(p1,p4) and kosher(p2,p4) and kosher(p3,p4):
                                for m in range(l+1,n):
                                    p5 = primes[m]
                                    if kosher(p1,p5) and kosher(p2,p5) and kosher(p3,p5) and kosher(p4,p5):
                                        print p1+p2+p3+p4+p5, (p1,p2,p3,p4,p5)
                                        return

#--------------------------------------------------------------------#

def f3(nmax):
    print("--- f3 ---")

    class Kosher(object):

        def __init__(self):
            # Dictionarly of a -> B, where B is a list of integers b,
            # such that a, b, ab and ba are prime, and a < b:
            self.cache = {}

        def isprime(self,num):
            '''
            Returns True if num is prime, False otherwise.
            '''

            if num in self.cache:
                return True

            if not num % 2:
                return False

            for i in range(3,int(math.sqrt(num))+1,2):
                if not num % i:
                    return False

            # If we reach thus far, i is prime, and was not
            # in cache, so introduce it in cache and return True:
            self.cache[num] = []
            return True

        def kosher(self,a,b):
            '''
            Return True if ab and ba are prime, False otherwise.
            '''

            if b in self.cache[a]:
                return True

            ab = int(str(a)+str(b))
            if not self.isprime(ab):
                return False

            ba = int(str(b)+str(a))
            if not self.isprime(ba):
                return False

            self.cache[a].append(b)
            return True

        def koshers(self,mylist,b):
            '''
            Return True if self.kosher(a,b) is True for b and every
            prime a in mylist.
            '''

            for a in mylist:
                if not self.kosher(a,b):
                    return False

            return True

    K = Kosher()
    for i in range(3,nmax,2):
        if K.isprime(i):
            for j in range(i+2,nmax,2):
                if K.isprime(j) and K.kosher(i,j):
                    for k in range(j+2,nmax,2):
                        if K.isprime(k) and K.koshers([i,j],k):
                            for l in range(k+2,nmax,2):
                                if K.isprime(l) and K.koshers([i,j,k],l):
                                    for m in range(l+2,nmax,2):
                                        if K.isprime(m) and K.koshers([i,j,k,l],m):
                                            print i+j+k+l+m, (i,j,k,l,m)
                                            return

#--------------------------------------------------------------------#

import math
import timeit

# f1():
t = timeit.Timer('f1(1000)', "from __main__ import f1")
t1 = t.timeit(number=1)

# f2():
t = timeit.Timer('f2(1200)', "from __main__ import f2")
t2 = t.timeit(number=1)

# f3():
t = timeit.Timer('f3(9000)', "from __main__ import f3")
t3 = t.timeit(number=1)

# f2() and f3() are equivalent
print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # doesn't work
print('t2 = {0:.1f} ms'.format(t2*1000)) # ~ 2 s
print('t3 = {0:.1f} ms'.format(t3*1000)) # ~ 2.1 s
