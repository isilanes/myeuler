#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")
    
    import math
    
    nodds = 0
    for N in range(2,10001):
        sN = math.sqrt(N)
        a0 = int(sN)
        # Avoid if perfect square:
        if a0*a0 == N:
            continue
        A, B = 1, a0
        
        trios = []
        while True:
            newA = (N - B**2)/A
            newB = a0 - (a0 + B) % newA
            ai = (a0 + B) / newA
            A, B = newA, newB
            trio = [ai, A, B]
            
            if trio in trios: # then we reached periodicity:
                if len(trios) % 2:
                    nodds += 1
                break
            else:
                trios.append(trio)
        
    print nodds

#--------------------------------------------------------------------#

def f1():
    '''
    by schwarznecken on https://projecteuler.net/thread=64;page=9
    '''
    print("--- f1 ---")

    import math
    
    def sqrtcontinuedfrac(d):
        p = int(math.floor(math.sqrt(d)))
        q = d - p ** 2
        while q > 0:
            a = int(math.floor((p + math.sqrt(d)) / q))
            yield (a, p, q)
            p = a * q - p
            q = (d - p ** 2) / q

    def cfraccount(d):
        L = []
        for t in sqrtcontinuedfrac(d):
            if len(L) > 0 and t == L[0]:
                return len(L)
            L.append(t)
        return len(L)

    c = 0
    for i in xrange(1, 10001):
        if cfraccount(i) % 2:
            c += 1

    print c

#--------------------------------------------------------------------#

def f2():
    '''
    by BasharTeg on https://projecteuler.net/thread=64;page=8
    '''
    print("--- f2 ---")

    import math
       
    def cont_fract(n):
       m = 0
       d = 1
       a_0 = a = math.floor(math.sqrt(n))
       iteration = 0
       while a != 2*a_0:
          m = d*a - m
          d = (n - m**2)/d
          a = math.floor((a_0+m)/d)
          iteration+=1
       return iteration

    count = 0
    for i in range(10001):
       if math.sqrt(i) % 1 != 0 and cont_fract(i) % 2 != 0:
          count+=1
          
    print count

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(3):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
