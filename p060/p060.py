#--------------------------------------------------------------------#

def f1(max):
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
    for mult in range(3,max,2):
        if not mult in composites:
            # Log mult as prime:
            primes.append(mult)
            pd[mult] = True

            # Sieve its multiples away:
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    print primes[-1]
    # Explore combos:
    mx = len(str(max))
    K = Kosher(pd)
    for i1 in range(len(primes)):
        p1 = primes[i1]
        lp1 = len(str(p1))
        for i2 in range(i1+1,len(primes)):
            p2 = primes[i2]
            lp2 = len(str(p2))
            if lp1 + lp2 >= mx:
                print lp1+lp2
                print p1,p2
                break
            if K.are(p1,p2): # only go on if these are a-OK
                for i3 in range(i2+1,len(primes)):
                    p3 = primes[i3]
                    lp3 = len(str(p3))
                    if lp2 + lp3 >= mx:
                        print lp2+lp3
                        break
                    if K.are(p1,p3) and K.are(p2,p3):
                        for i4 in range(i3+1,len(primes)):
                            p4 = primes[i4]
                            lp4 = len(str(p4))
                            if lp3 + lp4 >= mx:
                                print lp3+lp4
                                break
                            if K.are(p1,p4) and K.are(p2,p4) and K.are(p3,p4):
                                print p1,p2,p3,p4
                                return
                                for i5 in range(i4+1,len(primes)):
                                    p5 = primes[i5]
                                    lp5 = len(str(p5))
                                    if lp4 + lp5 >= mx:
                                        break
                                    if K.are(p1,p5) and K.are(p2,p5) and K.are(p3,p5):
                                        print p5
                                        if K.are(p4,p5):
                                            print p1,p2,p3,p4,p5
                                            print p1+p2+p3+p4+p5
                                            return

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1(1000000)', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.1f} ms'.format(t1*1000)) # ~ 2.8 s
