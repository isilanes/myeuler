import math
import timeit

#------------------------------------------------------------------------------#

def f0(nmax):
    '''Incorrect. Off by one (less).'''

    print("--- f0 ---")

    # How many n values satisfy nsolreq:
    nreq = 0

    # Number of solutions required:
    nsolreq = 10

    # Loop for all n below nmax:
    for n in range(1,nmax):
        nsol = 0
        dmin = int(math.sqrt(n)/2)
        dmax = int((n+1)/4)
        for d in range(dmin,dmax+1):
            s = 4*d**2 - n
            if s > 0:
                rs = int(math.sqrt(s))
                if rs**2 == s:
                    y = 2*d - rs
                    if y - d > 0:
                        nsol += 1
                    y = 2*d + rs
                    if y - d > 0:
                        nsol += 1
        if nsol == nsolreq:
            nreq +=1

    print(nreq)

def f1(nmax):
    '''Incorrect. Off by one (less)'''

    print("--- f1 ---")

    # How many n values satisfy nsolreq:
    nreq = 0

    # Number of solutions required:
    nsolreq = 10

    # Loop for all n below nmax:
    for n in range(1,nmax):
        nsol = 0
        dmin = int(math.sqrt(n)/2)
        dmax = int((n+1)/4)
        for d in range(dmin,dmax+1):
            s = 4*d**2 - n
            if s > 0:
                rs = int(math.sqrt(s))
                if rs**2 == s:
                    if d - rs > 0: # then BOTH + and - are > 0
                        nsol += 2
                    else: # since d + rs > 0 always
                        nsol += 1
            if nsol > nsolreq:
                break
        if nsol == nsolreq:
            nreq +=1

    print(nreq)

def f2(nmax):
    '''Incorrect. Off by one (less)'''

    print("--- f2 ---")

    # Pregenerate all squares below nmax**2/4 (largest value of 4*d**2 - n).
    # nmax**2/4 = (nmax/2)**2, obviously.
    sqs = {}
    for i in range(1, nmax/2+1):
        sqs[i*i] = i

    # How many n values satisfy nsolreq:
    nreq = 0

    # Number of solutions required:
    nsolreq = 10

    # Loop for all n below nmax:
    for n in range(1,nmax):
        nsol = 0
        dmin = int(math.sqrt(n)/2)
        dmax = int((n+1)/4)
        for d in range(dmin,dmax+1):
            s = 4*d**2 - n
            try:
                rs = sqs[s]
            except:
                continue

            if d - rs > 0: # then BOTH + and - are > 0
                nsol += 2
            else: # since d + rs > 0 always
                nsol += 1

            if nsol > nsolreq:
                break

        if nsol == nsolreq:
            nreq +=1

    print(nreq)

def f3(nmax):
    '''Correct, but slow.'''

    print("--- f3 ---")

    freq = [ 0 for x in range(nmax+1) ]

    dmax = int((nmax+1)/4)
    for d in range(1, dmax+1):
        for y in range(d+1, 4*d):
            n = 4*y*d - y**2
            if n > 0 and n < nmax:
                freq[n] += 1

    nfreq = 0
    for i,e in enumerate(freq):
        if e == 10:
            nfreq += 1
    print(nfreq)

def f4(nmax):
    '''f3 slightly optimized.'''

    print("--- f4 ---")

    freq = [ 0 for x in range(nmax+1) ]

    dmax = int((nmax+1)/4)
    for d in range(1, dmax+1):
        fourd = 4*d
        for y in range(d+1, fourd):
            n = y*(fourd - y)
            if n < nmax:
                freq[n] += 1

    nfreq = 0
    for i,e in enumerate(freq):
        if e == 10:
            nfreq += 1
    print(nfreq)

def f5(nmax):
    '''f3 highly optimized.'''

    print("--- f5 ---")

    freq = [ 0 for x in range(nmax+1) ]

    dmax = int((nmax+1)/4)
    for d in range(1, dmax+1):
        fourd = 4*d
        if fourd*d < nmax:
            for y in range(d+1, fourd):
                n = y*(fourd - y)
                if n < nmax:
                    freq[n] += 1
        else:
            rs = int(math.sqrt(fourd*d - nmax))
            for y in range(d+1, 2*d-rs):
                n = y*(fourd - y)
                if n < nmax:
                    freq[n] += 1
            for y in range(2*d+rs, fourd):
                n = y*(fourd - y)
                if n < nmax:
                    freq[n] += 1

    nfreq = 0
    for i,e in enumerate(freq):
        if e == 10:
            nfreq += 1
    print(nfreq)


#------------------------------------------------------------------------------#

times = []
for i in [5]:
    t = timeit.Timer('f{0}(10**6)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  nmax  t (ms)
#      2000      33
#     10000     224
#    100000   15500
#   1000000   

# f1:  nmax  t (ms)
#      2000      34
#     10000     194
#    100000   16400
#   1000000   

# f2:  nmax  t (ms)
#      2000      
#     10000     394  
#    100000   23830
#   1000000   

# f3:  nmax  t (ms)
#      1000      15      
#     10000     190  
#    100000   16510
#   1000000 1667300  

# f4:  nmax  t (ms)
#      1000       8.6      
#     10000     157  
#    100000   14570
#   1000000  

# f5:  nmax  t (ms)
#      2000       2.4      
#     10000      16  
#    100000      45
#   1000000     168  

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
